import { Rng } from '../rng';
import type { Difficulty, Question } from '../types';

/** What a generator definition returns for one seed. */
export interface GenResult {
  question: string;
  /** correct option (LaTeX-capable Markdown) */
  correct: string;
  /** wrong options from typical mistakes; duplicates are removed automatically */
  distractors: string[];
  explanation: string;
  difficulty: Difficulty;
  /** parameters + the computed answer, used by unit tests to recheck the answer independently */
  meta: Record<string, unknown>;
}

export interface GeneratorDef {
  id: string;
  name: string;
  topic: string;
  subtopic: string;
  tags?: string[];
  make: (r: Rng) => GenResult;
  /** extra plausible wrong answers used only if the mistake-based ones collide */
  fallback?: (r: Rng, res: GenResult) => string[];
}

export interface Generated extends Question {
  meta: Record<string, unknown>;
}

/**
 * Plausible near-miss values for a numeric answer (off-by-one, sign, doubling).
 * Only used when the mistake-based distractors collide with each other.
 */
export function numericNearMisses(correct: string): string[] {
  const s = correct.trim();
  let mm = /^\$(-?\d+(?:\.\d+)?)\$$/.exec(s);
  if (mm) {
    const v = Number(mm[1]);
    const dec = (mm[1].split('.')[1] ?? '').length;
    const f = (x: number) => `$${Number(x.toFixed(dec))}$`;
    const step = dec ? 10 ** -dec * 5 : 1;
    return [f(v + step), f(v - step), f(-v), f(2 * v), f(v + 2 * step), f(v - 2 * step), f(v + 3 * step)];
  }
  mm = /^\$(-?)\\frac\{(\d+)\}\{(\d+)\}\$$/.exec(s);
  if (mm) {
    const sign = mm[1];
    const n = Number(mm[2]);
    const d = Number(mm[3]);
    const fr = (a: number, b: number, sg = sign) => {
      if (a === 0) return '$0$';
      if (a % b === 0) return `$${sg}${a / b}$`;
      return `$${sg}\\frac{${a}}{${b}}$`;
    };
    return [fr(n, d, sign ? '' : '-'), fr(d, n), fr(n + 1, d), fr(n, d + 1), fr(n + 2, d + 1)];
  }
  mm = /^\$(-?)(\d*)\\sqrt\{(\d+)\}\$$/.exec(s);
  if (mm) {
    const k = mm[2] ? Number(mm[2]) : 1;
    const root = mm[3];
    const t = (c: number) => `$${mm![1]}${c === 1 ? '' : c}\\sqrt{${root}}$`;
    return [t(k + 1), t(2 * k), `$${mm[1] ? '' : '-'}${k === 1 ? '' : k}\\sqrt{${root}}$`, k > 1 ? t(k - 1) : t(3)];
  }
  return [];
}

/** Build a full Question from a generator and a seed (deterministic). */
export function runGenerator(def: GeneratorDef, seed: number): Generated {
  const r = new Rng(seed);
  const res = def.make(r);
  const seen = new Set<string>([res.correct]);
  const wrong: string[] = [];
  const pool = [...res.distractors];
  if (def.fallback) pool.push(...def.fallback(r, res));
  pool.push(...numericNearMisses(res.correct));
  for (const d of pool) {
    if (wrong.length === 3) break;
    if (!seen.has(d)) {
      seen.add(d);
      wrong.push(d);
    }
  }
  let k = 1;
  if (wrong.length < 3) res.meta.usedFiller = true;
  while (wrong.length < 3) {
    // last resort: numbered "none of these"-free filler never needed in tests, but keep it safe
    const filler = `$${k * 97}$`;
    if (!seen.has(filler)) {
      seen.add(filler);
      wrong.push(filler);
    }
    k++;
  }
  const pos = r.int(0, 3);
  const options = [...wrong];
  options.splice(pos, 0, res.correct);
  return {
    id: `gen:${def.id}:${seed}`,
    subject: 'math',
    topic: def.topic,
    subtopic: def.subtopic,
    difficulty: res.difficulty,
    question: res.question,
    options: options as [string, string, string, string],
    answer: pos,
    explanation: res.explanation,
    tags: ['generated', def.id, ...(def.tags ?? [])],
    generated: true,
    meta: res.meta,
  };
}
