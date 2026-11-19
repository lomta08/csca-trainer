import type { GeneratorDef } from './core';
import { Frac, m, sqrtTex, xMinus, gcd } from './format';
import { piTex } from './trigseq';

const pt = (x: number, y: number) => `(${x},${y})`;

/** Ax+By+C=0 as LaTeX */
export function lineGeneralTex(A: number, B: number, C: number): string {
  const term = (c: number, v: string, first: boolean) => {
    if (c === 0) return '';
    const sign = c < 0 ? '-' : first ? '' : '+';
    const abs = Math.abs(c);
    return `${sign}${abs === 1 && v ? '' : abs}${v}`;
  };
  let s = term(A, 'x', true);
  s += term(B, 'y', s === '');
  s += term(C, '', s === '');
  return `${s}=0`;
}

const pointLineDistance: GeneratorDef = {
  id: 'point-line-distance',
  name: 'Distance from a point to a line',
  topic: 'geometry-algebra',
  subtopic: 'lines-circles',
  make(r) {
    const [p, q] = r.pick([[3, 4], [4, 3], [5, 12], [12, 5], [6, 8], [8, 6], [1, 1], [1, 2], [2, 1]] as [number, number][]);
    const A = p * (r.bool() ? 1 : -1);
    const B = q;
    const C = r.int(-10, 10);
    const x0 = r.int(-4, 4);
    const y0 = r.int(-4, 4);
    let num = Math.abs(A * x0 + B * y0 + C);
    if (num === 0) num = 0;
    const den2 = A * A + B * B;
    // distance = num / sqrt(den2) = num*sqrt(den2)/den2
    const tex = (n: number, d2: number) => {
      const s = Math.sqrt(d2);
      if (Number.isInteger(s)) return new Frac(n, s).tex();
      // n/sqrt(d2) = n sqrt(d2) / d2
      const g = gcd(n, d2);
      const nn = n / g;
      const dd = d2 / g;
      const root = sqrtTex(d2);
      if (n === 0) return '0';
      return dd === 1 ? `${nn === 1 ? '' : nn}${root}` : `\\frac{${nn === 1 ? '' : nn}${root}}{${dd}}`;
    };
    const ans = tex(num, den2);
    const signed = A * x0 + B * y0 + C;
    return {
      question: `The distance from the point ${m(pt(x0, y0))} to the line ${m(lineGeneralTex(A, B, C))} is`,
      correct: m(ans),
      distractors: [m(tex(Math.abs(A * x0 + B * y0), den2)), m(String(num)), m(tex(Math.abs(A * x0 + B * y0 - C), den2)), m(tex(num + 1, den2)), m(tex(num, (Math.abs(A) + Math.abs(B)) ** 2))],
      explanation: `${m('d=\\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}')} ${m(`=\\dfrac{|${A}\\cdot(${x0})+${B}\\cdot(${y0})+(${C})|}{\\sqrt{${A * A}+${B * B}}}=\\dfrac{${Math.abs(signed)}}{${sqrtTex(den2)}}=${ans}`)}.`,
      difficulty: Number.isInteger(Math.sqrt(den2)) ? 1 : 2,
      meta: { A, B, C, x0, y0, value: num / Math.sqrt(den2) },
    };
  },
};

const circleCenterRadius: GeneratorDef = {
  id: 'circle-center-radius',
  name: 'Circle centre and radius',
  topic: 'geometry-algebra',
  subtopic: 'lines-circles',
  make(r) {
    const a = r.nonzero(-5, 5);
    const b = r.int(-5, 5);
    const rad2 = r.pick([1, 4, 9, 16, 25, 2, 3, 5, 8]);
    const D = -2 * a;
    const E = -2 * b;
    const Fc = a * a + b * b - rad2;
    const terms = ['x^2+y^2'];
    if (D) terms.push(`${D > 0 ? '+' : '-'}${Math.abs(D)}x`);
    if (E) terms.push(`${E > 0 ? '+' : '-'}${Math.abs(E)}y`);
    if (Fc) terms.push(`${Fc > 0 ? '+' : '-'}${Math.abs(Fc)}`);
    const eq = `${terms.join('')}=0`;
    const opt = (x: number, y: number, rr: string) => `centre ${m(pt(x, y))}, radius ${m(rr)}`;
    const rTex = sqrtTex(rad2);
    return {
      question: `The circle ${m(eq)} has`,
      correct: opt(a, b, rTex),
      distractors: [opt(-a, -b, rTex), opt(a, b, String(rad2)), opt(-a, -b, String(rad2)), opt(b, a, rTex)],
      explanation: `Complete the square: ${m(`(${xMinus(a)})^2+(${xMinus(b, 'y')})^2=${rad2}`)}. So the centre is ${m(`\\left(-\\tfrac{D}{2},-\\tfrac{E}{2}\\right)=${pt(a, b)}`)} and the radius is ${m(`\\sqrt{${rad2}}=${rTex}`)}.`,
      difficulty: 1,
      meta: { a, b, rad2, D, E, F: Fc },
    };
  },
  fallback: (_r, res) => {
    const { a, b, rad2 } = res.meta as Record<string, number>;
    const opt = (x: number, y: number, rr: string) => `centre ${m(pt(x, y))}, radius ${m(rr)}`;
    return [opt(a, b, sqrtTex(rad2 + 1)), opt(-a, -b, sqrtTex(rad2 + 1)), opt(a, -b, sqrtTex(rad2)), opt(-a, b, sqrtTex(rad2)), opt(a, b, String(2 * rad2))];
  },
};

const ELLIPSES: [number, number][] = [
  [4, 3], [9, 5], [25, 16], [25, 9], [16, 12], [9, 8], [169, 144], [100, 64], [100, 36], [8, 4], [6, 2],
];

const ellipseParams: GeneratorDef = {
  id: 'ellipse-parameters',
  name: 'Ellipse: a, b, c, e, foci',
  topic: 'geometry-algebra',
  subtopic: 'conics',
  make(r) {
    const [a2, b2] = r.pick(ELLIPSES);
    const c2 = a2 - b2;
    const vertical = r.bool();
    const eq = vertical ? `\\dfrac{x^2}{${b2}}+\\dfrac{y^2}{${a2}}=1` : `\\dfrac{x^2}{${a2}}+\\dfrac{y^2}{${b2}}=1`;
    const ask = r.pick(['e', 'foci', 'major'] as const);
    const a = sqrtTex(a2);
    const c = sqrtTex(c2);
    // e = c/a = sqrt(c2/a2)
    const eTex = (num2: number, den2: number) => {
      const f = new Frac(num2, den2); // e^2
      const sn = Math.sqrt(f.n);
      const sd = Math.sqrt(f.d);
      if (Number.isInteger(sn) && Number.isInteger(sd)) return new Frac(sn, sd).tex();
      // sqrt(n/d) = sqrt(n d)/d
      const root = sqrtTex(f.n * f.d);
      return `\\frac{${root}}{${f.d}}`;
    };
    const foc = (cc: string, vert: boolean) => (vert ? `(0,\\pm ${cc})` : `(\\pm ${cc},0)`);
    let correct: string;
    let distractors: string[];
    if (ask === 'e') {
      correct = m(eTex(c2, a2));
      distractors = [m(eTex(b2, a2)), m(eTex(c2, b2)), m(eTex(a2 + b2, a2)), m(eTex(b2, c2 + b2 + a2))];
    } else if (ask === 'foci') {
      correct = m(foc(c, vertical));
      distractors = [m(foc(c, !vertical)), m(foc(sqrtTex(a2 + b2), vertical)), m(foc(sqrtTex(a2 + b2), !vertical)), m(foc(String(c2), vertical))];
    } else {
      correct = m(sqrtTex(4 * a2));
      distractors = [m(a), m(sqrtTex(4 * b2)), m(sqrtTex(4 * c2)), m(String(2 * a2))];
    }
    const what = ask === 'e' ? 'eccentricity' : ask === 'foci' ? 'foci' : 'length of the major axis';
    return {
      question: `For the ellipse ${m(eq)}, the ${what} ${ask === 'foci' ? 'are' : 'is'}`,
      correct,
      distractors,
      explanation: [
        `The larger denominator is ${m('a^2')}: ${m(`a^2=${a2},\\ b^2=${b2}`)}, and the major axis lies along the ${m(vertical ? 'y' : 'x')}-axis.`,
        `For an ellipse ${m('c^2=a^2-b^2')}: ${m(`c^2=${c2}`)}, ${m(`c=${c}`)}.`,
        ask === 'e'
          ? `${m(`e=\\dfrac{c}{a}=\\dfrac{${c}}{${a}}=${eTex(c2, a2)}`)}.`
          : ask === 'foci'
            ? `The foci lie on the major axis: ${m(foc(c, vertical))}.`
            : `Major axis length ${m(`=2a=${sqrtTex(4 * a2)}`)}.`,
      ].join('\n\n'),
      difficulty: ask === 'major' ? 1 : 2,
      meta: { a2, b2, vertical, ask },
    };
  },
};

const HYPERBOLAS: [number, number][] = [
  [9, 16], [16, 9], [4, 5], [1, 3], [36, 64], [25, 144], [144, 25], [1, 8], [4, 12], [3, 1], [5, 4], [4, 4],
];

const hyperbolaParams: GeneratorDef = {
  id: 'hyperbola-parameters',
  name: 'Hyperbola: e, foci, asymptotes',
  topic: 'geometry-algebra',
  subtopic: 'conics',
  make(r) {
    const [a2, b2] = r.pick(HYPERBOLAS);
    const c2 = a2 + b2;
    const vertical = r.bool();
    const eq = vertical ? `\\dfrac{y^2}{${a2}}-\\dfrac{x^2}{${b2}}=1` : `\\dfrac{x^2}{${a2}}-\\dfrac{y^2}{${b2}}=1`;
    const ask = r.pick(['e', 'foci', 'asymptote'] as const);
    const a = sqrtTex(a2);
    const c = sqrtTex(c2);
    const ratioTex = (n2: number, d2: number) => {
      const f = new Frac(n2, d2);
      const sn = Math.sqrt(f.n);
      const sd = Math.sqrt(f.d);
      if (Number.isInteger(sn) && Number.isInteger(sd)) return new Frac(sn, sd).tex();
      const root = sqrtTex(f.n * f.d);
      return `\\frac{${root}}{${f.d}}`;
    };
    const asym = (n2: number, d2: number) => {
      const t = ratioTex(n2, d2);
      return `y=\\pm ${t === '1' ? '' : t}x`;
    };
    let correct: string;
    let distractors: string[];
    if (ask === 'e') {
      correct = m(ratioTex(c2, a2));
      distractors = [m(ratioTex(c2, b2)), m(ratioTex(Math.abs(a2 - b2) || 1, a2)), m(ratioTex(b2, a2)), m(ratioTex(a2, c2))];
    } else if (ask === 'foci') {
      const foc = (cc: string, vert: boolean) => (vert ? `(0,\\pm ${cc})` : `(\\pm ${cc},0)`);
      correct = m(foc(c, vertical));
      distractors = [m(foc(c, !vertical)), m(foc(sqrtTex(Math.abs(a2 - b2) || 2), vertical)), m(foc(a, vertical)), m(foc(String(c2), vertical))];
    } else {
      // horizontal: y = ±(b/a)x ; vertical: y = ±(a/b)x
      correct = m(vertical ? asym(a2, b2) : asym(b2, a2));
      distractors = [m(vertical ? asym(b2, a2) : asym(a2, b2)), m(asym(c2, a2)), m(asym(b2 * b2, a2 * a2 + 1)), m(asym(a2, c2))];
    }
    const what = ask === 'e' ? 'eccentricity is' : ask === 'foci' ? 'foci are' : 'asymptotes are';
    return {
      question: `For the hyperbola ${m(eq)}, the ${what}`,
      correct,
      distractors,
      explanation: [
        `The positive term gives ${m('a^2')}: ${m(`a^2=${a2},\\ b^2=${b2}`)}; the transverse axis is the ${m(vertical ? 'y' : 'x')}-axis.`,
        `For a hyperbola ${m('c^2=a^2+b^2')} (plus, not minus): ${m(`c^2=${c2}`)}, ${m(`c=${c}`)}.`,
        ask === 'e'
          ? `${m(`e=\\dfrac{c}{a}=${ratioTex(c2, a2)}`)} (always ${m('e>1')} for a hyperbola).`
          : ask === 'foci'
            ? `Foci on the transverse axis: ${correct}.`
            : `Set the right-hand side to 0: ${m(vertical ? `\\dfrac{y^2}{${a2}}=\\dfrac{x^2}{${b2}}` : `\\dfrac{x^2}{${a2}}=\\dfrac{y^2}{${b2}}`)}, giving ${correct}.`,
      ].join('\n\n'),
      difficulty: 2,
      meta: { a2, b2, vertical, ask },
    };
  },
};

const parabolaFocus: GeneratorDef = {
  id: 'parabola-focus',
  name: 'Parabola focus and directrix',
  topic: 'geometry-algebra',
  subtopic: 'conics',
  make(r) {
    const k = r.pick([2, 4, 6, 8, 12, 16, 1, 3]) * (r.bool() ? 1 : -1); // y^2 = kx or x^2 = ky
    const onX = r.bool(); // y^2 = kx (axis = x-axis)
    const ask = r.pick(['focus', 'directrix'] as const);
    const p4 = new Frac(k, 4);
    const eq = onX ? `y^2=${k}x` : `x^2=${k}y`;
    const focus = (f: Frac, xAxis: boolean) => (xAxis ? `\\left(${f.tex()},0\\right)` : `\\left(0,${f.tex()}\\right)`);
    const dir = (f: Frac, xAxis: boolean) => (xAxis ? `x=${f.tex()}` : `y=${f.tex()}`);
    let correct: string;
    let distractors: string[];
    if (ask === 'focus') {
      correct = m(focus(p4, onX));
      distractors = [m(focus(p4.neg(), onX)), m(focus(new Frac(k, 2), onX)), m(focus(p4, !onX)), m(focus(new Frac(k), onX))];
    } else {
      correct = m(dir(p4.neg(), onX));
      distractors = [m(dir(p4, onX)), m(dir(new Frac(-k, 2), onX)), m(dir(p4.neg(), !onX)), m(dir(new Frac(k, 2), onX))];
    }
    return {
      question: `The ${ask} of the parabola ${m(eq)} ${ask === 'focus' ? 'is' : 'has equation'}`,
      correct,
      distractors,
      explanation: `Compare with ${m(onX ? 'y^2=4px' : 'x^2=4py')}: ${m(`4p=${k}`)}, so ${m(`p=${p4.tex()}`)}. The focus is ${m(focus(p4, onX))} and the directrix is ${m(dir(p4.neg(), onX))}. (Common slip: using ${m(`\\tfrac{${k}}{2}`)} instead of ${m(`\\tfrac{${k}}{4}`)}.)`,
      difficulty: k < 0 || !onX ? 2 : 1,
      meta: { k, onX, ask, p: p4.value() },
    };
  },
};

const dotProduct: GeneratorDef = {
  id: 'dot-product',
  name: 'Dot product and perpendicular vectors',
  topic: 'geometry-algebra',
  subtopic: 'vectors',
  make(r) {
    const a: [number, number] = [r.nonzero(-4, 4), r.int(-4, 4)];
    const b: [number, number] = [r.int(-4, 4), r.nonzero(-4, 4)];
    const variant = r.int(0, 2);
    if (variant === 0) {
      const ans = a[0] * b[0] + a[1] * b[1];
      return {
        question: `Given ${m(`\\vec a=${pt(...a)}`)} and ${m(`\\vec b=${pt(...b)}`)}, find ${m('\\vec a\\cdot\\vec b')}.`,
        correct: m(String(ans)),
        distractors: [m(String(a[0] * b[1] + a[1] * b[0])), m(String(a[0] * b[1] - a[1] * b[0])), m(String(-ans)), m(String(a[0] * b[0] - a[1] * b[1]))],
        explanation: `${m(`\\vec a\\cdot\\vec b=x_1x_2+y_1y_2=(${a[0]})(${b[0]})+(${a[1]})(${b[1]})=${ans}`)}.`,
        difficulty: 1,
        meta: { variant, a, b, value: ans },
      };
    }
    if (variant === 1) {
      // (a + t b) · b? keep (2a - b)·a
      const u: [number, number] = [2 * a[0] - b[0], 2 * a[1] - b[1]];
      const ans = u[0] * a[0] + u[1] * a[1];
      const wrong1 = 2 * (a[0] * a[0] + a[1] * a[1]) + (a[0] * b[0] + a[1] * b[1]);
      return {
        question: `Given ${m(`\\vec a=${pt(...a)}`)} and ${m(`\\vec b=${pt(...b)}`)}, find ${m('(2\\vec a-\\vec b)\\cdot\\vec a')}.`,
        correct: m(String(ans)),
        distractors: [m(String(wrong1)), m(String(u[0] * b[0] + u[1] * b[1])), m(String(-ans)), m(String(ans + 2))],
        explanation: `${m(`2\\vec a-\\vec b=${pt(...u)}`)}, so ${m(`(2\\vec a-\\vec b)\\cdot\\vec a=(${u[0]})(${a[0]})+(${u[1]})(${a[1]})=${ans}`)}. (Equivalently ${m('2|\\vec a|^2-\\vec a\\cdot\\vec b')}.)`,
        difficulty: 2,
        meta: { variant, a, b, value: ans },
      };
    }
    // find m with a ⊥ (m, b1): a0*m + a1*b1 = 0
    const t = b[1];
    const ansF = new Frac(-a[1] * t, a[0]);
    const parallel = new Frac(a[1] === 0 ? 1 : a[0] * t, a[1] === 0 ? 1 : a[1]); // m with a ∥ (m,t): a0*t = a1*m
    return {
      question: `Given ${m(`\\vec a=${pt(...a)}`)} and ${m(`\\vec b=(m,${t})`)}. If ${m('\\vec a\\perp\\vec b')}, then ${m('m=')}`,
      correct: m(ansF.tex()),
      distractors: [m(ansF.neg().tex()), m(parallel.tex()), m(new Frac(a[0] * t, a[1] || 1).neg().tex()), m(ansF.add(1).tex())],
      explanation: `Perpendicular means the dot product is zero: ${m(`${a[0]}m+(${a[1]})(${t})=0`)}, so ${m(`m=${ansF.tex()}`)}. (Do not confuse with the parallel condition ${m('x_1y_2-x_2y_1=0')}.)`,
      difficulty: 1,
      meta: { variant, a, t, value: ansF.value() },
    };
  },
};

// angle cases: [cos value as tex, angle numerator k for kπ/12]
const vectorAngle: GeneratorDef = {
  id: 'vector-angle',
  name: 'Angle between vectors',
  topic: 'geometry-algebra',
  subtopic: 'vectors',
  make(r) {
    const angles: [number, number][] = [[1, 6], [1, 4], [1, 3], [1, 2], [2, 3], [3, 4], [5, 6]]; // kπ/den
    const [k, den] = r.pick(angles);
    const theta = (k * Math.PI) / den;
    const useCoords = den === 4 || den === 2 ? r.bool() : false;
    let question: string;
    let how: string;
    let meta: Record<string, unknown>;
    if (useCoords) {
      // integer vectors at 45°, 90°, 135°, rotated by a random multiple of 90° and scaled
      const s1 = r.int(1, 3);
      const s2 = r.int(1, 2);
      const base: [number, number] = [s1, 0];
      const other: [number, number] = den === 2 ? [0, s2] : k === 1 ? [s2, s2] : [-s2, s2];
      const rot = r.int(0, 3);
      const R = (v: [number, number]): [number, number] => {
        let [x, y] = v;
        for (let i = 0; i < rot; i++) [x, y] = [-y, x];
        return [x, y];
      };
      const a = R(base);
      const b = R(other);
      const dot = a[0] * b[0] + a[1] * b[1];
      question = `The angle between ${m(`\\vec a=${pt(...a)}`)} and ${m(`\\vec b=${pt(...b)}`)} is`;
      how = `${m(`\\cos\\theta=\\dfrac{\\vec a\\cdot\\vec b}{|\\vec a||\\vec b|}=\\dfrac{${dot}}{${sqrtTex(a[0] ** 2 + a[1] ** 2)}\\cdot ${sqrtTex(b[0] ** 2 + b[1] ** 2)}}`)} ${m(`=${dot === 0 ? '0' : Math.cos(theta) > 0 ? '\\frac{\\sqrt2}{2}' : '-\\frac{\\sqrt2}{2}'}`)}.`;
      meta = { a, b, theta };
    } else {
      const ma = r.int(1, 4);
      const mb = r.int(1, 4);
      // cos θ = sign·sqrt(root)/2  (sign 0 means cos θ = 0)
      const COS: Record<string, [number, number]> = { '1/6': [1, 3], '1/4': [1, 2], '1/3': [1, 1], '1/2': [0, 0], '2/3': [-1, 1], '3/4': [-1, 2], '5/6': [-1, 3] };
      const [sign, root] = COS[`${k}/${den}`];
      const dotNum = Math.cos(theta) * ma * mb;
      const dotTex = sign === 0 ? '0' : root === 1 ? new Frac(sign * ma * mb, 2).tex() : `${sign < 0 ? '-' : ''}${fracRoot(ma * mb, root, 2)}`;
      question = `Given ${m(`|\\vec a|=${ma}`)}, ${m(`|\\vec b|=${mb}`)} and ${m(`\\vec a\\cdot\\vec b=${dotTex}`)}, the angle between ${m('\\vec a')} and ${m('\\vec b')} is`;
      how = `${m(`\\cos\\theta=\\dfrac{\\vec a\\cdot\\vec b}{|\\vec a||\\vec b|}=\\dfrac{${dotTex}}{${ma * mb}}`)}, and ${m('\\theta\\in[0,\\pi]')}.`;
      meta = { ma, mb, dot: dotNum, theta };
    }
    const correct = m(piTex(k, den));
    const supplement = m(piTex(den - k, den));
    const all = angles.map(([kk, dd]) => m(piTex(kk, dd)));
    return {
      question,
      correct,
      distractors: [supplement, ...r.shuffle(all)],
      explanation: `${how} So ${m(`\\theta=${piTex(k, den)}`)}. Remember the angle between vectors lies in ${m('[0,\\pi]')}; a negative cosine means an obtuse angle.`,
      difficulty: 2,
      meta: { ...meta, k, den },
    };
  },
};

/** (n/den)·sqrt(root) as LaTeX */
function fracRoot(n: number, root: number, den: number): string {
  const f = new Frac(n, den);
  const num = f.n === 1 ? `\\sqrt{${root}}` : `${f.n}\\sqrt{${root}}`;
  return f.d === 1 ? num : `\\frac{${num}}{${f.d}}`;
}

/** a + bi as LaTeX */
export function cTex(re: Frac | number, im: Frac | number): string {
  const a = Frac.of(re);
  const b = Frac.of(im);
  if (b.n === 0) return a.tex();
  const bAbs = new Frac(Math.abs(b.n), b.d);
  const bPart = bAbs.eq(1) ? 'i' : bAbs.isInt() ? `${bAbs.tex()}i` : `${bAbs.tex()}i`;
  if (a.n === 0) return `${b.n < 0 ? '-' : ''}${bPart}`;
  return `${a.tex()}${b.n < 0 ? '-' : '+'}${bPart}`;
}

const complexArithmetic: GeneratorDef = {
  id: 'complex-arithmetic',
  name: 'Complex number arithmetic',
  topic: 'geometry-algebra',
  subtopic: 'complex-numbers',
  make(r) {
    const variant = r.int(0, 2);
    if (variant === 0) {
      const a = r.nonzero(-4, 4), b = r.nonzero(-4, 4), c = r.nonzero(-3, 3), d = r.nonzero(-3, 3);
      const re = a * c - b * d;
      const im = a * d + b * c;
      return {
        question: `${m(`(${cTex(a, b)})(${cTex(c, d)})=`)}`,
        correct: m(cTex(re, im)),
        distractors: [m(cTex(a * c + b * d, im)), m(cTex(a * c, b * d)), m(cTex(re, -im)), m(cTex(a * c + b * d, a * d - b * c))],
        explanation: `Expand and use ${m('i^2=-1')}: ${m(`(${cTex(a, b)})(${cTex(c, d)})=${a * c}+${a * d === 0 ? '' : `(${a * d})i`}+(${b * c})i+(${b * d})i^2=${cTex(re, im)}`)}.`,
        difficulty: 1,
        meta: { variant, a, b, c, d, re, im },
      };
    }
    if (variant === 1) {
      // z = w * q, ask z / w
      const qa = r.int(-3, 3), qb = r.nonzero(-3, 3);
      const [wa, wb] = r.pick([[1, 1], [1, -1], [1, 2], [2, -1], [2, 1], [1, -2]] as [number, number][]);
      const za = qa * wa - qb * wb;
      const zb = qa * wb + qb * wa;
      return {
        question: `${m(`\\dfrac{${cTex(za, zb)}}{${cTex(wa, wb)}}=`)}`,
        correct: m(cTex(qa, qb)),
        distractors: [m(cTex(qa, -qb)), m(cTex(-qa, qb)), m(cTex(qb, qa)), m(cTex(new Frac(za, wa), new Frac(zb, wb)))],
        explanation: `Multiply top and bottom by the conjugate ${m(cTex(wa, -wb))}: the denominator becomes ${m(`${wa}^2+${wb}^2=${wa * wa + wb * wb}`)}, the numerator ${m(`(${cTex(za, zb)})(${cTex(wa, -wb)})=${cTex(qa * (wa * wa + wb * wb), qb * (wa * wa + wb * wb))}`)}. Dividing gives ${m(cTex(qa, qb))}.`,
        difficulty: 2,
        meta: { variant, za, zb, wa, wb, re: qa, im: qb },
      };
    }
    const n = r.int(5, 2027);
    const rem = n % 4;
    const vals = ['1', 'i', '-1', '-i'];
    return {
      question: `${m(`i^{${n}}=`)}`,
      correct: m(vals[rem]),
      distractors: vals.filter((_, i) => i !== rem).map((v) => m(v)),
      explanation: `Powers of ${m('i')} repeat with period 4: ${m('i^1=i,\\ i^2=-1,\\ i^3=-i,\\ i^4=1')}. Since ${m(`${n}=4\\cdot${Math.floor(n / 4)}+${rem}`)}, ${m(`i^{${n}}=i^{${rem}}=${vals[rem]}`)}.`,
      difficulty: 1,
      meta: { variant, n, re: [1, 0, -1, 0][rem], im: [0, 1, 0, -1][rem] },
    };
  },
};

const complexModulus: GeneratorDef = {
  id: 'complex-modulus',
  name: 'Modulus of a complex number',
  topic: 'geometry-algebra',
  subtopic: 'complex-numbers',
  make(r) {
    const [p, q] = r.pick([[3, 4], [5, 12], [6, 8], [1, 1], [1, 2], [2, 3], [8, 15]] as [number, number][]);
    const a = p * (r.bool() ? 1 : -1);
    const b = q * (r.bool() ? 1 : -1);
    const quotient = r.bool();
    const mod2 = a * a + b * b;
    if (!quotient) {
      return {
        question: `If ${m(`z=${cTex(a, b)}`)}, then ${m('|z|=')}`,
        correct: m(sqrtTex(mod2)),
        distractors: [m(String(mod2)), m(String(Math.abs(a) + Math.abs(b))), m(sqrtTex(Math.abs(a * a - b * b) || 2)), m(String(Math.abs(a + b)))],
        explanation: `${m(`|a+bi|=\\sqrt{a^2+b^2}=\\sqrt{${a * a}+${b * b}}=${sqrtTex(mod2)}`)}.`,
        difficulty: 1,
        meta: { a, b, value: Math.sqrt(mod2) },
      };
    }
    const [wa, wb] = r.pick([[1, 1], [1, -1], [1, 2], [2, 1], [1, 3]] as [number, number][]);
    const w2 = wa * wa + wb * wb;
    // |z/w| = sqrt(mod2 / w2)
    const f = new Frac(mod2, w2);
    const ansTex = (() => {
      const sn = Math.sqrt(f.n), sd = Math.sqrt(f.d);
      if (Number.isInteger(sn) && Number.isInteger(sd)) return new Frac(sn, sd).tex();
      const root = sqrtTex(f.n * f.d);
      return f.d === 1 ? root : `\\frac{${root}}{${f.d}}`;
    })();
    return {
      question: `${m(`\\left|\\dfrac{${cTex(a, b)}}{${cTex(wa, wb)}}\\right|=`)}`,
      correct: m(ansTex),
      distractors: [m(f.tex()), m(sqrtTex(mod2)), m(new Frac(Math.abs(a) + Math.abs(b), Math.abs(wa) + Math.abs(wb)).tex()), m(sqrtTex(mod2 * w2))],
      explanation: `Use ${m('\\left|\\dfrac{z_1}{z_2}\\right|=\\dfrac{|z_1|}{|z_2|}')}: ${m(`\\dfrac{\\sqrt{${mod2}}}{\\sqrt{${w2}}}=${ansTex}`)}. No need to divide first.`,
      difficulty: 2,
      meta: { a, b, wa, wb, value: Math.sqrt(mod2 / w2) },
    };
  },
};

const distance3d: GeneratorDef = {
  id: 'distance-3d',
  name: 'Distance in 3D coordinates',
  topic: 'geometry-algebra',
  subtopic: 'solid-geometry',
  make(r) {
    const nice = r.pick([[1, 2, 2], [2, 3, 6], [1, 4, 8], [4, 4, 7], [2, 6, 9], [2, 1, 2], [1, 1, 1], [1, 2, 3], [2, 2, 1], [3, 1, 2]] as [number, number, number][]);
    const d = r.shuffle(nice).map((v) => v * (r.bool() ? 1 : -1));
    const A = [r.int(-3, 3), r.int(-3, 3), r.int(-3, 3)];
    const B = A.map((v, i) => v + d[i]);
    const s2 = d.reduce((s, v) => s + v * v, 0);
    const p3 = (v: number[]) => `(${v.join(',')})`;
    return {
      question: `In a space rectangular coordinate system, the distance between ${m(`A${p3(A)}`)} and ${m(`B${p3(B)}`)} is`,
      correct: m(sqrtTex(s2)),
      distractors: [m(String(s2)), m(sqrtTex(d[0] ** 2 + d[1] ** 2)), m(String(d.reduce((s, v) => s + Math.abs(v), 0))), m(sqrtTex(A.reduce((s, v, i) => s + (v + B[i]) ** 2, 0) || 3))],
      explanation: `${m(`|AB|=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}=\\sqrt{${d.map((v) => (v < 0 ? `(${v})^2` : `${v}^2`)).join('+')}}=${sqrtTex(s2)}`)}.`,
      difficulty: 1,
      meta: { A, B, value: Math.sqrt(s2) },
    };
  },
};

export const geometryGenerators = [pointLineDistance, circleCenterRadius, ellipseParams, hyperbolaParams, parabolaFocus, dotProduct, vectorAngle, complexArithmetic, complexModulus, distance3d];
