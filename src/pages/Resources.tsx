import { Link } from 'react-router-dom';
import { EXAM } from '../content/syllabus';

const OFFICIAL = [
  { href: 'https://www.csca.cn', label: 'CSCA official website (csca.cn)', note: 'Registration, exam dates, test centres and official notices.' },
  { href: 'https://www.csca.cn/testprep/examsv', label: 'Official syllabi and simulation tests', note: 'Download the 2025 syllabus for each subject and try the official simulation papers.' },
  { href: 'https://www.campuschina.org', label: 'Study in China (Campus China, China Scholarship Council)', note: 'Scholarships, universities and application information run by CSC.' },
];

export function Resources() {
  return (
    <div className="stack">
      <h1>Resources</h1>

      <div className="card">
        <h2 style={{ marginTop: 0 }}>Official links</h2>
        <ul>
          {OFFICIAL.map((l) => (
            <li key={l.href}>
              <a href={l.href} target="_blank" rel="noopener noreferrer">
                {l.label}
              </a>{' '}
              — <span className="muted">{l.note}</span>
            </li>
          ))}
        </ul>
        <p className="small muted">
          Exam dates, fees and the subjects each university requires can change. Always confirm them on csca.cn and on your target university's admissions page. This site is an
          independent practice tool and is not affiliated with the China Scholarship Council.
        </p>
      </div>

      <div className="card">
        <h2 style={{ marginTop: 0 }}>Choosing your subjects</h2>
        <p>Everyone takes Mathematics. What else you need depends on the programme (example rules from Sichuan University):</p>
        <ul>
          <li><strong>English-taught liberal arts, business, economics:</strong> Mathematics.</li>
          <li><strong>English-taught science and engineering:</strong> Mathematics + Physics.</li>
          <li><strong>English-taught medicine:</strong> Mathematics + Physics + Chemistry.</li>
          <li><strong>Chinese-taught programmes:</strong> add Professional Chinese (see the <Link to="/chinese">Chinese info page</Link>).</li>
        </ul>
        <p>If you are applying to several universities, prepare for the union of all their requirements. Mathematics, Physics and Chemistry can each be taken in English or Chinese.</p>
      </div>

      <div className="card">
        <h2 style={{ marginTop: 0 }}>Time strategy</h2>
        <ul>
          <li>
            {EXAM.questions} questions in {EXAM.minutes} minutes is about <strong>{EXAM.secondsPerQuestion} seconds per question</strong>. Check the clock at question 12 (≈15 min), 24 (≈30 min) and 36 (≈45 min).
          </li>
          <li>Do a fast first pass: answer what you can, <strong>flag</strong> anything taking more than about 2 minutes, and come back later.</li>
          <li>There is no evidence of negative marking, so <strong>never leave a question blank</strong> — eliminate options and guess.</li>
          <li>Keep 5 minutes at the end to revisit flagged questions and check that every question has an answer.</li>
          <li>Use the options: substitute simple values, check units and signs, estimate magnitudes, and rule out impossible answers (a negative variance, a probability above 1, an eccentricity below 1 for a hyperbola).</li>
        </ul>
      </div>

      <div className="card">
        <h2 style={{ marginTop: 0 }}>Exam-day tips</h2>
        <ul>
          <li>Read the official exam notice for ID requirements, allowed items and the check-in time; arrive early (or, for an online test, test your device, camera and connection the day before).</li>
          <li>Sleep well the night before — a tired brain makes careless algebra mistakes.</li>
          <li>Bring the permitted stationery and a watch if allowed. Do not expect to use a calculator: every question on this site is designed to be done by hand.</li>
          <li>Read each question twice: watch for "not", "must", "at least", units, and whether the answer is a <em>value</em> or a <em>point</em>.</li>
          <li>For physics, note the value of g given in the question. For chemistry, use the relative atomic masses given.</li>
          <li>If you panic, put the pen down, take three slow breaths, and move to a question you know.</li>
        </ul>
      </div>

      <div className="card">
        <h2 style={{ marginTop: 0 }}>How to use this site</h2>
        <ol>
          <li>Make a <Link to="/plan">study plan</Link> for your exam date.</li>
          <li>For each topic: read the <Link to="/learn">lesson</Link>, then practise 15–20 questions.</li>
          <li>Every day, clear the questions that are due in your <Link to="/mistakes">mistakes notebook</Link>.</li>
          <li>Use the <Link to="/drill">unlimited math drill</Link> to build speed on routine question types.</li>
          <li>In the last weeks, take the <Link to="/mock">mock exams</Link> under real timing and review every mistake.</li>
          <li>Send your progress code to your tutor from the <Link to="/tutor">Tutor</Link> page each week.</li>
        </ol>
      </div>
    </div>
  );
}
