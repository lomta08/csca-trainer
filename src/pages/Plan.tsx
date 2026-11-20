import { useState } from 'react';
import { Link } from 'react-router-dom';
import { SUBJECTS, type SubjectId } from '../content/syllabus';
import { generatePlan, planProgress, currentWeekIndex } from '../lib/plan';
import { setExamDate, setPlan, togglePlanItem, useAppState } from '../lib/store';
import { addDays, formatDate, toDateKey } from '../lib/dates';

export function Plan() {
  const state = useAppState();
  const plan = state.plan;
  const [editing, setEditing] = useState(!plan);
  const [examDate, setDate] = useState(state.examDate ?? plan?.examDate ?? addDays(toDateKey(), 90));
  const [subjects, setSubjects] = useState<SubjectId[]>(plan?.subjects ?? ['math', 'physics']);
  const [hours, setHours] = useState(plan?.hoursPerWeek ?? 8);
  const [error, setError] = useState<string | null>(null);

  const make = () => {
    try {
      if (plan && !window.confirm('Replace your current plan? Ticked items will be lost.')) return;
      const p = generatePlan({ examDate, subjects, hoursPerWeek: hours });
      setPlan(p);
      setExamDate(examDate);
      setError(null);
      setEditing(false);
    } catch (e) {
      setError((e as Error).message);
    }
  };

  const toggleSubject = (s: SubjectId) => setSubjects((cur) => (cur.includes(s) ? cur.filter((x) => x !== s) : [...cur, s]));

  return (
    <div className="stack">
      <h1>Study plan</h1>
      <p className="muted">A week-by-week plan that covers every syllabus topic of your subjects, with mock exams in the final weeks. Tick tasks off as you go.</p>

      {editing ? (
        <div className="card">
          <h2>Build your plan</h2>
          <div className="grid grid-3">
            <div>
              <label className="field" htmlFor="plan-date">Exam date</label>
              <input id="plan-date" type="date" min={addDays(toDateKey(), 1)} value={examDate} onChange={(e) => setDate(e.target.value)} />
            </div>
            <div>
              <label className="field" htmlFor="plan-hours">Hours per week</label>
              <input id="plan-hours" type="number" min={1} max={60} value={hours} onChange={(e) => setHours(Number(e.target.value) || 1)} />
            </div>
            <fieldset style={{ border: 'none', padding: 0, margin: 0 }}>
              <legend className="field">Subjects</legend>
              {SUBJECTS.map((s) => (
                <label key={s.id} className="check-row" style={{ padding: '2px 0' }}>
                  <input type="checkbox" checked={subjects.includes(s.id)} onChange={() => toggleSubject(s.id)} /> {s.name}
                </label>
              ))}
            </fieldset>
          </div>
          <p className="small muted">Not sure which subjects you need? See the table on the <Link to="/">dashboard</Link> or the <Link to="/resources">Resources</Link> page.</p>
          {error && <div className="notice bad">{error}</div>}
          <div className="row mt">
            <button className="btn primary" onClick={make}>Generate plan</button>
            {plan && <button className="btn" onClick={() => setEditing(false)}>Cancel</button>}
          </div>
        </div>
      ) : (
        plan && <PlanView onEdit={() => setEditing(true)} />
      )}
    </div>
  );
}

function PlanView({ onEdit }: { onEdit: () => void }) {
  const { plan } = useAppState();
  if (!plan) return null;
  const pp = planProgress(plan);
  const cur = currentWeekIndex(plan);
  return (
    <>
      <div className="card">
        <div className="spread">
          <div>
            <strong>
              {plan.weeks.length} weeks until {formatDate(plan.examDate)}
            </strong>
            <div className="small muted">
              {plan.subjects.map((s) => SUBJECTS.find((x) => x.id === s)!.name).join(', ')} · {plan.hoursPerWeek} h/week · {pp.done}/{pp.total} tasks done
            </div>
          </div>
          <span className="row no-print">
            <button className="btn small" onClick={() => window.print()}>Print</button>
            <button className="btn small" onClick={onEdit}>Change plan</button>
          </span>
        </div>
        <div className="progress mt" aria-hidden="true">
          <span style={{ width: `${(100 * pp.done) / Math.max(1, pp.total)}%` }} />
        </div>
        {plan.warning && <div className="notice warn mt">{plan.warning}</div>}
      </div>
      {plan.weeks.map((w, i) => {
        const done = w.items.filter((x) => x.done).length;
        const hours = w.items.reduce((s, x) => s + x.hours, 0);
        return (
          <details key={w.index} className="card" open={i === cur || (i === cur + 1 && done === 0 && cur === 0)} style={i === cur ? { borderColor: 'var(--primary)', borderWidth: 2 } : undefined}>
            <summary style={{ cursor: 'pointer' }}>
              <strong>
                Week {w.index}
                {i === cur ? ' (this week)' : ''}: {w.title}
              </strong>{' '}
              <span className="small muted">
                {formatDate(w.start)} – {formatDate(w.end)} · {done}/{w.items.length} done · ≈{Math.round(hours)} h
              </span>
            </summary>
            <div className="mt">
              {w.items.map((it) => (
                <div key={it.id} className="check-row">
                  <input type="checkbox" id={it.id} checked={it.done} onChange={() => togglePlanItem(it.id)} />
                  <label htmlFor={it.id} style={{ flex: 1, textDecoration: it.done ? 'line-through' : undefined, color: it.done ? 'var(--muted)' : undefined }}>
                    {it.label} <span className="small muted">({it.hours} h)</span>
                  </label>
                  <Link className="btn small no-print" to={it.link}>Go</Link>
                </div>
              ))}
            </div>
          </details>
        );
      })}
    </>
  );
}
