import { describe, expect, it } from 'vitest';
import { selectMockQuestions } from '../src/lib/mock';
import { QUESTIONS, FIXED_MOCKS } from '../src/content';
import { SUBJECTS } from '../src/content/syllabus';

describe('mock exam assembly', () => {
  for (const s of SUBJECTS) {
    const bank = QUESTIONS.filter((q) => q.subject === s.id);
    if (bank.length < 48) continue;
    it(`${s.id}: 48 distinct questions with the syllabus topic weights`, () => {
      for (const seed of [1, 2, 3, 99]) {
        const qs = selectMockQuestions(QUESTIONS, s.id, seed);
        expect(qs).toHaveLength(48);
        expect(new Set(qs.map((q) => q.id)).size).toBe(48);
        for (const t of s.topics) expect(qs.filter((q) => q.topic === t.id)).toHaveLength(t.mockCount);
        expect(qs.every((q) => q.subject === s.id)).toBe(true);
        const hard = qs.filter((q) => q.difficulty === 3).length;
        expect(hard).toBeGreaterThan(4);
        expect(hard).toBeLessThan(16);
      }
    });
    it(`${s.id}: three fixed mocks, disjoint, all ids exist`, () => {
      const mocks = FIXED_MOCKS[s.id];
      expect(mocks.length).toBeGreaterThanOrEqual(3);
      const seen = new Set<string>();
      for (const mk of mocks) {
        expect(mk.qids).toHaveLength(48);
        for (const id of mk.qids) {
          expect(QUESTIONS.find((q) => q.id === id)?.subject).toBe(s.id);
          expect(seen.has(id)).toBe(false);
          seen.add(id);
        }
      }
    });
  }
});
