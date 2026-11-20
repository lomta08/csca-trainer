import { useEffect, useRef } from 'react';
import { Md } from './Md';
import type { Question } from '../lib/types';
import { LETTERS } from '../lib/questions';
import { subtopicName, getSubject } from '../content/syllabus';

const DIFF_LABEL = ['', 'Easy', 'Medium', 'Hard'];

export interface QuestionCardProps {
  question: Question;
  index?: number;
  total?: number;
  /** chosen option (null = not answered yet) */
  selected: number | null;
  /** practice: show correct/wrong + explanation once answered. exam: never reveal. review: always reveal. */
  mode: 'practice' | 'exam' | 'review';
  onSelect?: (choice: number) => void;
  onNext?: () => void;
  nextLabel?: string;
  flagged?: boolean;
  onToggleFlag?: () => void;
  /** show the Next button inside the card (Enter still works when false) */
  showNextButton?: boolean;
  /** register keyboard shortcuts (only one card on the page should) */
  keyboard?: boolean;
}

function isTyping(e: KeyboardEvent) {
  const t = e.target as HTMLElement | null;
  return !!t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable);
}

export function QuestionCard(p: QuestionCardProps) {
  const { question: q, selected, mode } = p;
  const revealed = mode === 'review' || (mode === 'practice' && selected !== null);
  const locked = mode === 'review' || (mode === 'practice' && selected !== null);
  const feedbackRef = useRef<HTMLDivElement>(null);
  const propsRef = useRef(p);
  propsRef.current = p;

  useEffect(() => {
    if (!p.keyboard) return;
    const onKey = (e: KeyboardEvent) => {
      if (isTyping(e) || e.ctrlKey || e.metaKey || e.altKey) return;
      const cur = propsRef.current;
      const k = e.key.toLowerCase();
      const idx = ['1', '2', '3', '4'].indexOf(k) >= 0 ? ['1', '2', '3', '4'].indexOf(k) : ['a', 'b', 'c', 'd'].indexOf(k);
      const isLocked = cur.mode === 'review' || (cur.mode === 'practice' && cur.selected !== null);
      if (idx >= 0 && !isLocked && cur.onSelect) {
        e.preventDefault();
        cur.onSelect(idx);
      } else if (e.key === 'Enter' && cur.onNext && (cur.selected !== null || cur.mode !== 'practice')) {
        // let Enter activate a focused button normally
        const t = e.target as HTMLElement | null;
        if (t?.tagName === 'BUTTON' && !t.classList.contains('option')) return;
        e.preventDefault();
        cur.onNext();
      } else if (k === 'f' && cur.onToggleFlag) {
        e.preventDefault();
        cur.onToggleFlag();
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [p.keyboard]);

  useEffect(() => {
    if (mode === 'practice' && selected !== null && feedbackRef.current) {
      feedbackRef.current.scrollIntoView?.({ behavior: 'smooth', block: 'nearest' });
    }
  }, [mode, selected]);

  const subj = getSubject(q.subject);
  const correct = selected !== null && selected === q.answer;

  return (
    <article className="qcard" aria-labelledby={`q-${q.id}`}>
      <div className="qmeta">
        {p.index !== undefined && p.total !== undefined && (
          <strong>
            Question {p.index + 1} of {p.total}
          </strong>
        )}
        <span className={`chip ${q.subject}`}>{subj?.short}</span>
        <span className="chip">{subtopicName(q.subject, q.subtopic)}</span>
        <span className="chip">{DIFF_LABEL[q.difficulty]}</span>
        {q.generated && <span className="chip">Generated</span>}
        {p.onToggleFlag && (
          <button type="button" className={`btn small ${p.flagged ? 'primary' : ''}`} style={{ marginLeft: 'auto' }} onClick={p.onToggleFlag} aria-pressed={!!p.flagged} title="Flag for review (F)">
            {p.flagged ? '⚑ Flagged' : '⚐ Flag'}
          </button>
        )}
      </div>
      <div className="qtext" id={`q-${q.id}`}>
        <Md>{q.question}</Md>
      </div>
      <div className="options" role="radiogroup" aria-label="Answer options">
        {q.options.map((opt, i) => {
          let cls = 'option';
          if (revealed) {
            if (i === q.answer) cls += ' correct';
            else if (i === selected) cls += ' wrong';
          } else if (i === selected) cls += ' selected';
          return (
            <button
              key={i}
              type="button"
              role="radio"
              aria-checked={selected === i}
              className={cls}
              disabled={locked}
              onClick={() => p.onSelect?.(i)}
              aria-label={`Option ${LETTERS[i]}`}
            >
              <span className="letter" aria-hidden="true">
                {LETTERS[i]}
              </span>
              <span className="otext">
                <Md inline>{opt}</Md>
              </span>
            </button>
          );
        })}
      </div>
      {revealed && (
        <div ref={feedbackRef}>
          {selected !== null ? (
            <div className={`feedback ${correct ? 'good' : 'bad'}`} role="status" aria-live="polite">
              <div className="verdict">{correct ? '✓ Correct' : `✗ Not quite — the answer is ${LETTERS[q.answer]}`}</div>
            </div>
          ) : (
            <div className="feedback bad" role="status">
              <div className="verdict">Not answered — the answer is {LETTERS[q.answer]}</div>
            </div>
          )}
          <div className="explanation">
            <strong>Solution</strong>
            <Md>{q.explanation}</Md>
          </div>
        </div>
      )}
      {(p.onNext || p.keyboard) && (
        <div className="qactions">
          <span className="kbd-hint">
            Keys: <kbd>1</kbd>–<kbd>4</kbd> or <kbd>A</kbd>–<kbd>D</kbd> to answer, <kbd>Enter</kbd> for next{p.onToggleFlag ? <>, <kbd>F</kbd> to flag</> : null}
          </span>
          {p.onNext && p.showNextButton !== false && (
            <button type="button" className="btn primary" onClick={p.onNext} disabled={mode === 'practice' && selected === null}>
              {p.nextLabel ?? 'Next →'}
            </button>
          )}
        </div>
      )}
    </article>
  );
}
