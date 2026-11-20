import { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { SUBJECTS, EXAM, getSubject } from '../content/syllabus';
import { setExamDate, useAppState } from '../lib/store';
import { subjectProgress, subtopicStats, weakestTopics, streak, totalStudyMs } from '../lib/stats';
import { daysBetween, formatDate, formatDuration, toDateKey } from '../lib/dates';
import { orderForReview } from '../lib/srs';
import { currentWeekIndex, planProgress } from '../lib/plan';
import { QUESTIONS } from '../content';

const PROGRAM_TABLE: [string, string][] = [
  ['English-taught liberal arts, economics, management', 'Mathematics'],
  ['English-taught science and engineering', 'Mathematics + Physics'],
  ['English-taught medicine', 'Mathematics + Physics + Chemistry'],
  ['Chinese-taught programmes', 'the above + Professional Chinese (Humanities or STEM)'],
];

function Bar({ value, cls = '', label = 'Progress' }: { value: number; cls?: string; label?: string }) {
  return (
    <div className={`progress ${cls}`} role="progressbar" aria-label={label} aria-valuenow={Math.round(value * 100)} aria-valuemin={0} aria-valuemax={100}>
      <span style={{ width: `${Math.max(0, Math.min(100, value * 100))}%` }} />
    </div>
  );
}

export function Home() {
  const state = useAppState();
  const [editingDate, setEditingDate] = useState(false);
  const today = toDateKey();
  const daysLeft = state.examDate ? daysBetween(today, state.examDate) : null;
  const progress = useMemo(() => subjectProgress(state), [state]);
  const stats = useMemo(() => subtopicStats(state.attempts), [state.attempts]);
  const weak = weakestTopics(stats, 5);
  const due = orderForReview(state.mistakes).filter((m) => !m.correctDays.includes(today)).length;
  const st = streak(state);
  const studied = totalStudyMs(state);
  const plan = state.plan;
  const pp = plan ? planProgress(plan) : null;
  const thisWeek = plan ? plan.weeks[currentWeekIndex(plan)] : null;
  const nextTasks = thisWeek ? thisWeek.items.filter((i) => !i.done).slice(0, 3) : [];
  const newUser = state.attempts.length === 0 && state.mocks.length === 0;

  return (
    <div className="stack">
      <div className="spread">
        <div>
          <h1 style={{ marginBottom: 4 }}>{state.name ? `Welcome back, ${state.name}` : 'CSCA Trainer'}</h1>
          <p className="muted" style={{ margin: 0 }}>
            Practice for the CSCA Mathematics, Physics and Chemistry papers — {QUESTIONS.length} original questions, unlimited generated maths, full mock exams.
          </p>
        </div>
      </div>

      <div className="grid grid-3">
        <div className="card">
          <div className="stat">
            {daysLeft !== null && !editingDate ? (
              <>
                <span className="value">{daysLeft > 0 ? daysLeft : daysLeft === 0 ? 'Today!' : 'Past'}</span>
                <span className="label">{daysLeft > 0 ? `days until your exam (${formatDate(state.examDate!)})` : 'exam date'}</span>
                <button className="btn small mt" onClick={() => setEditingDate(true)}>Change date</button>
              </>
            ) : (
              <>
                <label className="field" htmlFor="exam-date">Your exam date</label>
                <input
                  id="exam-date"
                  type="date"
                  min={today}
                  defaultValue={state.examDate ?? ''}
                  onChange={(e) => {
                    if (e.target.value) {
                      setExamDate(e.target.value);
                      setEditingDate(false);
                    }
                  }}
                />
                <span className="label mt">Set it to see a countdown. Check csca.cn for the official dates.</span>
              </>
            )}
          </div>
        </div>
        <div className="card">
          <div className="stat">
            <span className="value">{st} 🔥</span>
            <span className="label">day study streak</span>
            <span className="small muted mt">Total study time: {formatDuration(studied)}</span>
          </div>
        </div>
        <div className="card">
          <div className="stat">
            <span className="value">{due}</span>
            <span className="label">mistakes due for review</span>
            <Link className="btn small mt" to="/mistakes">Retry my mistakes</Link>
          </div>
        </div>
      </div>

      {(state.last || newUser) && (
        <div className="card spread">
          {state.last ? (
            <>
              <span>
                <strong>Continue where you left off:</strong> {state.last.label}
              </span>
              <Link className="btn primary" to={state.last.path}>Continue →</Link>
            </>
          ) : (
            <>
              <span>
                <strong>New here?</strong> Start with a short maths practice, or build a study plan for your exam date.
              </span>
              <span className="row">
                <Link className="btn primary" to="/practice?subject=math&start=1">Quick maths practice</Link>
                <Link className="btn" to="/plan">Make a study plan</Link>
              </span>
            </>
          )}
        </div>
      )}

      {plan && thisWeek && (
        <div className="card">
          <div className="spread">
            <h2 style={{ margin: 0 }}>This week: {thisWeek.title}</h2>
            <span className="small muted">
              Plan progress {pp!.done}/{pp!.total}
            </span>
          </div>
          <Bar value={pp!.done / Math.max(1, pp!.total)} />
          <ul>
            {nextTasks.map((t) => (
              <li key={t.id}>
                <Link to={t.link}>{t.label}</Link>
              </li>
            ))}
            {nextTasks.length === 0 && <li>All tasks for this week are done. 🎉</li>}
          </ul>
          <Link to="/plan">Open the full plan</Link>
        </div>
      )}

      <div className="card">
        <h2>Your progress</h2>
        <div className="grid grid-3">
          {progress.map((p) => {
            const s = getSubject(p.subject)!;
            return (
              <div key={p.subject} className="stack">
                <div className="spread">
                  <strong style={{ color: `var(--${p.subject})` }}>{s.name}</strong>
                  <span className="small muted">{p.attempts ? `${Math.round((100 * p.correct) / p.attempts)}% correct` : 'not started'}</span>
                </div>
                <div className="small muted">Mastery (recent accuracy across all topics)</div>
                <Bar value={p.mastery} />
                <div className="small muted">Topics practised (5+ questions): {Math.round(p.coverage * 100)}%</div>
                <Bar value={p.coverage} cls="good" />
                <div className="small">
                  Mock: {p.lastMock === null ? '—' : `latest ${p.lastMock}, best ${p.bestMock}`}
                </div>
              </div>
            );
          })}
        </div>
        <details className="mt">
          <summary>Progress by topic</summary>
          {SUBJECTS.map((s) => (
            <div key={s.id}>
              <h3>{s.name}</h3>
              <div className="table-wrap">
                <table>
                  <tbody>
                    {stats
                      .filter((x) => x.subject === s.id)
                      .map((x) => (
                        <tr key={x.subtopic}>
                          <td>
                            <Link to={`/learn/${x.subject}/${x.subtopic}`}>{x.name}</Link>
                          </td>
                          <td style={{ width: '35%' }}>
                            <Bar value={x.recent ?? 0} cls={x.recent === null ? '' : x.recent >= 0.7 ? 'good' : x.recent >= 0.5 ? 'warn' : 'bad'} />
                          </td>
                          <td className="small muted" style={{ whiteSpace: 'nowrap' }}>
                            {x.attempts ? `${Math.round((x.recent ?? 0) * 100)}% · ${x.attempts} Q` : '—'}
                          </td>
                        </tr>
                      ))}
                  </tbody>
                </table>
              </div>
            </div>
          ))}
        </details>
      </div>

      <div className="card">
        <h2>Weakest topics</h2>
        {weak.length === 0 ? (
          <p className="muted">Answer at least 3 questions in a topic to see your weak spots here.</p>
        ) : (
          <div className="topic-list">
            {weak.map((w) => (
              <div key={w.subject + w.subtopic} className="topic-item">
                <span>
                  <strong>{w.name}</strong> <span className="small muted">· {getSubject(w.subject)!.short} · {Math.round((w.recent ?? 0) * 100)}% recently</span>
                </span>
                <span className="row">
                  <Link className="btn small" to={`/learn/${w.subject}/${w.subtopic}`}>Notes</Link>
                  <Link className="btn small primary" to={`/practice?subject=${w.subject}&subtopics=${w.subtopic}&start=1`}>Practise</Link>
                </span>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="card">
        <h2>About the exam</h2>
        <p>
          The <strong>CSCA</strong> (China Scholastic Competency Assessment) is run by the China Scholarship Council for international students applying to undergraduate programmes in China.
        </p>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Paper</th>
                <th>Time</th>
                <th>Questions</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Mathematics, Physics, Chemistry (each)</td>
                <td>{EXAM.minutes} min</td>
                <td>{EXAM.questions} multiple choice, one correct answer</td>
                <td>0–100 · English or Chinese</td>
              </tr>
              <tr>
                <td>Professional Chinese (Humanities or STEM)</td>
                <td>90 min</td>
                <td>80 multiple choice</td>
                <td>see <Link to="/chinese">info page</Link></td>
              </tr>
            </tbody>
          </table>
        </div>
        <h3>Which subjects do I need?</h3>
        <p className="small muted">Typical requirements (example: Sichuan University). Always check your target university's own rules.</p>
        <div className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Programme</th>
                <th>Subjects</th>
              </tr>
            </thead>
            <tbody>
              {PROGRAM_TABLE.map(([p, s]) => (
                <tr key={p}>
                  <td>{p}</td>
                  <td>{s}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="small">
          Time strategy: about {EXAM.secondsPerQuestion} seconds per question. More on the <Link to="/resources">Resources</Link> page.
        </p>
      </div>
    </div>
  );
}
