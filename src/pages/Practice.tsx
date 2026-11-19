import { useEffect, useMemo, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { SUBJECTS, getSubject, type SubjectId } from '../content/syllabus';
import { questionsFor } from '../content';
import { buildPractice, getQuestion } from '../lib/questions';
import type { Difficulty, Question } from '../lib/types';
import { PracticeSession } from '../components/PracticeSession';
import { setLastLocation, useAppState } from '../lib/store';

const COUNTS = [5, 10, 20, 30];

export function Practice() {
  const [params, setParams] = useSearchParams();
  const state = useAppState();
  const initialSubject = (getSubject(params.get('subject') ?? '')?.id ?? 'math') as SubjectId;
  const [subject, setSubject] = useState<SubjectId>(initialSubject);
  const [subtopics, setSubtopics] = useState<string[]>(() => (params.get('subtopics') ? params.get('subtopics')!.split(',') : []));
  const [diffs, setDiffs] = useState<Difficulty[]>([]);
  const [count, setCount] = useState(10);
  const [includeGenerated, setIncludeGenerated] = useState(true);
  const [flaggedOnly, setFlaggedOnly] = useState(false);
  const [session, setSession] = useState<Question[] | null>(null);

  const subj = getSubject(subject)!;
  const seen = useMemo(() => new Set(state.attempts.map((a) => a.qid)), [state.attempts]);
  const available = useMemo(
    () => questionsFor(subject, subtopics).filter((q) => diffs.length === 0 || diffs.includes(q.difficulty)).filter((q) => !flaggedOnly || state.flags.includes(q.id)),
    [subject, subtopics, diffs, flaggedOnly, state.flags],
  );

  const start = () => {
    let qs: Question[];
    if (flaggedOnly) {
      const flagged = state.flags.map(getQuestion).filter((q): q is Question => !!q && q.subject === subject);
      qs = flagged.filter((q) => (subtopics.length === 0 || subtopics.includes(q.subtopic)) && (diffs.length === 0 || diffs.includes(q.difficulty))).slice(0, count);
    } else qs = buildPractice({ subject, subtopics, difficulties: diffs, count, includeGenerated: subject === 'math' && includeGenerated, preferUnseen: seen });
    if (qs.length === 0) return;
    setSession(qs);
    setLastLocation({ path: `/practice?subject=${subject}${subtopics.length ? `&subtopics=${subtopics.join(',')}` : ''}`, label: `Practice: ${subj.name}${subtopics.length === 1 ? ` – ${subj.topics.flatMap((t) => t.subtopics).find((s) => s.id === subtopics[0])?.name}` : ''}` });
  };

  // "Practice this topic" links use ?start=1
  useEffect(() => {
    if (params.get('start') === '1' && !session) {
      start();
      params.delete('start');
      setParams(params, { replace: true });
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (session) {
    return (
      <PracticeSession
        key={session.map((q) => q.id).join()}
        questions={session}
        mode="practice"
        title={`${subj.name} practice`}
        onExit={() => setSession(null)}
        onRestart={(qs) => setSession([...qs])}
      />
    );
  }

  const toggle = (id: string) => setSubtopics((s) => (s.includes(id) ? s.filter((x) => x !== id) : [...s, id]));
  const toggleTopic = (ids: string[]) => setSubtopics((s) => (ids.every((id) => s.includes(id)) ? s.filter((x) => !ids.includes(x)) : [...new Set([...s, ...ids])]));
  const toggleDiff = (d: Difficulty) => setDiffs((s) => (s.includes(d) ? s.filter((x) => x !== d) : [...s, d]));

  return (
    <div className="stack">
      <h1>Practice</h1>
      <p className="muted">Instant feedback with a full solution after every question. Wrong answers go to your Mistakes notebook automatically.</p>

      <div className="card">
        <h2>1. Subject</h2>
        <div className="tabs" role="tablist">
          {SUBJECTS.map((s) => (
            <button key={s.id} role="tab" aria-selected={subject === s.id} className={`tab ${subject === s.id ? 'active' : ''}`} onClick={() => { setSubject(s.id); setSubtopics([]); }}>
              {s.name}
            </button>
          ))}
        </div>

        <h2>2. Topics <span className="small muted">({subtopics.length === 0 ? 'all' : `${subtopics.length} selected`})</span></h2>
        <div className="grid grid-2">
          {subj.topics.map((t) => {
            const ids = t.subtopics.map((s) => s.id);
            const all = ids.every((id) => subtopics.includes(id));
            return (
              <fieldset key={t.id} style={{ border: '1px solid var(--border)', borderRadius: 10, padding: '8px 12px' }}>
                <legend>
                  <label className="row" style={{ gap: 6, fontWeight: 700 }}>
                    <input type="checkbox" checked={all} onChange={() => toggleTopic(ids)} /> {t.name}
                  </label>
                </legend>
                {t.subtopics.map((st) => (
                  <label key={st.id} className="check-row" style={{ padding: '4px 0' }}>
                    <input type="checkbox" checked={subtopics.includes(st.id)} onChange={() => toggle(st.id)} />
                    <span>
                      {st.name} <span className="small muted">({questionsFor(subject, [st.id]).length})</span>
                    </span>
                  </label>
                ))}
              </fieldset>
            );
          })}
        </div>
        {subtopics.length > 0 && (
          <button className="btn small mt" onClick={() => setSubtopics([])}>Clear selection (use all topics)</button>
        )}

        <h2>3. Difficulty <span className="small muted">({diffs.length === 0 ? 'all' : diffs.length + ' selected'})</span></h2>
        <div className="row">
          {([1, 2, 3] as Difficulty[]).map((d) => (
            <label key={d} className="check-row" style={{ marginRight: 16 }}>
              <input type="checkbox" checked={diffs.includes(d)} onChange={() => toggleDiff(d)} />
              {['', 'Easy', 'Medium', 'Hard'][d]}
            </label>
          ))}
        </div>

        <h2>4. Number of questions</h2>
        <div className="tabs">
          {COUNTS.map((c) => (
            <button key={c} className={`tab ${count === c ? 'active' : ''}`} onClick={() => setCount(c)} aria-pressed={count === c}>
              {c}
            </button>
          ))}
        </div>
        {subject === 'math' && (
          <label className="check-row">
            <input type="checkbox" checked={includeGenerated} onChange={(e) => setIncludeGenerated(e.target.checked)} />
            <span>Mix in freshly generated math questions (unlimited variety)</span>
          </label>
        )}
        <label className="check-row">
          <input type="checkbox" checked={flaggedOnly} onChange={(e) => setFlaggedOnly(e.target.checked)} />
          <span>Only questions I have flagged ({state.flags.filter((f) => getQuestion(f)?.subject === subject).length})</span>
        </label>

        <div className="spread mt">
          <span className="muted small">{available.length} matching questions in the bank{subject === 'math' && includeGenerated && !flaggedOnly ? ' + generated' : ''}</span>
          <button className="btn primary" onClick={start} disabled={available.length === 0 && !(subject === 'math' && includeGenerated && !flaggedOnly)}>
            Start practice →
          </button>
        </div>
      </div>
    </div>
  );
}
