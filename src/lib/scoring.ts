import type { Question } from './types';

/** CSCA fundamental subjects are scored 0–100; we scale the raw count of correct answers. */
export function scoreMock(questions: Question[], answers: (number | null)[]): { correct: number; total: number; score: number } {
  const total = questions.length;
  let correct = 0;
  questions.forEach((q, i) => {
    if (answers[i] !== null && answers[i] === q.answer) correct++;
  });
  const score = total === 0 ? 0 : Math.round((100 * correct) / total);
  return { correct, total, score };
}

export interface TopicBreakdown {
  key: string;
  subtopic: string;
  topic: string;
  correct: number;
  total: number;
  timeMs: number;
}

export function breakdownBySubtopic(questions: Question[], answers: (number | null)[], timePerQ: number[] = []): TopicBreakdown[] {
  const map = new Map<string, TopicBreakdown>();
  questions.forEach((q, i) => {
    const key = q.subtopic;
    const row = map.get(key) ?? { key, subtopic: q.subtopic, topic: q.topic, correct: 0, total: 0, timeMs: 0 };
    row.total++;
    if (answers[i] === q.answer) row.correct++;
    row.timeMs += timePerQ[i] ?? 0;
    map.set(key, row);
  });
  return [...map.values()];
}

/** Rough grade band to help interpret a 0–100 score. */
export function scoreBand(score: number): string {
  if (score >= 85) return 'Excellent';
  if (score >= 70) return 'Good';
  if (score >= 55) return 'Pass level';
  return 'Needs work';
}
