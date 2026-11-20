import { Link, useParams } from 'react-router-dom';
import { SUBJECTS, getSubject } from '../content/syllabus';
import { getFormulaSheet } from '../content';
import { Md } from '../components/Md';

export function Formulas() {
  const { subject = 'math' } = useParams();
  const subj = getSubject(subject) ?? SUBJECTS[0];
  const sheet = getFormulaSheet(subj.id);
  return (
    <div className="stack sheet">
      <div className="tabs no-print">
        {SUBJECTS.map((s) => (
          <Link key={s.id} to={`/formulas/${s.id}`} className={`tab ${s.id === subj.id ? 'active' : ''}`}>
            {s.name}
          </Link>
        ))}
        <button className="btn small" onClick={() => window.print()} style={{ marginLeft: 'auto' }}>
          🖨 Print / save as PDF
        </button>
      </div>
      <div className="card">
        <h1>CSCA {subj.name} — formula sheet</h1>
        {sheet ? <Md>{sheet}</Md> : <p>Coming soon.</p>}
      </div>
      <p className="small muted no-print">Tip: printing uses a compact one-page layout (A4). In the print dialog choose “Save as PDF” to keep a copy on your phone.</p>
    </div>
  );
}
