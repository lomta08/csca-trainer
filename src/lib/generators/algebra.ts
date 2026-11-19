import type { GeneratorDef } from './core';
import { Frac, intervalTex, iv, intersect, union, complement, polyTex, xMinus, m, type Interval } from './format';
import type { Rng } from '../rng';

type Op = '<' | '>' | '\\le' | '\\ge';
const OPS: Op[] = ['<', '>', '\\le', '\\ge'];

function distinctRoots(r: Rng, lo = -6, hi = 7): [number, number] {
  const a = r.int(lo, hi);
  let b = r.int(lo, hi);
  while (b === a) b = r.int(lo, hi);
  return a < b ? [a, b] : [b, a];
}

/** Solution of k(x-r1)(x-r2) op 0 with r1<r2. */
export function quadSolution(k: number, r1: number, r2: number, op: Op): Interval[] {
  const closed = op === '\\le' || op === '\\ge';
  // positive outside the roots when k>0
  const wantPositive = op === '>' || op === '\\ge';
  const outside = (k > 0) === wantPositive;
  return outside ? [iv(-Infinity, r1, false, closed), iv(r2, Infinity, closed, false)] : [iv(r1, r2, closed, closed)];
}


/** Near-miss interval answers: shift one finite endpoint by ±1. Used only when other distractors collide. */
function shiftedFallback(_r: Rng, res: { meta: Record<string, unknown> }): string[] {
  const sol = res.meta.solution as Interval[];
  const out: string[] = [];
  for (const delta of [1, -1, 2]) {
    out.push(m(intervalTex(sol.map((i) => ({ ...i, lo: isFinite(i.lo) ? i.lo - delta : i.lo })))));
    out.push(m(intervalTex(sol.map((i) => ({ ...i, hi: isFinite(i.hi) ? i.hi + delta : i.hi })))));
  }
  return out;
}

const quadraticInequality: GeneratorDef = {
  id: 'quadratic-inequality',
  name: 'Quadratic inequality',
  topic: 'sets-inequalities',
  subtopic: 'quadratic-inequalities',
  make(r) {
    const [r1, r2] = distinctRoots(r);
    const k = r.pick([1, 1, 1, -1, 2]);
    const op = r.pick(OPS);
    const coeffs = [k, -k * (r1 + r2), k * r1 * r2];
    const sol = quadSolution(k, r1, r2, op);
    const closed = op === '\\le' || op === '\\ge';
    const opposite = sol.length === 1 ? [iv(-Infinity, r1, false, closed), iv(r2, Infinity, closed, false)] : [iv(r1, r2, closed, closed)];
    const signFlip = quadSolution(k, -r2, -r1, op); // roots with the wrong sign
    const wrongBrackets = sol.map((i) => ({ ...i, loC: isFinite(i.lo) && !i.loC, hiC: isFinite(i.hi) && !i.hiC }));
    const correct = m(intervalTex(sol));
    const factored = `${k === 1 ? '' : k === -1 ? '-' : k}(${xMinus(r1)})(${xMinus(r2)})`;
    return {
      question: `The solution set of the inequality ${m(`${polyTex(coeffs)} ${op} 0`)} is`,
      correct,
      distractors: [m(intervalTex(opposite)), m(intervalTex(signFlip)), m(intervalTex(wrongBrackets))],
      explanation: [
        `Factor: ${m(`${polyTex(coeffs)} = ${factored}`)}, so the roots are ${m(`x=${r1}`)} and ${m(`x=${r2}`)}.`,
        k < 0
          ? `The leading coefficient is negative, so the parabola opens **downward**: it is positive *between* the roots and negative outside them. (Or multiply by ${m(String(k))} and reverse the inequality sign.)`
          : `The leading coefficient is positive, so the parabola opens upward: it is negative *between* the roots and positive outside them.`,
        closed ? 'The inequality is non-strict, so the roots themselves are included.' : 'The inequality is strict, so the roots are excluded.',
        `Solution set: ${correct}.`,
      ].join('\n\n'),
      difficulty: k === 1 ? 1 : 2,
      meta: { k, r1, r2, op, solution: sol },
    };
  },
  fallback: shiftedFallback,
};

const rationalInequality: GeneratorDef = {
  id: 'rational-inequality',
  name: 'Rational (fractional) inequality',
  topic: 'sets-inequalities',
  subtopic: 'rational-inequalities',
  make(r) {
    const [p, q] = distinctRoots(r, -5, 6);
    // numerator zero at a, denominator zero at b
    const numFirst = r.bool();
    const a = numFirst ? p : q;
    const b = numFirst ? q : p;
    const op = r.pick(OPS);
    const closed = op === '\\le' || op === '\\ge';
    const lo = Math.min(a, b);
    const hi = Math.max(a, b);
    const wantPositive = op === '>' || op === '\\ge';
    // (x-a)/(x-b) has the same sign as (x-a)(x-b): positive outside [lo,hi]
    const loClosed = closed && lo === a;
    const hiClosed = closed && hi === a;
    const sol = wantPositive
      ? [iv(-Infinity, lo, false, loClosed), iv(hi, Infinity, hiClosed, false)]
      : [iv(lo, hi, loClosed, hiClosed)];
    const includeB = wantPositive
      ? [iv(-Infinity, lo, false, closed), iv(hi, Infinity, closed, false)]
      : [iv(lo, hi, closed, closed)];
    const opposite = wantPositive ? [iv(lo, hi, loClosed, hiClosed)] : [iv(-Infinity, lo, false, loClosed), iv(hi, Infinity, hiClosed, false)];
    const allOpen = sol.map((i) => ({ ...i, loC: false, hiC: false }));
    const swapped = sol.map((i) => ({ ...i, loC: isFinite(i.lo) && i.lo === b, hiC: isFinite(i.hi) && i.hi === b }));
    const withA = sol.map((i) => ({ ...i, loC: isFinite(i.lo) && i.lo === a, hiC: isFinite(i.hi) && i.hi === a }));
    const withBoth = sol.map((i) => ({ ...i, loC: isFinite(i.lo), hiC: isFinite(i.hi) }));
    const correct = m(intervalTex(sol));
    const pool = closed ? [includeB, opposite, allOpen, swapped] : [opposite, withA, withBoth, swapped];
    return {
      question: `The solution set of ${m(`\\dfrac{${xMinus(a)}}{${xMinus(b)}} ${op} 0`)} is`,
      correct,
      distractors: pool.map((p) => m(intervalTex(p))),
      explanation: [
        `A quotient has the same sign as the product, so the inequality is equivalent to ${m(`(${xMinus(a)})(${xMinus(b)}) ${op} 0`)} **together with** ${m(`x \\ne ${b}`)}.`,
        `The critical points are ${m(`x=${a}`)} (numerator zero) and ${m(`x=${b}`)} (denominator zero). The product is positive outside ${m(`[${lo},${hi}]`)} and negative between them.`,
        closed
          ? `Because the inequality allows equality, ${m(`x=${a}`)} is included, but ${m(`x=${b}`)} is **never** included: the expression is undefined there.`
          : 'The inequality is strict, so neither critical point is included.',
        `Solution set: ${correct}.`,
      ].join('\n\n'),
      difficulty: closed ? 2 : 1,
      meta: { a, b, op, solution: sol },
    };
  },
  fallback: shiftedFallback,
};

const setOperations: GeneratorDef = {
  id: 'set-operations',
  name: 'Set operations with intervals',
  topic: 'sets-inequalities',
  subtopic: 'sets',
  make(r) {
    const [r1, r2] = distinctRoots(r, -4, 5);
    let k = r.int(r1 - 2, r2 + 2);
    if (k === r1 || k === r2) k = r1 + 1 === r2 ? r2 + 1 : r1 + 1;
    const A = [iv(r1, r2, false, false)]; // x^2 - (r1+r2)x + r1r2 < 0
    const bClosed = r.bool();
    const bUp = r.bool();
    const B = bUp ? [iv(k, Infinity, bClosed, false)] : [iv(-Infinity, k, false, bClosed)];
    const op = r.pick(['cap', 'cup', 'capc'] as const);
    const compute = (o: typeof op) => (o === 'cap' ? intersect(A, B) : o === 'cup' ? union(A, B) : intersect(A, complement(B)));
    const res = compute(op);
    const opTex = op === 'cap' ? 'A\\cap B' : op === 'cup' ? 'A\\cup B' : 'A\\cap(\\complement_{\\mathbb{R}}B)';
    const bTex = `\\{x\\mid x ${bUp ? (bClosed ? '\\ge' : '>') : bClosed ? '\\le' : '<'} ${k}\\}`;
    const others = (['cap', 'cup', 'capc'] as const).filter((o) => o !== op).map((o) => m(intervalTex(compute(o))));
    const wrongEnd = res.map((i) => ({ ...i, loC: isFinite(i.lo) && !i.loC, hiC: isFinite(i.hi) && !i.hiC }));
    const correct = m(intervalTex(res));
    return {
      question: `Let ${m(`A=\\{x\\mid ${polyTex([1, -(r1 + r2), r1 * r2])}<0\\}`)} and ${m(`B=${bTex}`)}. Then ${m(opTex)} equals`,
      correct,
      distractors: [...others, m(intervalTex(wrongEnd)), m(intervalTex(intersect(complement(A), B)))],
      explanation: [
        `Solve the quadratic: ${m(`(${xMinus(r1)})(${xMinus(r2)})<0`)} gives ${m(`A=(${r1},${r2})`)}.`,
        `${m(`B=${intervalTex(B)}`)}${op === 'capc' ? `, so ${m(`\\complement_{\\mathbb{R}}B=${intervalTex(complement(B))}`)} (the endpoint switches between open and closed).` : '.'}`,
        `Draw both on a number line and take ${op === 'cup' ? 'everything covered by at least one set' : 'the overlap'}: ${m(`${opTex}=${intervalTex(res)}`)}.`,
      ].join('\n\n'),
      difficulty: op === 'capc' ? 2 : 1,
      meta: { r1, r2, k, bUp, bClosed, op, solution: res },
    };
  },
  fallback: (_r, res) => {
    const { r1, r2 } = res.meta as { r1: number; r2: number };
    return [...shiftedFallback(_r, res), m(intervalTex([iv(r1, r2, true, true)])), m(intervalTex([iv(-Infinity, r1, false, false), iv(r2, Infinity, false, false)])), m('\\varnothing'), m('\\mathbb{R}')];
  },
};

const functionDomain: GeneratorDef = {
  id: 'function-domain',
  name: 'Domain of a function',
  topic: 'functions',
  subtopic: 'function-properties',
  make(r) {
    const variant = r.int(0, 2);
    const [a, b] = distinctRoots(r, -5, 6);
    let f: string;
    let sol: Interval[];
    let reasons: string;
    let wrong: Interval[][];
    if (variant === 0) {
      f = `\\sqrt{${xMinus(a)}}+\\ln(${b}-x)`.replace('(0-x)', '(-x)');
      sol = [iv(a, b, true, false)];
      reasons = `${m(`${xMinus(a)}\\ge 0`)} (square root) and ${m(`${b}-x>0`)} (logarithm), so ${m(`${a}\\le x<${b}`)}.`;
      wrong = [[iv(a, b, true, true)], [iv(a, b, false, false)], [iv(a, b, false, true)]];
    } else if (variant === 1) {
      f = `\\dfrac{1}{\\sqrt{${xMinus(a)}}}+\\sqrt{${b}-x}`.replace('{0-x}', '{-x}');
      sol = [iv(a, b, false, true)];
      reasons = `${m(`${xMinus(a)}>0`)} (square root in a denominator must be positive) and ${m(`${b}-x\\ge 0`)}, so ${m(`${a}<x\\le ${b}`)}.`;
      wrong = [[iv(a, b, true, true)], [iv(a, b, true, false)], [iv(a, b, false, false)]];
    } else {
      f = `\\lg(${polyTex([1, -(a + b), a * b])})`;
      sol = [iv(-Infinity, a, false, false), iv(b, Infinity, false, false)];
      reasons = `The argument of a logarithm must be positive: ${m(`(${xMinus(a)})(${xMinus(b)})>0`)}, so ${m(`x<${a}`)} or ${m(`x>${b}`)}.`;
      wrong = [[iv(a, b, false, false)], [iv(-Infinity, a, false, true), iv(b, Infinity, true, false)], [iv(a, b, true, true)]];
    }
    const correct = m(intervalTex(sol));
    return {
      question: `The domain of ${m(`f(x)=${f}`)} is`,
      correct,
      distractors: wrong.map((w) => m(intervalTex(w))),
      explanation: `${reasons}\n\nDomain: ${correct}.`,
      difficulty: variant === 2 ? 2 : 1,
      meta: { variant, a, b, solution: sol },
    };
  },
  fallback: shiftedFallback,
};

const logExp: GeneratorDef = {
  id: 'log-exp-evaluation',
  name: 'Evaluate logs and powers',
  topic: 'functions',
  subtopic: 'elementary-functions',
  make(r) {
    const variant = r.int(0, 3);
    if (variant === 0) {
      // lg x + lg y with xy = 10^k
      const k = r.int(1, 3);
      const pairs: [number, number][] = k === 1 ? [[2, 5], [4, 2.5]] : k === 2 ? [[4, 25], [2, 50], [5, 20]] : [[8, 125], [4, 250], [25, 40]];
      const [x, y] = r.pick(pairs);
      return {
        question: `Evaluate ${m(`\\lg ${x}+\\lg ${y}`)}.`,
        correct: m(String(k)),
        distractors: [m(`\\lg ${x + y}`), m(String(k + 1)), m(String(10 ** k)), m(`${k * 10}`)],
        explanation: `${m(`\\lg a+\\lg b=\\lg(ab)`)}, so the sum is ${m(`\\lg ${x * y}=\\lg 10^{${k}}=${k}`)}.`,
        difficulty: 1,
        meta: { variant, x, y, value: k },
      };
    }
    if (variant === 1) {
      // a^{p/q} with a = b^q
      const b = r.pick([2, 3, 4, 5]);
      const q = b === 2 ? r.pick([2, 3]) : r.pick([2, 3]);
      const p = r.pick([-2, -1, 1, 2, 3].filter((v) => Math.abs(v) !== q));
      const a = b ** q;
      const val = new Frac(1).mul(p > 0 ? b ** p : 1).div(p < 0 ? b ** -p : 1);
      return {
        question: `Evaluate ${m(`${a}^{${new Frac(p, q).tex()}}`)}.`,
        correct: m(val.tex()),
        distractors: [m(new Frac(1).div(val).tex()), m(val.neg().tex()), m(new Frac(a * p, q).tex()), m(String(b ** Math.abs(p) * (p < 0 ? -1 : 1)))],
        explanation: `${m(`${a}=${b}^{${q}}`)}, so ${m(`${a}^{${new Frac(p, q).tex()}}=${b}^{${q}\\cdot ${new Frac(p, q).tex()}}=${b}^{${p}}=${val.tex()}`)}.${p < 0 ? ' A negative exponent means a reciprocal, not a negative number.' : ''}`,
        difficulty: 2,
        meta: { variant, a, p, q, value: val.value() },
      };
    }
    if (variant === 2) {
      // log_b(b^k) - log with fraction
      const b = r.pick([2, 3, 5]);
      const k1 = r.int(2, 4);
      const k2 = r.int(1, 3);
      const val = k1 + k2;
      return {
        question: `Evaluate ${m(`\\log_{${b}}${b ** k1}-\\log_{${b}}\\dfrac{1}{${b ** k2}}`)}.`,
        correct: m(String(val)),
        distractors: [m(String(k1 - k2)), m(String(-val)), m(new Frac(k1, k2).tex()), m(String(k1 * k2))],
        explanation: `${m(`\\log_{${b}}${b ** k1}=${k1}`)} and ${m(`\\log_{${b}}\\dfrac{1}{${b ** k2}}=-${k2}`)}, so the value is ${m(`${k1}-(-${k2})=${val}`)}.`,
        difficulty: 1,
        meta: { variant, b, k1, k2, value: val },
      };
    }
    // change of base: log_a b * log_b c = log_a c
    const base = r.pick([2, 3]);
    const e1 = r.int(1, 2);
    const e2 = r.int(2, 4);
    const a = base ** e1;
    const mid = r.pick([3, 5, 7].filter((x) => x !== base));
    const c = base ** e2;
    const val = new Frac(e2, e1);
    return {
      question: `Evaluate ${m(`\\log_{${a}}${mid}\\cdot\\log_{${mid}}${c}`)}.`,
      correct: m(val.tex()),
      distractors: [m(new Frac(e1, e2).tex()), m(String(e2)), m(String(e1 * e2)), m(val.add(1).tex())],
      explanation: `By the change-of-base formula ${m(`\\log_a b\\cdot\\log_b c=\\log_a c`)}, the product is ${m(`\\log_{${a}}${c}=\\log_{${base}^{${e1}}}${base}^{${e2}}=${val.tex()}`)}.`,
      difficulty: 2,
      meta: { variant, a, mid, c, value: val.value() },
    };
  },
};

type Spec = { kind: 'pow'; base: number; exp: number } | { kind: 'log'; base: number; arg: number };
export function specValue(s: Spec): number {
  return s.kind === 'pow' ? Math.pow(s.base, s.exp) : Math.log(s.arg) / Math.log(s.base);
}
function specTex(s: Spec): string {
  const t = (x: number) => (Number.isInteger(x) ? String(x) : String(x));
  return s.kind === 'pow' ? `${t(s.base)}^{${t(s.exp)}}` : `\\log_{${t(s.base)}}${t(s.arg)}`;
}

const compareValues: GeneratorDef = {
  id: 'compare-values',
  name: 'Compare exponential/log values',
  topic: 'functions',
  subtopic: 'elementary-functions',
  make(r) {
    // one value > 1, one in (0,1), one < 0
    const big: Spec = r.pick<Spec>([
      { kind: 'pow', base: 2, exp: r.pick([0.1, 0.2, 0.3, 0.5]) },
      { kind: 'pow', base: 3, exp: r.pick([0.1, 0.2, 0.4]) },
      { kind: 'log', base: 2, arg: r.pick([3, 5, 7]) },
    ]);
    const mid: Spec = r.pick<Spec>([
      { kind: 'pow', base: 0.5, exp: r.pick([0.2, 0.3, 2]) },
      { kind: 'log', base: 3, arg: 2 },
      { kind: 'log', base: 5, arg: r.pick([2, 3]) },
      { kind: 'pow', base: 0.3, exp: 2 },
    ]);
    const neg: Spec = r.pick<Spec>([
      { kind: 'log', base: 0.5, arg: r.pick([3, 5]) },
      { kind: 'log', base: 2, arg: r.pick([0.3, 0.5, 0.7]) },
      { kind: 'log', base: 3, arg: 0.5 },
    ]);
    const letters = r.shuffle(['a', 'b', 'c']);
    const specs: Record<string, Spec> = { [letters[0]]: big, [letters[1]]: mid, [letters[2]]: neg };
    const order = (perm: string[]) => perm.join('<');
    const correctPerm = [letters[2], letters[1], letters[0]];
    const allPerms = [
      ['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a'],
    ].filter((p) => order(p) !== order(correctPerm));
    const reversed = [...correctPerm].reverse();
    const swapTop = [correctPerm[0], correctPerm[2], correctPerm[1]];
    const swapBottom = [correctPerm[1], correctPerm[0], correctPerm[2]];
    const ds = [reversed, swapTop, swapBottom, ...allPerms].map((p) => m(order(p)));
    const desc = (s: Spec) =>
      s === big ? `${m(specTex(s))} > 1` : s === mid ? `${m(`0<${specTex(s)}<1`)}` : `${m(specTex(s))} < 0`;
    return {
      question: `Let ${m(`a=${specTex(specs.a)}`)}, ${m(`b=${specTex(specs.b)}`)}, ${m(`c=${specTex(specs.c)}`)}. Which ordering is correct?`,
      correct: m(order(correctPerm)),
      distractors: ds,
      explanation: [
        'Compare each value with the benchmarks 0 and 1 (no calculator needed):',
        `- ${desc(big)}${big.kind === 'pow' ? ' because the base is greater than 1 and the exponent is positive' : ' because the argument is larger than the base'};`,
        `- ${desc(mid)}${mid.kind === 'pow' ? ' because the base is between 0 and 1 and the exponent is positive' : ' because the argument is between 1 and the base'};`,
        `- ${desc(neg)}${neg.base < 1 ? ' because a base below 1 gives a negative log for arguments above 1' : ' because the argument is less than 1'}.`,
        `Hence ${m(order(correctPerm))}.`,
      ].join('\n'),
      difficulty: 2,
      meta: { specs, ordering: correctPerm },
    };
  },
};

export const algebraGenerators = [quadraticInequality, rationalInequality, setOperations, functionDomain, logExp, compareValues];

