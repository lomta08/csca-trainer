import { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { QuestionCard } from './QuestionCard';
import { Md } from './Md';
import type { Mode, Question } from '../lib/types';
import { recordAnswer, toggleFlag, useAppState } from '../lib/store';
import { LETTERS } from '../lib/questions';
import { subtopicName } from '../content/syllabus';

interface Props {
  questions: Question[];
  mode: Mode;
  /** endless sessions: called when the list runs out */
  more?: () => Question[];
  onExit: () => void;
  onRestart?: (questions: Question[]) => void;
  title?: string;
}

interface Answered {
  q: Question;
  choice: number;
  correct: boolean;
}

export function PracticeSession({ questions: initial, mode, more, onExit, onRestart, title }: Props) {
  const [questions, setQuestions] = useState(initial);
  const [i, setI] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [answered, setAnswered] = useState<Answered[]>([]);
  const [done, setDone] = useState(false);
  const started = useRef(Date.now());
  const state = useAppState();

  useEffect(() => {
    started.current = Date.now();
  }, [i]);

  const q = questions[i];

  const select = (choice: number) => {
    if (selected !== null || !q) return;
    setSelected(choice);
    const correct = recordAnswer(q, choice, Date.now() - started.current, mode);
    setAnswered((a) => [...a, { q, choice, correct }]);
  };

  const next = () => {
    if (selected === null) return;
    if (i + 1 < questions.length) {
      setI(i + 1);
      setSelected(null);
    } else if (more) {
      const extra = more();
      setQuestions((qs) => [...qs, ...extra]);
      setI(i + 1);
      setSelected(null);
    } else setDone(true);
  };

  if (done || !q) {
    const correct = answered.filter((a) => a.correct).length;
    const wrong = answered.filter((a) => !a.correct).map((a) => a.q);
    const pct = answered.length ? Math.round((100 * correct) / answered.length) : 0;
    return (
      <div className="stack">
        <div className="card">
          <h2>Session complete</h2>
          <div className="grid grid-3">
            <div className="stat"><span className="value">{correct}/{answered.length}</span><span className="label">correct</span></div>
            <div className="stat"><span className="value">{pct}%</span><span className="label">accuracy</span></div>
            <div className="stat"><span className="value">{wrong.length}</span><span className="label">added to Mistakes</span></div>
          </div>
          <div className="row mt">
            {wrong.length > 0 && onRestart && (
              <button className="btn primary" onClick={() => onRestart(wrong)}>Retry the {wrong.length} I got wrong</button>
            )}
            <button className="btn" onClick={onExit}>New session</button>
            <Link className="btn" to="/mistakes">Mistakes notebook</Link>
          </div>
        </div>
        <div className="card">
          <h3>Review</h3>
          <div className="table-wrap">
            <table>
              <thead><tr><th>#</th><th>Question</th><th>Topic</th><th>You</th><th>Answer</th></tr></thead>
              <tbody>
                {answered.map((a, k) => (
                  <tr key={k}>
                    <td>{k + 1}</td>
                    <td style={{ minWidth: 220 }}><Md inline>{a.q.question.length > 140 ? a.q.question.slice(0, 140).replace(/\$[^$]*$/, '') + '…' : a.q.question}</Md></td>
                    <td className="small muted">{subtopicName(a.q.subject, a.q.subtopic)}</td>
                    <td><span className={`chip ${a.correct ? 'good' : 'bad'}`}>{LETTERS[a.choice]}</span></td>
                    <td>{LETTERS[a.q.answer]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }

  const correctSoFar = answered.filter((a) => a.correct).length;
  return (
    <div className="stack">
      <div className="spread">
        <div>
          {title && <strong>{title}</strong>}
          <div className="small muted">
            {answered.length} answered · {correctSoFar} correct{more ? ' · endless' : ''}
          </div>
        </div>
        <button className="btn small" onClick={() => (answered.length ? setDone(true) : onExit())}>
          {answered.length ? 'Finish' : 'Cancel'}
        </button>
      </div>
      {!more && (
        <div className="progress" aria-hidden="true">
          <span style={{ width: `${(100 * (i + (selected !== null ? 1 : 0))) / questions.length}%` }} />
        </div>
      )}
      <QuestionCard
        key={q.id + i}
        question={q}
        index={more ? undefined : i}
        total={more ? undefined : questions.length}
        selected={selected}
        mode="practice"
        onSelect={select}
        onNext={next}
        nextLabel={i + 1 < questions.length || more ? 'Next →' : 'See results'}
        flagged={state.flags.includes(q.id)}
        onToggleFlag={() => toggleFlag(q.id)}
        keyboard
      />
    </div>
  );
}
