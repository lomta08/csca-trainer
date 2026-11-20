import { useMemo, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useAppState } from '../lib/store';
import { getQuestion } from '../lib/questions';
import { breakdownBySubtopic, scoreBand } from '../lib/scoring';
import { subtopicName, topicName } from '../content/syllabus';
import { QuestionCard } from '../components/QuestionCard';
import { formatClock, formatDate, toDateKey } from '../lib/dates';
import type { Question } from '../lib/types';

type Filter = 'all' | 'wrong' | 'flagged' | 'slow';

export function MockResult() {
  const { id } = useParams();
  const state = useAppState();
  const r = state.mocks.find((x) => x.id === id);
  const [filter, setFilter] = useState<Filter>('wrong');
  const [focus, setFocus] = useState<number | null>(null);

  const questions = useMemo(() => (r ? (r.qids.map(getQuestion) as (Question | undefined)[]) : []), [r]);
  if (!r) {
    return (
      <div className="card">
        <h1>Result not found</h1>
        <Link to="/mock">Back to mock exams</Link>
      </div>
    );
  }
  const qs = questions.filter(Boolean) as Question[];
  const rows = breakdownBySubtopic(qs, r.answers, r.timePerQ).sort((a, b) => a.correct / a.total - b.correct / b.total);
  const unanswered = r.answers.filter((a) => a === null).length;
  const avgTime = r.timePerQ.reduce((s, t) => s + t, 0) / Math.max(1, r.qids.length);
  const slowCut = [...r.timePerQ].sort((a, b) => b - a)[Math.min(9, r.timePerQ.length - 1)] ?? 0;

  const visible = r.qids
    .map((_, i) => i)
    .filter((i) => {
      const q = questions[i];
      if (!q) return false;
      if (filter === 'wrong') return r.answers[i] !== q.answer;
      if (filter === 'flagged') return r.flagged[i];
      if (filter === 'slow') return r.timePerQ[i] >= slowCut && r.timePerQ[i] > 0;
      return true;
    });

  return (
    <div className="stack">
      <div className="spread">
        <h1 style={{ margin: 0 }}>{r.title}</h1>
        <Link className="btn small" to="/mock">All mock exams</Link>
      </div>
      <div className="card">
        <div className="grid grid-3">
          <div className="stat">
            <span className="value" style={{ fontSize: '2.6rem' }}>{r.score}</span>
            <span className="label">score out of 100 · {scoreBand(r.score)}</span>
          </div>
          <div className="stat">
            <span className="value">
              {r.correct}/{r.total}
            </span>
            <span className="label">correct ({unanswered} unanswered)</span>
          </div>
          <div className="stat">
            <span className="value">{formatClock(r.durationMs)}</span>
            <span className="label">
              time used{r.autoSubmitted ? ' — auto-submitted at time-up' : ''} · avg {Math.round(avgTime / 1000)} s/question
            </span>
          </div>
        </div>
        <p className="small muted" style={{ marginBottom: 0 }}>
          Taken {formatDate(toDateKey(r.finishedTs))}. Wrong and unanswered questions were added to your <Link to="/mistakes">Mistakes notebook</Link>.
        </p>
      </div>

      <div className="card">
        <h2>Per-topic breakdown</h2>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Topic</th>
                <th>Correct</th>
                <th style={{ minWidth: 120 }}>Accuracy</th>
                <th>Avg time</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {rows.map((row) => {
                const pct = Math.round((100 * row.correct) / row.total);
                return (
                  <tr key={row.key}>
                    <td>
                      {subtopicName(r.subject, row.subtopic)}
                      <div className="small muted">{topicName(r.subject, row.topic)}</div>
                    </td>
                    <td>
                      {row.correct}/{row.total}
                    </td>
                    <td>
                      <div className={`progress ${pct >= 70 ? 'good' : pct >= 50 ? 'warn' : 'bad'}`}>
                        <span style={{ width: `${pct}%` }} />
                      </div>
                      <span className="small">{pct}%</span>
                    </td>
                    <td className="small">{Math.round(row.timeMs / row.total / 1000)} s</td>
                    <td>
                      <Link className="small" to={`/learn/${r.subject}/${row.subtopic}`}>Notes</Link>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      <div className="card">
        <h2>Answer map</h2>
        <div className="navigator">
          {r.qids.map((qid, i) => {
            const q = questions[i];
            const ok = q && r.answers[i] === q.answer;
            return (
              <button
                key={qid}
                className={`nav-cell ${ok ? 'correct' : 'wrong'} ${r.flagged[i] ? 'flagged' : ''}`}
                onClick={() => {
                  setFilter('all');
                  setFocus(i);
                  setTimeout(() => document.getElementById(`review-${i}`)?.scrollIntoView({ behavior: 'smooth' }), 50);
                }}
                aria-label={`Question ${i + 1}: ${ok ? 'correct' : r.answers[i] === null ? 'unanswered' : 'wrong'}`}
              >
                {i + 1}
              </button>
            );
          })}
        </div>
      </div>

      <div className="card">
        <div className="spread">
          <h2 style={{ margin: 0 }}>Review with solutions</h2>
          <div className="tabs" style={{ margin: 0 }}>
            {(
              [
                ['wrong', 'Wrong / unanswered'],
                ['flagged', 'Flagged'],
                ['slow', 'Slowest 10'],
                ['all', 'All'],
              ] as [Filter, string][]
            ).map(([f, label]) => (
              <button key={f} className={`tab ${filter === f ? 'active' : ''}`} onClick={() => setFilter(f)}>
                {label}
              </button>
            ))}
          </div>
        </div>
      </div>
      {visible.length === 0 && <p className="muted center">Nothing to show for this filter.</p>}
      {visible.map((i) => (
        <div key={i} id={`review-${i}`} style={focus === i ? { outline: '3px solid var(--primary)', borderRadius: 12 } : undefined}>
          <div className="small muted" style={{ margin: '0 0 4px 4px' }}>
            Time spent: {Math.round((r.timePerQ[i] ?? 0) / 1000)} s
          </div>
          <QuestionCard question={questions[i]!} index={i} total={r.qids.length} selected={r.answers[i]} mode="review" />
        </div>
      ))}
    </div>
  );
}
