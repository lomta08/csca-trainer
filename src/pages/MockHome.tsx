import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { SUBJECTS, EXAM, getSubject, type SubjectId } from '../content/syllabus';
import { FIXED_MOCKS, QUESTIONS } from '../content';
import { selectMockQuestions, MOCK_MS } from '../lib/mock';
import { randomSeed } from '../lib/rng';
import { setActiveMock, useAppState, setLastLocation } from '../lib/store';
import { LineChart } from '../components/LineChart';
import { formatClock, formatDate, toDateKey } from '../lib/dates';
import { scoreBand } from '../lib/scoring';
import type { ActiveMock } from '../lib/types';

export function MockHome() {
  const state = useAppState();
  const nav = useNavigate();
  const [subject, setSubject] = useState<SubjectId>('math');
  const subj = getSubject(subject)!;
  const active = state.activeMock;

  const start = (qids: string[], kind: 'random' | 'fixed', title: string, fixedId?: string) => {
    if (active && !window.confirm('You have a mock exam in progress. Abandon it and start a new one?')) return;
    const now = Date.now();
    const m: ActiveMock = {
      id: `mock-${now}`,
      subject,
      kind,
      fixedId,
      title,
      qids,
      answers: qids.map(() => null),
      flagged: qids.map(() => false),
      timePerQ: qids.map(() => 0),
      current: 0,
      startedTs: now,
      endsTs: now + MOCK_MS,
    };
    setActiveMock(m);
    setLastLocation({ path: '/mock/run', label: `Mock exam in progress: ${title}` });
    nav('/mock/run');
  };

  const startRandom = () => {
    const qs = selectMockQuestions(QUESTIONS, subject, randomSeed());
    start(qs.map((q) => q.id), 'random', `${subj.name} random mock`);
  };

  const history = state.mocks.slice().sort((a, b) => b.finishedTs - a.finishedTs);
  const series = SUBJECTS.map((s) => ({
    name: s.name,
    color: `var(--${s.id})`,
    points: state.mocks
      .filter((m) => m.subject === s.id)
      .sort((a, b) => a.finishedTs - b.finishedTs)
      .map((m, i) => ({ x: i + 1, y: m.score, label: formatDate(toDateKey(m.finishedTs)) })),
  })).filter((s) => s.points.length > 0);

  const fixed = FIXED_MOCKS[subject] ?? [];
  const bankSize = QUESTIONS.filter((q) => q.subject === subject).length;

  return (
    <div className="stack">
      <h1>Mock exams</h1>
      <p className="muted">
        A realistic simulation: {EXAM.questions} single-answer questions, {EXAM.minutes}-minute timer, topic mix weighted like the syllabus, no feedback until you submit, and
        automatic submission when time is up. Scored 0–100.
      </p>

      {active && (
        <div className="notice warn spread">
          <span>
            <strong>{active.title}</strong> is in progress — {formatClock(Math.max(0, active.endsTs - Date.now()))} left.
          </span>
          <Link className="btn primary" to="/mock/run">Resume</Link>
        </div>
      )}

      <div className="card">
        <div className="tabs" role="tablist">
          {SUBJECTS.map((s) => (
            <button key={s.id} role="tab" aria-selected={subject === s.id} className={`tab ${subject === s.id ? 'active' : ''}`} onClick={() => setSubject(s.id)}>
              {s.name}
            </button>
          ))}
        </div>
        <div className="grid grid-2">
          <div className="card">
            <h3>Random mock</h3>
            <p className="muted small">A new paper every time, drawn from {bankSize} {subj.name.toLowerCase()} questions with the syllabus weighting:</p>
            <ul className="small">
              {subj.topics.map((t) => (
                <li key={t.id}>
                  {t.name}: {t.mockCount} questions
                </li>
              ))}
            </ul>
            <button className="btn primary" onClick={startRandom} disabled={bankSize < EXAM.questions}>
              Start random mock
            </button>
          </div>
          <div className="card">
            <h3>Fixed mocks</h3>
            <p className="muted small">The same paper each time, so you can measure progress. The three papers do not share questions.</p>
            <div className="stack">
              {fixed.map((f) => {
                const tries = state.mocks.filter((m) => m.fixedId === f.id);
                const best = tries.length ? Math.max(...tries.map((t) => t.score)) : null;
                return (
                  <div key={f.id} className="spread">
                    <span>
                      <strong>{f.title}</strong>
                      <span className="small muted"> · {best === null ? 'not attempted' : `best ${best}/100 (${tries.length} attempt${tries.length > 1 ? 's' : ''})`}</span>
                    </span>
                    <button className="btn small" onClick={() => start(f.qids, 'fixed', f.title, f.id)}>
                      Start
                    </button>
                  </div>
                );
              })}
              {fixed.length === 0 && <p className="muted">No fixed mocks for this subject yet.</p>}
            </div>
          </div>
        </div>
      </div>

      <div className="card">
        <h2>Score trend</h2>
        {series.length ? <LineChart series={series} ariaLabel="Mock exam scores over time" /> : <p className="muted">Finish a mock exam to see your score trend here.</p>}
      </div>

      <div className="card">
        <h2>History</h2>
        {history.length === 0 ? (
          <p className="muted">No mock exams yet.</p>
        ) : (
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Paper</th>
                  <th>Score</th>
                  <th>Correct</th>
                  <th>Time</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {history.map((m) => (
                  <tr key={m.id}>
                    <td>{formatDate(toDateKey(m.finishedTs))}</td>
                    <td>{m.title}</td>
                    <td>
                      <strong>{m.score}</strong> <span className="small muted">{scoreBand(m.score)}</span>
                    </td>
                    <td>
                      {m.correct}/{m.total}
                    </td>
                    <td>{formatClock(m.durationMs)}{m.autoSubmitted ? ' (time up)' : ''}</td>
                    <td>
                      <Link to={`/mock/result/${m.id}`}>Review</Link>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
