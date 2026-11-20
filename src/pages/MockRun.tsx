import { useCallback, useEffect, useRef, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { QuestionCard } from '../components/QuestionCard';
import { getQuestion } from '../lib/questions';
import { getState, setActiveMock, setLastLocation, submitMockResult, useAppState } from '../lib/store';
import { scoreMock } from '../lib/scoring';
import { formatClock } from '../lib/dates';
import type { ActiveMock, MockResult, Question } from '../lib/types';

export function MockRun() {
  const state = useAppState();
  const m = state.activeMock;
  const nav = useNavigate();
  const [now, setNow] = useState(Date.now());
  const [confirming, setConfirming] = useState(false);
  const enteredAt = useRef(Date.now());
  const submitted = useRef(false);

  const questions: Question[] = m ? (m.qids.map(getQuestion).filter(Boolean) as Question[]) : [];

  /** Add the time spent on the current question and return the updated mock. */
  const withTime = useCallback((mock: ActiveMock): ActiveMock => {
    const t = Date.now();
    const spent = t - enteredAt.current;
    enteredAt.current = t;
    const timePerQ = mock.timePerQ.slice();
    timePerQ[mock.current] = (timePerQ[mock.current] ?? 0) + Math.max(0, spent);
    return { ...mock, timePerQ };
  }, []);

  const submit = useCallback(
    (auto: boolean) => {
      const cur = getState().activeMock;
      if (!cur || submitted.current) return;
      submitted.current = true;
      const fin = withTime(cur);
      const qs = fin.qids.map(getQuestion).filter(Boolean) as Question[];
      const { correct, total, score } = scoreMock(qs, fin.answers);
      const finishedTs = Math.min(Date.now(), fin.endsTs);
      const result: MockResult = {
        id: fin.id,
        subject: fin.subject,
        kind: fin.kind,
        fixedId: fin.fixedId,
        title: fin.title,
        startedTs: fin.startedTs,
        finishedTs,
        durationMs: finishedTs - fin.startedTs,
        qids: fin.qids,
        answers: fin.answers,
        timePerQ: fin.timePerQ,
        flagged: fin.flagged,
        correct,
        total,
        score,
        autoSubmitted: auto,
      };
      submitMockResult(result, qs);
      setLastLocation({ path: `/mock/result/${fin.id}`, label: `Review your mock: ${fin.title} (${score}/100)` });
      nav(`/mock/result/${fin.id}`, { replace: true });
    },
    [nav, withTime],
  );

  useEffect(() => {
    const id = window.setInterval(() => setNow(Date.now()), 1000);
    return () => window.clearInterval(id);
  }, []);

  useEffect(() => {
    if (m && now >= m.endsTs) submit(true);
  }, [now, m, submit]);

  // warn before leaving the page mid-exam
  useEffect(() => {
    const h = (e: BeforeUnloadEvent) => {
      e.preventDefault();
    };
    window.addEventListener('beforeunload', h);
    return () => window.removeEventListener('beforeunload', h);
  }, []);

  if (!m) {
    return (
      <div className="card">
        <h1>No mock exam in progress</h1>
        <Link className="btn primary" to="/mock">Choose a mock exam</Link>
      </div>
    );
  }

  const q = questions[m.current];
  const remaining = Math.max(0, m.endsTs - now);
  const answeredCount = m.answers.filter((a) => a !== null).length;
  const flaggedCount = m.flagged.filter(Boolean).length;

  const update = (fn: (mock: ActiveMock) => ActiveMock) => {
    const cur = getState().activeMock;
    if (cur) setActiveMock(fn(cur));
  };
  const goTo = (i: number) => {
    if (i < 0 || i >= m.qids.length) return;
    update((cur) => ({ ...withTime(cur), current: i }));
  };
  const select = (choice: number) =>
    update((cur) => {
      const answers = cur.answers.slice();
      answers[cur.current] = answers[cur.current] === choice ? null : choice;
      return { ...cur, answers };
    });
  const toggleFlag = () =>
    update((cur) => {
      const flagged = cur.flagged.slice();
      flagged[cur.current] = !flagged[cur.current];
      return { ...cur, flagged };
    });

  return (
    <div>
      <div className="mock-bar">
        <div>
          <strong>{m.title}</strong>
          <div className="small muted">
            {answeredCount}/{m.qids.length} answered{flaggedCount ? ` · ${flaggedCount} flagged` : ''}
          </div>
        </div>
        <div className="row">
          <span className={`timer ${remaining < 5 * 60 * 1000 ? 'low' : ''}`} role="timer" aria-live="off" aria-label={`Time remaining ${formatClock(remaining)}`}>
            ⏱ {formatClock(remaining)}
          </span>
          <button className="btn primary" onClick={() => setConfirming(true)}>
            Submit
          </button>
        </div>
      </div>

      {confirming && (
        <div className="notice warn mb" role="alertdialog" aria-label="Confirm submission">
          <p style={{ marginTop: 0 }}>
            Submit now? {m.qids.length - answeredCount > 0 ? <strong>{m.qids.length - answeredCount} question(s) are unanswered</strong> : 'All questions are answered.'}
            {flaggedCount > 0 && ` ${flaggedCount} question(s) are flagged for review.`}
          </p>
          <div className="row">
            <button className="btn primary" onClick={() => submit(false)}>
              Yes, submit
            </button>
            <button className="btn" onClick={() => setConfirming(false)}>
              Keep working
            </button>
          </div>
        </div>
      )}

      <div className="mock-layout">
        <div className="stack">
          {q ? (
            <QuestionCard
              key={q.id}
              question={q}
              index={m.current}
              total={m.qids.length}
              selected={m.answers[m.current]}
              mode="exam"
              onSelect={select}
              onNext={() => goTo(m.current + 1)}
              showNextButton={false}
              flagged={m.flagged[m.current]}
              onToggleFlag={toggleFlag}
              keyboard
            />
          ) : (
            <div className="card">Question not found.</div>
          )}
          <div className="spread">
            <button className="btn" onClick={() => goTo(m.current - 1)} disabled={m.current === 0}>
              ← Previous
            </button>
            {m.current < m.qids.length - 1 ? (
              <button className="btn primary" onClick={() => goTo(m.current + 1)}>
                Next →
              </button>
            ) : (
              <button className="btn primary" onClick={() => setConfirming(true)}>
                Finish &amp; submit
              </button>
            )}
          </div>
          <p className="small muted">Tip: about {Math.round((60 * 60) / m.qids.length)} seconds per question. Flag hard ones and come back later. Click a chosen answer again to clear it.</p>
        </div>
        <aside className="card" aria-label="Question navigator">
          <h3>Questions</h3>
          <div className="navigator">
            {m.qids.map((id, i) => (
              <button
                key={id}
                className={`nav-cell ${m.answers[i] !== null ? 'answered' : ''} ${m.flagged[i] ? 'flagged' : ''} ${i === m.current ? 'current' : ''}`}
                onClick={() => goTo(i)}
                aria-label={`Question ${i + 1}${m.answers[i] !== null ? ', answered' : ''}${m.flagged[i] ? ', flagged' : ''}`}
                aria-current={i === m.current}
              >
                {i + 1}
              </button>
            ))}
          </div>
          <div className="small muted mt">
            <span className="chip">answered</span> <span className="chip warn">● flagged</span>
          </div>
        </aside>
      </div>
    </div>
  );
}
