import { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { removeMistake, setLastLocation, useAppState } from '../lib/store';
import { isDue, orderForReview, progressLabel, REQUIRED_CORRECT_DAYS } from '../lib/srs';
import { getQuestion } from '../lib/questions';
import { SUBJECTS, getSubject, subtopicName, type SubjectId } from '../content/syllabus';
import { PracticeSession } from '../components/PracticeSession';
import { Md } from '../components/Md';
import { formatDate, toDateKey } from '../lib/dates';
import type { Question } from '../lib/types';

export function Mistakes() {
  const state = useAppState();
  const [filter, setFilter] = useState<SubjectId | 'all'>('all');
  const [session, setSession] = useState<Question[] | null>(null);
  const ordered = useMemo(() => orderForReview(state.mistakes), [state.mistakes]);
  const list = ordered.filter((m) => filter === 'all' || m.subject === filter);
  const due = list.filter((m) => isDue(m));

  if (session) {
    return (
      <PracticeSession
        key={session.map((q) => q.id).join()}
        questions={session}
        mode="mistakes"
        title="Retrying mistakes"
        onExit={() => setSession(null)}
        onRestart={(qs) => setSession([...qs])}
      />
    );
  }

  const start = (entries: typeof list) => {
    const qs = entries
      .slice(0, 20)
      .map((m) => getQuestion(m.qid))
      .filter((q): q is Question => !!q);
    if (qs.length) {
      setLastLocation({ path: '/mistakes', label: 'Mistakes notebook' });
      setSession(qs);
    }
  };

  return (
    <div className="stack">
      <h1>Mistakes notebook</h1>
      <p className="muted">
        Every wrong answer is saved here automatically. A question leaves the notebook once you answer it correctly on {REQUIRED_CORRECT_DAYS} different days — spaced repetition, so
        it really sticks. Getting it wrong again resets its progress.
      </p>
      <div className="card">
        <div className="tabs">
          {(['all', ...SUBJECTS.map((s) => s.id)] as (SubjectId | 'all')[]).map((f) => (
            <button key={f} className={`tab ${filter === f ? 'active' : ''}`} onClick={() => setFilter(f)}>
              {f === 'all' ? 'All' : getSubject(f)!.name} ({ordered.filter((m) => f === 'all' || m.subject === f).length})
            </button>
          ))}
        </div>
        <div className="spread">
          <span>
            <strong>{due.length}</strong> due today · {list.length - due.length} already answered correctly today
          </span>
          <span className="row">
            <button className="btn primary" disabled={due.length === 0} onClick={() => start(due)}>
              Retry my mistakes ({Math.min(20, due.length)})
            </button>
            <button className="btn" disabled={list.length === 0} onClick={() => start(list)}>
              Retry all
            </button>
          </span>
        </div>
      </div>

      {list.length === 0 ? (
        <div className="card center">
          <p>No mistakes here. 🎉</p>
          <Link className="btn primary" to="/practice">Practise some questions</Link>
        </div>
      ) : (
        <div className="topic-list">
          {list.map((m) => {
            const q = getQuestion(m.qid);
            return (
              <div key={m.qid} className="topic-item" style={{ alignItems: 'flex-start' }}>
                <div style={{ minWidth: 0, flex: 1 }}>
                  <div className="qmeta" style={{ marginBottom: 4 }}>
                    <span className={`chip ${m.subject}`}>{getSubject(m.subject)?.short}</span>
                    <span className="chip">{subtopicName(m.subject, m.subtopic)}</span>
                    <span className={`chip ${isDue(m) ? 'warn' : 'good'}`}>{isDue(m) ? 'due' : 'done today'}</span>
                    <span className="chip">{progressLabel(m)}</span>
                  </div>
                  {q ? <Md className="small">{q.question.length > 220 ? q.question.slice(0, 220).replace(/\$[^$]*$/, '') + '…' : q.question}</Md> : <span className="muted">Question no longer exists.</span>}
                  <div className="small muted">
                    Wrong {m.wrongCount}× · last on {formatDate(toDateKey(m.lastWrongTs))}
                  </div>
                </div>
                <button className="btn small" onClick={() => removeMistake(m.qid)} aria-label="Remove from notebook">
                  Remove
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
