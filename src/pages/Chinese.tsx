import { Link } from 'react-router-dom';

export function Chinese() {
  return (
    <div className="stack">
      <h1>Professional Chinese</h1>
      <div className="card stack">
        <p>
          Applicants to <strong>Chinese-taught</strong> programmes also take a Professional Chinese paper, in one of two versions: <strong>Humanities Chinese</strong> (for liberal
          arts, economics, management, etc.) or <strong>STEM Chinese</strong> (for science, engineering and medicine).
        </p>
        <ul>
          <li>Format: 90 minutes, 80 multiple-choice questions.</li>
          <li>It tests the Chinese needed to study the subject at university: vocabulary, reading academic texts, and subject-specific language.</li>
          <li>Students on English-taught programmes usually do not need it — check your university's requirements.</li>
        </ul>
        <p className="muted small">This site does not include Professional Chinese practice. Use the official materials:</p>
        <ul>
          <li>
            <a href="https://www.csca.cn/testprep/examsv" target="_blank" rel="noopener noreferrer">Official syllabus and simulation tests (csca.cn)</a>
          </li>
          <li>
            <a href="https://www.csca.cn" target="_blank" rel="noopener noreferrer">CSCA official website</a>
          </li>
          <li>
            <a href="https://www.chinesetest.cn" target="_blank" rel="noopener noreferrer">Chinese Testing International (HSK)</a> — general Chinese proficiency, often required alongside.
          </li>
        </ul>
        <p>
          <Link to="/resources">← Back to Resources</Link>
        </p>
      </div>
    </div>
  );
}
