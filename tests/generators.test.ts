import { describe, expect, it } from 'vitest';
import { GENERATORS, generate, fromGeneratedId, type Generated } from '../src/lib/generators';
import { specialValue } from '../src/lib/generators/trigseq';
import { evalTex, tryEval, parseIntervals, member, GRID, parseComplex, close, strip, phi, invPhi } from './texeval';

const SEEDS = Array.from({ length: 250 }, (_, i) => i * 7919 + 13);

/** Each checker independently recomputes the answer from the generator's parameters. */
type Checker = (q: Generated) => void;

const correctOpt = (q: Generated) => q.options[q.answer];
const wrongOpts = (q: Generated) => q.options.filter((_, i) => i !== q.answer);

/** Correct option evaluates to `value`; every wrong option evaluates to something else (when numeric). */
function numeric(q: Generated, value: number) {
  const got = evalTex(correctOpt(q));
  expect(close(got, value), `${q.id}: correct option ${correctOpt(q)} = ${got}, expected ${value}`).toBe(true);
  for (const w of wrongOpts(q)) {
    const v = tryEval(w);
    if (v !== null) expect(close(v, value), `${q.id}: distractor ${w} also equals ${value}`).toBe(false);
  }
}

/** Correct option (interval union) agrees with `truth` on a grid; every wrong option disagrees somewhere. */
function solutionSet(q: Generated, truth: (x: number) => boolean) {
  const sol = parseIntervals(correctOpt(q));
  for (const x of GRID) expect(member(sol, x), `${q.id} at x=${x}: ${correctOpt(q)}`).toBe(truth(x));
  for (const w of wrongOpts(q)) {
    const ivs = parseIntervals(w);
    expect(GRID.some((x) => member(ivs, x) !== truth(x)), `${q.id}: distractor ${w} is also correct`).toBe(true);
  }
}

const cmp = (lhs: number, op: string) => (op === '<' ? lhs < 0 : op === '>' ? lhs > 0 : op === '\\le' ? lhs <= 0 : lhs >= 0);

const checkers: Record<string, Checker> = {
  'quadratic-inequality': (q) => {
    const { k, r1, r2, op } = q.meta as { k: number; r1: number; r2: number; op: string };
    solutionSet(q, (x) => cmp(k * (x - r1) * (x - r2), op));
  },
  'rational-inequality': (q) => {
    const { a, b, op } = q.meta as { a: number; b: number; op: string };
    solutionSet(q, (x) => x !== b && cmp((x - a) / (x - b), op));
  },
  'set-operations': (q) => {
    const { r1, r2, k, bUp, bClosed, op } = q.meta as { r1: number; r2: number; k: number; bUp: boolean; bClosed: boolean; op: string };
    const inA = (x: number) => (x - r1) * (x - r2) < 0;
    const inB = (x: number) => (bUp ? (bClosed ? x >= k : x > k) : bClosed ? x <= k : x < k);
    solutionSet(q, (x) => (op === 'cap' ? inA(x) && inB(x) : op === 'cup' ? inA(x) || inB(x) : inA(x) && !inB(x)));
  },
  'function-domain': (q) => {
    const { variant, a, b } = q.meta as { variant: number; a: number; b: number };
    const ok = (x: number) => (variant === 0 ? x - a >= 0 && b - x > 0 : variant === 1 ? x - a > 0 && b - x >= 0 : (x - a) * (x - b) > 0);
    solutionSet(q, ok);
  },
  'log-exp-evaluation': (q) => {
    const mt = q.meta as Record<string, number>;
    let v: number;
    if (mt.variant === 0) v = Math.log10(mt.x) + Math.log10(mt.y);
    else if (mt.variant === 1) v = Math.pow(mt.a, mt.p / mt.q);
    else if (mt.variant === 2) v = Math.log(mt.b ** mt.k1) / Math.log(mt.b) - Math.log(1 / mt.b ** mt.k2) / Math.log(mt.b);
    else v = (Math.log(mt.mid) / Math.log(mt.a)) * (Math.log(mt.c) / Math.log(mt.mid));
    numeric(q, v);
  },
  'compare-values': (q) => {
    const specs = q.meta.specs as Record<string, { kind: string; base: number; exp?: number; arg?: number }>;
    const val = (s: (typeof specs)[string]) => (s.kind === 'pow' ? Math.pow(s.base, s.exp!) : Math.log(s.arg!) / Math.log(s.base));
    const order = ['a', 'b', 'c'].sort((x, y) => val(specs[x]) - val(specs[y])).join('<');
    expect(strip(correctOpt(q))).toBe(order);
    for (const w of wrongOpts(q)) expect(strip(w)).not.toBe(order);
  },
  'trig-special-value': (q) => {
    const { fn, k, den } = q.meta as { fn: string; k: number; den: number };
    const x = (k * Math.PI) / den;
    const v = fn === 'sin' ? Math.sin(x) : fn === 'cos' ? Math.cos(x) : Math.tan(x);
    expect(close(specialValue(strip(correctOpt(q))), v, 1e-9) || Math.abs(v) < 1e-9 && strip(correctOpt(q)) === '0').toBe(true);
    for (const w of wrongOpts(q)) expect(Math.abs(specialValue(strip(w)) - v) > 1e-6).toBe(true);
  },
  'trig-identity': (q) => {
    const { opp, adj, h, quad, target } = q.meta as { opp: number; adj: number; h: number; quad: number; target: string };
    // reconstruct α numerically from the quadrant and the reference angle
    const ref = Math.atan2(opp, adj);
    const alpha = quad === 1 ? ref : quad === 2 ? Math.PI - ref : quad === 3 ? Math.PI + ref : 2 * Math.PI - ref;
    expect(close(Math.abs(Math.sin(alpha)), opp / h)).toBe(true);
    const givenSin = q.meta.givenSin as boolean;
    const v = target === 'cos' ? (givenSin ? Math.cos(alpha) : Math.sin(alpha)) : target === 'tan' ? Math.tan(alpha) : target === 'sin2' ? Math.sin(2 * alpha) : Math.cos(2 * alpha);
    numeric(q, v);
  },
  'arithmetic-sequence': (q) => {
    const { a1, d, variant, k, n } = q.meta as Record<string, number>;
    const terms = [a1];
    for (let i = 1; i < 40; i++) terms.push(terms[i - 1] + d);
    const sum = (m: number) => terms.slice(0, m).reduce((s, t) => s + t, 0);
    numeric(q, variant === 0 ? terms[k - 1] : sum(n));
  },
  'geometric-sequence': (q) => {
    const { a1, q: r, variant, n } = q.meta as Record<string, number>;
    const terms = [a1];
    for (let i = 1; i < 12; i++) terms.push(terms[i - 1] * r);
    numeric(q, variant === 0 ? terms[n - 1] : variant === 1 ? terms.slice(0, n).reduce((s, t) => s + t, 0) : r);
  },
  'derivative-at-point': (q) => {
    const { coeffs, x0 } = q.meta as { coeffs: number[]; x0: number };
    const f = (x: number) => coeffs.reduce((acc, c) => acc * x + c, 0);
    const h = 1e-4;
    const num = (f(x0 + h) - f(x0 - h)) / (2 * h);
    numeric(q, Math.round(num));
    expect(Math.abs(num - Math.round(num)) < 1e-4).toBe(true);
  },
  'tangent-line': (q) => {
    const { coeffs, x0 } = q.meta as { coeffs: number[]; x0: number };
    const f = (x: number) => coeffs.reduce((acc, c) => acc * x + c, 0);
    const h = 1e-4;
    const slope = Math.round((f(x0 + h) - f(x0 - h)) / (2 * h));
    const parse = (s: string) => {
      const t = strip(s).replace(/^y=/, '');
      // evaluate line at two points by substituting x
      const at = (x: number) => evalTex(t.replace(/x/g, `*(${x})`).replace(/^\*/, '').replace(/([+-])\*/g, '$1'));
      return [at(1) - at(0), at(0)];
    };
    const [ms, cs] = parse(correctOpt(q));
    expect(close(ms, slope)).toBe(true);
    expect(close(ms * x0 + cs, f(x0))).toBe(true);
    for (const w of wrongOpts(q)) {
      const [mw, cw] = parse(w);
      expect(close(mw, slope) && close(cw, cs)).toBe(false);
    }
  },
  'cubic-extrema': (q) => {
    const { coeffs, wantMax } = q.meta as { coeffs: number[]; wantMax: boolean };
    const f = (x: number) => coeffs.reduce((acc, c) => acc * x + c, 0);
    // scan for local extrema on a fine grid
    const xs = Array.from({ length: 4001 }, (_, i) => -10 + i * 0.005);
    const found: number[] = [];
    for (let i = 1; i < xs.length - 1; i++) {
      const [a, b, c] = [f(xs[i - 1]), f(xs[i]), f(xs[i + 1])];
      if (wantMax ? b > a && b >= c : b < a && b <= c) found.push(Math.round(b * 1000) / 1000);
    }
    expect(found.length).toBe(1);
    numeric(q, found[0]);
  },
  'point-line-distance': (q) => {
    const { A, B, C, x0, y0 } = q.meta as Record<string, number>;
    // brute-force minimise distance along the line
    const p0 = B !== 0 ? [0, -C / B] : [-C / A, 0];
    const dir = [B, -A];
    let best = Infinity;
    let lo = -1000, hi = 1000;
    const dist = (t: number) => Math.hypot(p0[0] + t * dir[0] - x0, p0[1] + t * dir[1] - y0);
    for (let i = 0; i < 200; i++) {
      const m1 = lo + (hi - lo) / 3, m2 = hi - (hi - lo) / 3;
      if (dist(m1) < dist(m2)) hi = m2;
      else lo = m1;
    }
    best = dist((lo + hi) / 2);
    numeric(q, best);
  },
  'circle-center-radius': (q) => {
    const { D, E, F } = q.meta as Record<string, number>;
    const parse = (s: string) => {
      const mm = /centre \$\((-?\d+),(-?\d+)\)\$, radius \$(.+)\$/.exec(s)!;
      return [Number(mm[1]), Number(mm[2]), evalTex(mm[3])];
    };
    const onCircle = ([a, b, rr]: number[]) =>
      [0, 1, 2, 3, 4, 5].every((j) => {
        const x = a + rr * Math.cos(j), y = b + rr * Math.sin(j);
        return Math.abs(x * x + y * y + D * x + E * y + F) < 1e-6;
      });
    expect(onCircle(parse(correctOpt(q)))).toBe(true);
    for (const w of wrongOpts(q)) expect(onCircle(parse(w))).toBe(false);
  },
  'ellipse-parameters': (q) => conicCheck(q, 'ellipse'),
  'hyperbola-parameters': (q) => conicCheck(q, 'hyperbola'),
  'parabola-focus': (q) => {
    const { k, onX, ask } = q.meta as { k: number; onX: boolean; ask: string };
    // a point on the curve: y^2 = kx → (t^2/k, t); x^2 = ky → (t, t^2/k)
    const pts = [1, 2, -3].map((t) => (onX ? [(t * t) / k, t] : [t, (t * t) / k]));
    const parsePoint = (s: string) => strip(s).replace(/[()]/g, '').split(',').map(evalTex);
    if (ask === 'focus') {
      const ok = (f: number[]) => pts.every(([x, y]) => close(Math.hypot(x - f[0], y - f[1]), onX ? Math.abs(x + k / 4) : Math.abs(y + k / 4)));
      expect(ok(parsePoint(correctOpt(q)))).toBe(true);
      for (const w of wrongOpts(q)) expect(ok(parsePoint(w))).toBe(false);
    } else {
      const parseDir = (s: string) => {
        const [v, val] = strip(s).split('=');
        return [v === 'x' ? 1 : 0, evalTex(val)] as const;
      };
      const ok = ([isX, c]: readonly [number, number]) =>
        pts.every(([x, y]) => close(Math.hypot(x - (onX ? k / 4 : 0), y - (onX ? 0 : k / 4)), isX ? Math.abs(x - c) : Math.abs(y - c)));
      expect(ok(parseDir(correctOpt(q)))).toBe(true);
      for (const w of wrongOpts(q)) expect(ok(parseDir(w))).toBe(false);
    }
  },
  'dot-product': (q) => {
    const mt = q.meta as { variant: number; a: number[]; b: number[]; t: number };
    const dot = (u: number[], v: number[]) => u[0] * v[0] + u[1] * v[1];
    if (mt.variant === 0) numeric(q, dot(mt.a, mt.b));
    else if (mt.variant === 1) numeric(q, dot([2 * mt.a[0] - mt.b[0], 2 * mt.a[1] - mt.b[1]], mt.a));
    else {
      const mval = evalTex(correctOpt(q));
      expect(Math.abs(dot(mt.a, [mval, mt.t])) < 1e-9).toBe(true);
      for (const w of wrongOpts(q)) expect(Math.abs(dot(mt.a, [evalTex(w), mt.t])) < 1e-9).toBe(false);
    }
  },
  'vector-angle': (q) => {
    const mt = q.meta as { a?: number[]; b?: number[]; ma?: number; mb?: number; dot?: number };
    const cos = mt.a ? (mt.a[0] * mt.b![0] + mt.a[1] * mt.b![1]) / (Math.hypot(mt.a[0], mt.a[1]) * Math.hypot(mt.b![0], mt.b![1])) : mt.dot! / (mt.ma! * mt.mb!);
    numeric(q, Math.acos(Math.max(-1, Math.min(1, cos))));
  },
  'complex-arithmetic': (q) => {
    const mt = q.meta as Record<string, number>;
    let re: number, im: number;
    if (mt.variant === 0) [re, im] = [mt.a * mt.c - mt.b * mt.d, mt.a * mt.d + mt.b * mt.c];
    else if (mt.variant === 1) {
      const den = mt.wa ** 2 + mt.wb ** 2;
      [re, im] = [(mt.za * mt.wa + mt.zb * mt.wb) / den, (mt.zb * mt.wa - mt.za * mt.wb) / den];
    } else {
      // repeated multiplication by i
      let [x, y] = [1, 0];
      for (let i = 0; i < mt.n % 4; i++) [x, y] = [-y, x];
      [re, im] = [x, y];
    }
    const [cr, ci] = parseComplex(correctOpt(q));
    expect(close(cr, re) && close(ci, im), `${q.id} ${correctOpt(q)} vs ${re}+${im}i`).toBe(true);
    for (const w of wrongOpts(q)) {
      const [wr, wi] = parseComplex(w);
      expect(close(wr, re) && close(wi, im)).toBe(false);
    }
  },
  'complex-modulus': (q) => {
    const mt = q.meta as Record<string, number>;
    numeric(q, mt.wa !== undefined ? Math.hypot(mt.a, mt.b) / Math.hypot(mt.wa, mt.wb) : Math.hypot(mt.a, mt.b));
  },
  'distance-3d': (q) => {
    const { A, B } = q.meta as { A: number[]; B: number[] };
    numeric(q, Math.hypot(A[0] - B[0], A[1] - B[1], A[2] - B[2]));
  },
  'dice-probability': (q) => {
    const { variant, param } = q.meta as Record<string, number>;
    let fav = 0;
    for (let a = 1; a <= 6; a++)
      for (let b = 1; b <= 6; b++) {
        if (variant === 0 && a + b === param) fav++;
        if (variant === 1 && a + b >= param) fav++;
        if (variant === 2 && (a * b) % param === 0) fav++;
      }
    numeric(q, fav / 36);
  },
  'balls-probability': (q) => {
    const { red, white, variant } = q.meta as { red: number; white: number; variant: string };
    const balls = [...Array(red).fill('R'), ...Array(white).fill('W')];
    let fav = 0, tot = 0;
    for (let i = 0; i < balls.length; i++)
      for (let j = i + 1; j < balls.length; j++) {
        tot++;
        const pair = [balls[i], balls[j]];
        if (variant === 'both-red' && pair.every((c) => c === 'R')) fav++;
        if (variant === 'one-each' && pair.includes('R') && pair.includes('W')) fav++;
        if (variant === 'at-least-one-white' && pair.includes('W')) fav++;
      }
    numeric(q, fav / tot);
  },
  'mean-variance': (q) => {
    const mt = q.meta as { variant: number; data?: number[]; mu: number; s2: number; a: number; b: number };
    const stats = (xs: number[]) => {
      const mean = xs.reduce((s, x) => s + x, 0) / xs.length;
      return [mean, xs.reduce((s, x) => s + (x - mean) ** 2, 0) / xs.length];
    };
    if (mt.variant === 0) numeric(q, stats(mt.data!)[1]);
    else {
      // a concrete data set with the given mean and variance, transformed
      const sd = Math.sqrt(mt.s2);
      const [mean, variance] = stats([mt.mu - sd, mt.mu + sd].map((x) => mt.a * x + mt.b));
      if (correctOpt(q).startsWith('mean')) {
        const mm = /mean \$(-?\d+)\$, variance \$(-?\d+)\$/;
        const [, cm, cv] = mm.exec(correctOpt(q))!.map(Number);
        expect(close(cm, mean) && close(cv, variance)).toBe(true);
        for (const w of wrongOpts(q)) {
          const [, wm, wv] = mm.exec(w)!.map(Number);
          expect(close(wm, mean) && close(wv, variance)).toBe(false);
        }
      } else numeric(q, variance);
    }
  },
  'normal-symmetry': (q) => {
    const { mu, k, p, variant } = q.meta as Record<string, number>;
    // choose σ so that P(X > μ+k) = p, then compute the asked probability with the real normal CDF
    const sigma = k / invPhi(1 - p);
    const P = (x: number) => phi((x - mu) / sigma); // P(X < x)
    const v = variant === 0 ? P(mu + k) - P(mu - k) : variant === 1 ? P(mu + k) - P(mu) : P(2 * mu - (mu + k));
    numeric(q, Math.round(v * 1000) / 1000);
  },
};

function conicCheck(q: Generated, kind: 'ellipse' | 'hyperbola') {
  const { a2, b2, vertical, ask } = q.meta as { a2: number; b2: number; vertical: boolean; ask: string };
  const a = Math.sqrt(a2), b = Math.sqrt(b2);
  const c = kind === 'ellipse' ? Math.sqrt(a2 - b2) : Math.sqrt(a2 + b2);
  // sanity: a point on the curve has |PF1 ± PF2| = 2a with the computed c
  const t = 0.7;
  const P = kind === 'ellipse' ? [a * Math.cos(t), b * Math.sin(t)] : [a / Math.cos(t), b * Math.tan(t)];
  const s = Math.abs(Math.hypot(P[0] - c, P[1]) + (kind === 'ellipse' ? 1 : -1) * Math.hypot(P[0] + c, P[1]));
  expect(close(s, 2 * a)).toBe(true);
  const parseFoci = (str: string) => {
    const sx = strip(str).replace(/[()]/g, '');
    const [x, y] = sx.split(',');
    const onY = x === '0';
    return [onY ? 1 : 0, evalTex((onY ? y : x).replace('\\pm', ''))];
  };
  if (ask === 'e') numeric(q, c / a);
  else if (ask === 'major') numeric(q, 2 * a);
  else if (ask === 'foci') {
    const ok = ([onY, v]: number[]) => onY === (vertical ? 1 : 0) && close(v, c);
    expect(ok(parseFoci(correctOpt(q)))).toBe(true);
    for (const w of wrongOpts(q)) expect(ok(parseFoci(w))).toBe(false);
  } else {
    const slope = vertical ? a / b : b / a;
    const parseAsym = (str: string) => {
      const sx = strip(str).replace('y=\\pm', '').replace(/x$/, '').trim();
      return sx === '' ? 1 : evalTex(sx);
    };
    expect(close(parseAsym(correctOpt(q)), slope)).toBe(true);
    for (const w of wrongOpts(q)) expect(close(parseAsym(w), slope)).toBe(false);
  }
}

describe('math generators', () => {
  it('has at least 20 generators, each with a checker', () => {
    expect(GENERATORS.length).toBeGreaterThanOrEqual(20);
    for (const g of GENERATORS) expect(checkers[g.id], `missing checker for ${g.id}`).toBeTypeOf('function');
  });

  for (const g of GENERATORS) {
    it(`${g.id}: answers are correct and options are well-formed`, () => {
      const positions = [0, 0, 0, 0];
      for (const seed of SEEDS) {
        const q = generate(g.id, seed);
        expect(q.options).toHaveLength(4);
        expect(new Set(q.options).size, `${q.id} duplicate options ${q.options.join(' | ')}`).toBe(4);
        expect(q.answer).toBeGreaterThanOrEqual(0);
        expect(q.answer).toBeLessThan(4);
        expect(q.meta.usedFiller, `${q.id} needed filler distractors: ${q.options.join(' | ')}`).toBeUndefined();
        expect(q.question.length).toBeGreaterThan(5);
        expect(q.explanation.length).toBeGreaterThan(10);
        expect(q.options.join('')).not.toMatch(/NaN|undefined|Infinity/);
        positions[q.answer]++;
        checkers[g.id](q);
      }
      // positions are spread out
      for (const p of positions) expect(p).toBeGreaterThan(SEEDS.length / 10);
    });
  }

  it('is deterministic and rebuildable from the id', () => {
    for (const g of GENERATORS) {
      const a = generate(g.id, 12345);
      const b = fromGeneratedId(a.id)!;
      expect(b.options).toEqual(a.options);
      expect(b.answer).toBe(a.answer);
    }
  });
});
