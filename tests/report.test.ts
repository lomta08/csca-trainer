import { describe, expect, it } from 'vitest';
import { buildSummary, parseProgressCode, progressCode, reportText } from '../src/lib/report';
import { emptyState } from '../src/lib/store';
import type { AppState } from '../src/lib/types';

function sample(): AppState {
  const s = emptyState();
  s.name = 'Lin';
  s.examDate = '2027-03-01';
  const ts = new Date(2026, 10, 20, 10).getTime();
  for (let i = 0; i < 10; i++)
    s.attempts.push({ qid: `q${i}`, subject: 'math', topic: 'functions', subtopic: 'trigonometry', correct: i % 2 === 0, ts, timeMs: 60000, mode: 'practice' });
  s.studyLog['2026-11-20'] = 600000;
  s.mocks.push({ id: 'm1', subject: 'math', kind: 'fixed', title: 'Mathematics Mock 1', startedTs: ts, finishedTs: ts, durationMs: 3_000_000, qids: [], answers: [], timePerQ: [], flagged: [], correct: 30, total: 48, score: 63, autoSubmitted: false });
  return s;
}

describe('progress code and report', () => {
  it('round-trips through the code', () => {
    const s = sample();
    const code = progressCode(s);
    const parsed = parseProgressCode(`here it is: ${code} thanks`);
    expect(parsed).toEqual(JSON.parse(code));
    expect(parsed.topics).toEqual([['math', 'trigonometry', 10, 5, 50]]);
    expect(parsed.mocks[0][2]).toBe(63);
  });

  it('stays compact', () => {
    const s = sample();
    for (let i = 0; i < 3000; i++) s.attempts.push({ ...s.attempts[0], qid: `x${i}` });
    expect(progressCode(s).length).toBeLessThan(2000);
  });

  it('rejects junk', () => {
    expect(() => parseProgressCode('hello')).toThrow();
    expect(() => parseProgressCode('{"a":1}')).toThrow(/not a CSCA/);
    expect(() => parseProgressCode('{bad json}')).toThrow(/damaged/);
  });

  it('writes a readable plain-text report', () => {
    const txt = reportText(buildSummary(sample(), new Date(2026, 10, 20, 12).getTime()));
    expect(txt).toContain('Lin');
    expect(txt).toContain('Mathematics: 50% of 10 questions');
    expect(txt).toContain('latest 63/100');
    expect(txt).toContain('Trigonometric Functions (50%)');
    expect(txt).toContain('Streak: 1 day');
  });
});
