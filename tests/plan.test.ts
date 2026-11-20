import { describe, expect, it } from 'vitest';
import { generatePlan, planProgress, currentWeekIndex } from '../src/lib/plan';
import { allSubtopics } from '../src/content/syllabus';

const base = { startDate: '2026-11-20', hoursPerWeek: 10 };

describe('study plan generator', () => {
  it('covers every syllabus subtopic of the chosen subjects exactly once (lesson + practice)', () => {
    const plan = generatePlan({ ...base, examDate: '2027-03-01', subjects: ['math', 'physics', 'chemistry'] });
    const items = plan.weeks.flatMap((w) => w.items);
    for (const ref of allSubtopics()) {
      expect(items.filter((i) => i.kind === 'learn' && i.subject === ref.subject.id && i.subtopic === ref.subtopic.id)).toHaveLength(1);
      expect(items.filter((i) => i.kind === 'practice' && i.subject === ref.subject.id && i.subtopic === ref.subtopic.id)).toHaveLength(1);
    }
  });

  it('only includes the chosen subjects', () => {
    const plan = generatePlan({ ...base, examDate: '2027-02-01', subjects: ['math'] });
    const items = plan.weeks.flatMap((w) => w.items);
    expect(items.every((i) => !i.subject || i.subject === 'math')).toBe(true);
    expect(items.filter((i) => i.kind === 'learn')).toHaveLength(allSubtopics('math').length);
  });

  it('puts the mock exams in the final weeks and no lessons there', () => {
    const plan = generatePlan({ ...base, examDate: '2027-03-01', subjects: ['math', 'physics'] });
    const n = plan.weeks.length;
    expect(n).toBe(15);
    const mockWeeks = plan.weeks.filter((w) => w.items.some((i) => i.kind === 'mock'));
    expect(mockWeeks.map((w) => w.index)).toEqual([n - 2, n - 1, n]);
    for (const w of mockWeeks) expect(w.items.some((i) => i.kind === 'learn')).toBe(false);
    // three fixed mocks per subject are scheduled
    const mocks = plan.weeks.flatMap((w) => w.items).filter((i) => i.kind === 'mock' && i.subject === 'math');
    expect(mocks.length).toBeGreaterThanOrEqual(3);
  });

  it('works with a very short time to the exam', () => {
    const plan = generatePlan({ ...base, examDate: '2026-11-25', subjects: ['math'] });
    expect(plan.weeks).toHaveLength(1);
    const items = plan.weeks[0].items;
    expect(items.some((i) => i.kind === 'mock')).toBe(true);
    expect(items.filter((i) => i.kind === 'learn')).toHaveLength(allSubtopics('math').length);
    expect(plan.warning).toMatch(/hours per week/);
    expect(new Set(items.map((i) => i.id)).size).toBe(items.length);
  });

  it('item ids are unique and weeks are contiguous', () => {
    const plan = generatePlan({ ...base, examDate: '2027-06-01', subjects: ['math', 'physics', 'chemistry'] });
    const ids = plan.weeks.flatMap((w) => w.items.map((i) => i.id));
    expect(new Set(ids).size).toBe(ids.length);
    expect(plan.weeks[0].start).toBe('2026-11-20');
    expect(plan.weeks[plan.weeks.length - 1].end).toBe('2027-06-01');
    plan.weeks.forEach((w, i) => expect(w.index).toBe(i + 1));
    expect(plan.weeks.every((w) => w.items.length > 0)).toBe(true);
  });

  it('balances the study load across study weeks', () => {
    const plan = generatePlan({ ...base, examDate: '2027-03-01', subjects: ['math', 'physics', 'chemistry'] });
    const studyWeeks = plan.weeks.filter((w) => !w.items.some((i) => i.kind === 'mock'));
    const loads = studyWeeks.map((w) => w.items.reduce((s, i) => s + i.hours, 0));
    expect(Math.max(...loads) - Math.min(...loads)).toBeLessThan(6);
  });

  it('warns only when the hours are not enough', () => {
    expect(generatePlan({ ...base, hoursPerWeek: 20, examDate: '2027-06-01', subjects: ['math'] }).warning).toBeUndefined();
    expect(generatePlan({ ...base, hoursPerWeek: 1, examDate: '2026-12-10', subjects: ['math', 'physics', 'chemistry'] }).warning).toBeDefined();
  });

  it('rejects an exam date in the past or no subjects', () => {
    expect(() => generatePlan({ ...base, examDate: '2026-11-01', subjects: ['math'] })).toThrow();
    expect(() => generatePlan({ ...base, examDate: '2027-01-01', subjects: [] })).toThrow();
  });

  it('tracks progress and the current week', () => {
    const plan = generatePlan({ ...base, examDate: '2027-01-20', subjects: ['math'] });
    plan.weeks[0].items[0].done = true;
    expect(planProgress(plan).done).toBe(1);
    expect(currentWeekIndex(plan, '2026-11-28')).toBe(1);
    expect(currentWeekIndex(plan, '2020-01-01')).toBe(0);
    expect(currentWeekIndex(plan, '2030-01-01')).toBe(plan.weeks.length - 1);
  });
});
