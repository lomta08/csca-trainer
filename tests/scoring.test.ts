import { describe, expect, it } from 'vitest';
import { scoreMock, breakdownBySubtopic, scoreBand } from '../src/lib/scoring';
import type { Question } from '../src/lib/types';

const q = (id: string, answer: number, subtopic = 'sets'): Question => ({
  id, subject: 'math', topic: 'sets-inequalities', subtopic, difficulty: 1,
  question: 'q', options: ['a', 'b', 'c', 'd'], answer, explanation: 'e', tags: [],
});

describe('scoreMock', () => {
  it('scales to 0–100 and counts unanswered as wrong', () => {
    const qs = Array.from({ length: 48 }, (_, i) => q(`q${i}`, i % 4));
    const all = qs.map((x) => x.answer);
    expect(scoreMock(qs, all)).toEqual({ correct: 48, total: 48, score: 100 });
    expect(scoreMock(qs, qs.map(() => null)).score).toBe(0);
    const half = qs.map((x, i) => (i < 24 ? x.answer : null));
    expect(scoreMock(qs, half)).toEqual({ correct: 24, total: 48, score: 50 });
    const wrong = qs.map((x, i) => (i < 36 ? x.answer : (x.answer + 1) % 4));
    expect(scoreMock(qs, wrong).score).toBe(75);
  });
  it('rounds to the nearest integer', () => {
    const qs = Array.from({ length: 48 }, (_, i) => q(`q${i}`, 0));
    expect(scoreMock(qs, qs.map((_, i) => (i < 1 ? 0 : 1))).score).toBe(2); // 2.08
    expect(scoreMock(qs, qs.map((_, i) => (i < 47 ? 0 : 1))).score).toBe(98); // 97.9
  });
  it('handles an empty exam', () => {
    expect(scoreMock([], []).score).toBe(0);
  });
});

describe('breakdownBySubtopic', () => {
  it('groups by subtopic with time', () => {
    const qs = [q('a', 0, 'sets'), q('b', 1, 'sets'), q('c', 2, 'vectors')];
    const rows = breakdownBySubtopic(qs, [0, 0, 2], [1000, 2000, 3000]);
    const sets = rows.find((r) => r.subtopic === 'sets')!;
    expect(sets).toMatchObject({ correct: 1, total: 2, timeMs: 3000 });
    expect(rows.find((r) => r.subtopic === 'vectors')).toMatchObject({ correct: 1, total: 1 });
  });
  it('bands', () => {
    expect(scoreBand(90)).toBe('Excellent');
    expect(scoreBand(40)).toBe('Needs work');
  });
});
