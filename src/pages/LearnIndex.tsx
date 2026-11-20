import { Link } from 'react-router-dom';
import { SUBJECTS } from '../content/syllabus';
import { questionsFor } from '../content';
import { useAppState } from '../lib/store';

export function LearnIndex() {
  const state = useAppState();
  return (
    <div className="stack">
      <h1>Learn</h1>
      <p className="muted">
        One lesson for every bullet of the official 2025 CSCA syllabus: key ideas, every formula, worked examples and common traps. Each lesson ends with a button to practise that topic.
      </p>
      <p className="small">
        Also see the printable <Link to="/formulas">formula sheets</Link> and the <Link to="/chemistry-data">periodic table and chemistry data</Link>.
      </p>
      {SUBJECTS.map((s) => (
        <section key={s.id} className="card">
          <h2 style={{ marginTop: 0, color: `var(--${s.id})` }}>{s.name}</h2>
          {s.topics.map((t) => (
            <div key={t.id}>
              <h3>{t.name}</h3>
              <div className="topic-list">
                {t.subtopics.map((st) => {
                  const read = state.lessonsRead.includes(`${s.id}/${st.id}`);
                  return (
                    <Link key={st.id} to={`/learn/${s.id}/${st.id}`}>
                      <div className="topic-item">
                        <span>
                          <strong>{st.name}</strong>
                          <div className="small muted">{st.covers}</div>
                        </span>
                        <span className="row" style={{ flexWrap: 'nowrap' }}>
                          {read && <span className="chip good">read</span>}
                          <span className="chip">{questionsFor(s.id, [st.id]).length} Q</span>
                        </span>
                      </div>
                    </Link>
                  );
                })}
              </div>
            </div>
          ))}
        </section>
      ))}
    </div>
  );
}
