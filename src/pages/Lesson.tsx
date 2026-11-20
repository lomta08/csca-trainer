import { useEffect, useRef } from 'react';
import { Link, useParams } from 'react-router-dom';
import { allSubtopics, findSubtopic } from '../content/syllabus';
import { getNote, questionsFor } from '../content';
import { Md } from '../components/Md';
import { addStudyTime, markLessonRead, setLastLocation } from '../lib/store';

export function Lesson() {
  const { subject = '', subtopic = '' } = useParams();
  const ref = findSubtopic(subject, subtopic);
  const note = getNote(subject, subtopic);
  const opened = useRef(Date.now());

  useEffect(() => {
    if (!ref) return;
    opened.current = Date.now();
    setLastLocation({ path: `/learn/${subject}/${subtopic}`, label: `Lesson: ${ref.subtopic.name}` });
    const t = window.setTimeout(() => markLessonRead(`${subject}/${subtopic}`), 30000);
    const flush = () => {
      if (document.visibilityState === 'hidden') {
        addStudyTime(Date.now() - opened.current);
        opened.current = Date.now();
      } else opened.current = Date.now();
    };
    document.addEventListener('visibilitychange', flush);
    return () => {
      window.clearTimeout(t);
      document.removeEventListener('visibilitychange', flush);
      if (document.visibilityState === 'visible') addStudyTime(Date.now() - opened.current);
    };
  }, [subject, subtopic, ref]);

  if (!ref) {
    return (
      <div className="card">
        <h1>Lesson not found</h1>
        <Link to="/learn">All lessons</Link>
      </div>
    );
  }
  const list = allSubtopics(ref.subject.id);
  const idx = list.findIndex((r) => r.subtopic.id === subtopic);
  const prev = list[idx - 1];
  const next = list[idx + 1];
  const count = questionsFor(ref.subject.id, [subtopic]).length;
  const practice = `/practice?subject=${ref.subject.id}&subtopics=${subtopic}&start=1`;

  return (
    <article className="lesson stack">
      <nav className="small muted" aria-label="Breadcrumb">
        <Link to="/learn">Learn</Link> › {ref.subject.name} › {ref.topic.name}
      </nav>
      <h1>{ref.subtopic.name}</h1>
      <p className="muted" style={{ marginTop: -8 }}>Syllabus: {ref.subtopic.covers}.</p>
      <div className="card">{note ? <Md>{note}</Md> : <p>Notes for this topic are coming soon.</p>}</div>
      <div className="card spread">
        <span>
          <strong>Ready?</strong> {count} questions on this topic{ref.subject.id === 'math' ? ' plus generated ones' : ''}.
        </span>
        <Link className="btn primary" to={practice}>Practice this topic →</Link>
      </div>
      <div className="spread">
        {prev ? <Link className="btn small" to={`/learn/${prev.subject.id}/${prev.subtopic.id}`}>← {prev.subtopic.name}</Link> : <span />}
        {next ? <Link className="btn small" to={`/learn/${next.subject.id}/${next.subtopic.id}`}>{next.subtopic.name} →</Link> : <span />}
      </div>
    </article>
  );
}
