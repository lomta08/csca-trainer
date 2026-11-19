import type { GeneratorDef } from './core';
import { Frac, m } from './format';

/** Exact LaTeX for a few special trig values, matched numerically. */
const SPECIAL: [number, string][] = [
  [0, '0'],
  [0.5, '\\frac{1}{2}'],
  [Math.SQRT2 / 2, '\\frac{\\sqrt{2}}{2}'],
  [Math.sqrt(3) / 2, '\\frac{\\sqrt{3}}{2}'],
  [1, '1'],
  [Math.sqrt(3), '\\sqrt{3}'],
  [Math.sqrt(3) / 3, '\\frac{\\sqrt{3}}{3}'],
];

export function specialTex(v: number): string {
  for (const [x, t] of SPECIAL) {
    if (Math.abs(Math.abs(v) - x) < 1e-9) return v < -1e-9 ? `-${t}` : t;
  }
  throw new Error(`not a special value: ${v}`);
}

/** Evaluate the LaTeX produced by specialTex (used by tests). */
export function specialValue(t: string): number {
  const neg = t.startsWith('-');
  const body = neg ? t.slice(1) : t;
  const found = SPECIAL.find(([, s]) => s === body);
  if (!found) throw new Error(`unknown ${t}`);
  return neg ? -found[0] : found[0];
}

/** k·π/den as LaTeX, e.g. -5π/6 */
export function piTex(k: number, den: number): string {
  const f = new Frac(k, den);
  if (f.n === 0) return '0';
  const sign = f.n < 0 ? '-' : '';
  const a = Math.abs(f.n);
  const num = a === 1 ? '\\pi' : `${a}\\pi`;
  return f.d === 1 ? `${sign}${num}` : `${sign}\\frac{${num}}{${f.d}}`;
}

type Fn = 'sin' | 'cos' | 'tan';
const fnVal = (fn: Fn, x: number) => (fn === 'sin' ? Math.sin(x) : fn === 'cos' ? Math.cos(x) : Math.tan(x));

const trigSpecial: GeneratorDef = {
  id: 'trig-special-value',
  name: 'Trig special values',
  topic: 'functions',
  subtopic: 'trigonometry',
  make(r) {
    const den = r.pick([6, 4, 3]);
    const fn: Fn = r.pick(['sin', 'cos', 'tan'] as const);
    let k = r.int(-2 * den, 2 * den);
    // avoid multiples of π/2 for tan, and avoid boring k=0
    while (k === 0 || (fn === 'tan' && Math.abs(Math.cos((k * Math.PI) / den)) < 1e-9)) k = r.int(-2 * den, 2 * den);
    const x = (k * Math.PI) / den;
    const val = fnVal(fn, x);
    const correct = m(specialTex(val));
    const ref = Math.abs(val);
    const co: Fn = fn === 'sin' ? 'cos' : fn === 'cos' ? 'sin' : 'tan';
    const coVal = co === 'tan' ? (Math.abs(val) > 1e-9 ? 1 / val : 1) : fnVal(co, x);
    const distractors = [m(specialTex(-val)), m(specialTex(coVal)), m(specialTex(-coVal)), m(specialTex(ref)), m(specialTex(val === 0 ? 1 : 0))];
    // quadrant / reference-angle explanation
    const turns = Math.floor((x + 1e-9) / (2 * Math.PI));
    const reduced = x - turns * 2 * Math.PI;
    const redK = Math.round((reduced * den) / Math.PI);
    return {
      question: `${m(`\\${fn}\\left(${piTex(k, den)}\\right)`)} equals`,
      correct,
      distractors,
      explanation: [
        turns !== 0
          ? `Add or subtract whole turns of ${m('2\\pi')}: ${m(`${piTex(k, den)} = ${piTex(redK, den)} ${turns > 0 ? '+' : '-'} ${piTex(2 * Math.abs(turns), 1)}`)}, so the value equals ${m(`\\${fn}\\left(${piTex(redK, den)}\\right)`)}.`
          : `The angle ${m(piTex(k, den))} is already between ${m('0')} and ${m('2\\pi')}.`,
        `Find the reference angle and the sign from the quadrant (ASTC rule: All, Sin, Tan, Cos are positive in quadrants I–IV).`,
        `${m(`\\${fn}\\left(${piTex(k, den)}\\right)=${specialTex(val)}`)}.`,
      ].join('\n\n'),
      difficulty: Math.abs(k) > den * 1 ? 2 : 1,
      meta: { fn, k, den, value: val },
    };
  },
  fallback: (r, res) => {
    const v = res.meta.value as number;
    const sign = v < 0 ? -1 : 1;
    return r.shuffle(SPECIAL.slice(1).map(([x]) => m(specialTex(sign * x))));
  },
};

const TRIPLES: [number, number, number][] = [
  [3, 4, 5],
  [5, 12, 13],
  [8, 15, 17],
  [7, 24, 25],
];
const QUAD_TEX: Record<number, string> = {
  1: '\\left(0,\\frac{\\pi}{2}\\right)',
  2: '\\left(\\frac{\\pi}{2},\\pi\\right)',
  3: '\\left(\\pi,\\frac{3\\pi}{2}\\right)',
  4: '\\left(\\frac{3\\pi}{2},2\\pi\\right)',
};

const trigIdentity: GeneratorDef = {
  id: 'trig-identity',
  name: 'Trig identities from one ratio',
  topic: 'functions',
  subtopic: 'trigonometry',
  make(r) {
    const [p, q, h] = r.pick(TRIPLES);
    const swap = r.bool();
    const [opp, adj] = swap ? [q, p] : [p, q];
    const quad = r.int(1, 4);
    const sinSign = quad <= 2 ? 1 : -1;
    const cosSign = quad === 1 || quad === 4 ? 1 : -1;
    const sin = new Frac(sinSign * opp, h);
    const cos = new Frac(cosSign * adj, h);
    const givenSin = r.bool();
    const target = r.pick(['cos', 'tan', 'sin2', 'cos2'] as const);
    const givenTex = givenSin ? `\\sin\\alpha=${sin.tex()}` : `\\cos\\alpha=${cos.tex()}`;
    let ans: Frac;
    let tTex: string;
    let wrong: Frac[];
    let how: string;
    if (target === 'cos') {
      // ask for the other basic ratio
      ans = givenSin ? cos : sin;
      tTex = givenSin ? '\\cos\\alpha' : '\\sin\\alpha';
      wrong = [ans.neg(), givenSin ? new Frac(cosSign * opp, h) : new Frac(sinSign * adj, h), new Frac(ans.n, ans.d).neg().add(0)];
      how = `${m(`\\sin^2\\alpha+\\cos^2\\alpha=1`)} gives ${m(`${tTex}=\\pm\\sqrt{1-\\left(${(givenSin ? sin : cos).tex()}\\right)^2}=\\pm${new Frac(Math.abs(ans.n), ans.d).tex()}`)}; the quadrant fixes the sign.`;
    } else if (target === 'tan') {
      ans = sin.div(cos);
      tTex = '\\tan\\alpha';
      wrong = [ans.neg(), cos.div(sin), cos.div(sin).neg()];
      how = `First find the missing ratio with ${m('\\sin^2\\alpha+\\cos^2\\alpha=1')} and the quadrant: ${m(`\\sin\\alpha=${sin.tex()},\\ \\cos\\alpha=${cos.tex()}`)}. Then ${m(`\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}=${ans.tex()}`)}.`;
    } else if (target === 'sin2') {
      ans = sin.mul(cos).mul(2);
      tTex = '\\sin 2\\alpha';
      wrong = [ans.neg(), sin.mul(cos), new Frac(1).sub(sin.mul(sin).mul(2))];
      how = `${m(`\\sin\\alpha=${sin.tex()},\\ \\cos\\alpha=${cos.tex()}`)} (sign from the quadrant), so ${m(`\\sin2\\alpha=2\\sin\\alpha\\cos\\alpha=${ans.tex()}`)}.`;
    } else {
      ans = cos.mul(cos).sub(sin.mul(sin));
      tTex = '\\cos 2\\alpha';
      wrong = [ans.neg(), sin.mul(cos).mul(2), new Frac(1).sub(cos.mul(cos).mul(2)).neg().add(0).neg()];
      how = `${m(`\\cos2\\alpha=1-2\\sin^2\\alpha=2\\cos^2\\alpha-1=${ans.tex()}`)}. (The quadrant does not matter here because only squares appear.)`;
    }
    return {
      question: `Given ${m(givenTex)} and ${m(`\\alpha\\in${QUAD_TEX[quad]}`)}, find ${m(tTex)}.`,
      correct: m(ans.tex()),
      distractors: [...wrong.map((w) => m(w.tex())), m(new Frac(opp, adj).tex()), m(new Frac(adj, opp).neg().tex())],
      explanation: how,
      difficulty: target === 'cos' ? 1 : 2,
      meta: { opp, adj, h, quad, givenSin, target, value: ans.value() },
    };
  },
};

const arithmeticSeq: GeneratorDef = {
  id: 'arithmetic-sequence',
  name: 'Arithmetic sequence',
  topic: 'functions',
  subtopic: 'sequences',
  make(r) {
    const a1 = r.int(-8, 10);
    const d = r.nonzero(-4, 5);
    const term = (n: number) => a1 + (n - 1) * d;
    const S = (n: number) => (n * (2 * a1 + (n - 1) * d)) / 2;
    const variant = r.int(0, 2);
    if (variant === 0) {
      const p = r.int(2, 4);
      const q = p + r.int(2, 5);
      const k = q + r.int(2, 8);
      const ans = term(k);
      return {
        question: `In an arithmetic sequence ${m('\\{a_n\\}')}, ${m(`a_{${p}}=${term(p)}`)} and ${m(`a_{${q}}=${term(q)}`)}. Find ${m(`a_{${k}}`)}.`,
        correct: m(String(ans)),
        distractors: [m(String(a1 + k * d)), m(String(term(k - 1))), m(String(ans + 2 * d)), m(String(-ans))],
        explanation: `${m(`d=\\dfrac{a_{${q}}-a_{${p}}}{${q}-${p}}=\\dfrac{${term(q) - term(p)}}{${q - p}}=${d}`)}. Then ${m(`a_{${k}}=a_{${q}}+(${k}-${q})d=${term(q)}+${k - q}\\cdot(${d})=${ans}`)}.`,
        difficulty: 1,
        meta: { a1, d, variant, k, value: ans },
      };
    }
    if (variant === 1) {
      const n = r.int(6, 15);
      const ans = S(n);
      return {
        question: `An arithmetic sequence has first term ${m(`a_1=${a1}`)} and common difference ${m(`d=${d}`)}. Find the sum of the first ${m(String(n))} terms, ${m(`S_{${n}}`)}.`,
        correct: m(String(ans)),
        distractors: [m(String((n * (2 * a1 + n * d)) / 2)), m(String(n * (a1 + term(n)))), m(String(S(n - 1))), m(String(n * a1 + n * n * d))],
        explanation: `${m(`S_n=na_1+\\dfrac{n(n-1)}{2}d=${n}\\cdot(${a1})+\\dfrac{${n}\\cdot${n - 1}}{2}\\cdot(${d})=${ans}`)}.`,
        difficulty: 1,
        meta: { a1, d, variant, n, value: ans },
      };
    }
    // property: a_p + a_q = 2 a_mid, S_{2m-1} = (2m-1) a_m
    const mid = r.int(3, 7);
    const off = r.int(1, mid - 1);
    const n = 2 * mid - 1;
    const sumPair = term(mid - off) + term(mid + off);
    const ans = n * term(mid);
    return {
      question: `In an arithmetic sequence ${m('\\{a_n\\}')}, ${m(`a_{${mid - off}}+a_{${mid + off}}=${sumPair}`)}. Find ${m(`S_{${n}}`)}.`,
      correct: m(String(ans)),
      distractors: [m(String(n * sumPair)), m(String((n * sumPair) / 4)), m(String((n + 1) * term(mid))), m(String(ans / 2 + n))],
      explanation: `Because ${m(`${mid - off}+${mid + off}=1+${n}`)}, ${m(`a_1+a_{${n}}=a_{${mid - off}}+a_{${mid + off}}=${sumPair}`)}. So ${m(`S_{${n}}=\\dfrac{${n}(a_1+a_{${n}})}{2}=\\dfrac{${n}\\cdot ${sumPair}}{2}=${ans}`)}.`,
      difficulty: 2,
      meta: { a1, d, variant, n, value: ans },
    };
  },
};

const geometricSeq: GeneratorDef = {
  id: 'geometric-sequence',
  name: 'Geometric sequence',
  topic: 'functions',
  subtopic: 'sequences',
  make(r) {
    const a1 = r.pick([1, 2, 3, -1, -2, 4]);
    const q = r.pick([2, 3, -2, -3, 2]);
    const term = (n: number) => a1 * q ** (n - 1);
    const S = (n: number) => (a1 * (1 - q ** n)) / (1 - q);
    const variant = r.int(0, 2);
    if (variant === 0) {
      const n = r.int(4, 7);
      const ans = term(n);
      return {
        question: `A geometric sequence has ${m(`a_1=${a1}`)} and common ratio ${m(`q=${q}`)}. Find ${m(`a_{${n}}`)}.`,
        correct: m(String(ans)),
        distractors: [m(String(a1 * q ** n)), m(String(-ans)), m(String(a1 + (n - 1) * q)), m(String(term(n - 1)))],
        explanation: `${m(`a_n=a_1q^{n-1}`)}, so ${m(`a_{${n}}=${a1}\\cdot(${q})^{${n - 1}}=${ans}`)}.`,
        difficulty: 1,
        meta: { a1, q, variant, n, value: ans },
      };
    }
    if (variant === 1) {
      const n = r.int(4, 6);
      const ans = S(n);
      return {
        question: `A geometric sequence has ${m(`a_1=${a1}`)} and common ratio ${m(`q=${q}`)}. Find the sum of its first ${m(String(n))} terms.`,
        correct: m(String(ans)),
        distractors: [m(String(S(n + 1))), m(String(S(n - 1))), m(String((a1 * (1 - q ** (n - 1))) / (1 - q) + a1 * q ** n)), m(String(-ans)), m(String(a1 * q ** n))],
        explanation: `${m(`S_n=\\dfrac{a_1(1-q^n)}{1-q}=\\dfrac{${a1}(1-(${q})^{${n}})}{1-(${q})}=${ans}`)}.`,
        difficulty: 2,
        meta: { a1, q, variant, n, value: ans },
      };
    }
    const i = r.int(1, 3);
    const j = i + 3;
    const ans = q;
    return {
      question: `In a geometric sequence, ${m(`a_{${i}}=${term(i)}`)} and ${m(`a_{${j}}=${term(j)}`)}. Find the common ratio ${m('q')}.`,
      correct: m(String(ans)),
      distractors: [m(String(-ans)), m(new Frac(1, ans).tex()), m(String(ans * ans)), m(String(term(j) / term(i)))],
      explanation: `${m(`\\dfrac{a_{${j}}}{a_{${i}}}=q^{${j - i}}=\\dfrac{${term(j)}}{${term(i)}}=${term(j) / term(i)}`)}, so ${m(`q=${ans}`)} (a cube root has only one real value, so there is no ± ambiguity).`,
      difficulty: 2,
      meta: { a1, q, variant, value: ans },
    };
  },
};

export const trigSeqGenerators = [trigSpecial, trigIdentity, arithmeticSeq, geometricSeq];
