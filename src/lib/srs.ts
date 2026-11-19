import type { MistakeEntry, Question } from './types';
import { toDateKey } from './dates';

/** Number of distinct days a question must be answered correctly before it leaves the notebook. */
export const REQUIRED_CORRECT_DAYS = 2;

type Mistakes = Record<string, MistakeEntry>;

/**
 * Apply one answer to the mistakes notebook (pure; returns a new object).
 * - wrong answer → add / update the entry and reset its correct-day count
 * - correct answer on a question in the notebook → record the day; remove after 2 distinct days
 */
export function applyAnswer(mistakes: Mistakes, q: Pick<Question, 'id' | 'subject' | 'subtopic'>, correct: boolean, now: number = Date.now()): Mistakes {
  const existing = mistakes[q.id];
  if (!correct) {
    const entry: MistakeEntry = existing
      ? { ...existing, lastWrongTs: now, wrongCount: existing.wrongCount + 1, correctDays: [] }
      : { qid: q.id, subject: q.subject, subtopic: q.subtopic, addedTs: now, lastWrongTs: now, wrongCount: 1, correctDays: [] };
    return { ...mistakes, [q.id]: entry };
  }
  if (!existing) return mistakes;
  const day = toDateKey(now);
  const days = existing.correctDays.includes(day) ? existing.correctDays : [...existing.correctDays, day];
  if (days.length >= REQUIRED_CORRECT_DAYS) {
    const next = { ...mistakes };
    delete next[q.id];
    return next;
  }
  return { ...mistakes, [q.id]: { ...existing, correctDays: days } };
}

/** A mistake is due unless it was already answered correctly today. */
export function isDue(entry: MistakeEntry, now: number = Date.now()): boolean {
  return !entry.correctDays.includes(toDateKey(now));
}

/** Due mistakes first (oldest wrong answer first), then the rest. */
export function orderForReview(mistakes: Mistakes, now: number = Date.now()): MistakeEntry[] {
  const all = Object.values(mistakes);
  const due = all.filter((m) => isDue(m, now)).sort((a, b) => a.lastWrongTs - b.lastWrongTs);
  const notDue = all.filter((m) => !isDue(m, now)).sort((a, b) => a.lastWrongTs - b.lastWrongTs);
  return [...due, ...notDue];
}

export function progressLabel(entry: MistakeEntry): string {
  const n = entry.correctDays.length;
  return `${n}/${REQUIRED_CORRECT_DAYS} days correct`;
}
