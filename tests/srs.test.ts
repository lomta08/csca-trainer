import { describe, expect, it } from 'vitest';
import { applyAnswer, isDue, orderForReview, REQUIRED_CORRECT_DAYS } from '../src/lib/srs';

const q = { id: 'm-x-1', subject: 'math' as const, subtopic: 'sets' };
const day = (d: number, h = 10) => new Date(2026, 10, d, h).getTime();

describe('spaced repetition mistakes notebook', () => {
  it('adds a question on a wrong answer', () => {
    const m = applyAnswer({}, q, false, day(1));
    expect(m[q.id]).toMatchObject({ wrongCount: 1, correctDays: [] });
  });

  it('ignores correct answers for questions not in the notebook', () => {
    expect(applyAnswer({}, q, true, day(1))).toEqual({});
  });

  it('needs correct answers on 2 different days to leave the notebook', () => {
    expect(REQUIRED_CORRECT_DAYS).toBe(2);
    let m = applyAnswer({}, q, false, day(1));
    m = applyAnswer(m, q, true, day(2, 9));
    m = applyAnswer(m, q, true, day(2, 18)); // same day again — does not count twice
    expect(m[q.id].correctDays).toEqual(['2026-11-02']);
    m = applyAnswer(m, q, true, day(3));
    expect(m[q.id]).toBeUndefined();
  });

  it('a new wrong answer resets progress', () => {
    let m = applyAnswer({}, q, false, day(1));
    m = applyAnswer(m, q, true, day(2));
    m = applyAnswer(m, q, false, day(3));
    expect(m[q.id]).toMatchObject({ wrongCount: 2, correctDays: [] });
    m = applyAnswer(m, q, true, day(4));
    expect(m[q.id]).toBeDefined();
    m = applyAnswer(m, q, true, day(5));
    expect(m[q.id]).toBeUndefined();
  });

  it('is not due again on the day it was answered correctly', () => {
    let m = applyAnswer({}, q, false, day(1));
    expect(isDue(m[q.id], day(1))).toBe(true);
    m = applyAnswer(m, q, true, day(2));
    expect(isDue(m[q.id], day(2, 20))).toBe(false);
    expect(isDue(m[q.id], day(3))).toBe(true);
  });

  it('orders due items first, oldest mistake first', () => {
    const q2 = { ...q, id: 'm-x-2' };
    const q3 = { ...q, id: 'm-x-3' };
    let m = applyAnswer({}, q, false, day(1));
    m = applyAnswer(m, q2, false, day(2));
    m = applyAnswer(m, q3, false, day(3));
    m = applyAnswer(m, q, true, day(4));
    expect(orderForReview(m, day(4, 15)).map((e) => e.qid)).toEqual(['m-x-2', 'm-x-3', 'm-x-1']);
  });

  it('does not mutate the input', () => {
    const m0 = applyAnswer({}, q, false, day(1));
    const copy = JSON.parse(JSON.stringify(m0));
    applyAnswer(m0, q, true, day(2));
    expect(m0).toEqual(copy);
  });
});
