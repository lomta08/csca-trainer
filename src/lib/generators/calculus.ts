import type { GeneratorDef } from './core';
import { m, polyTex, polyEval, polyDeriv } from './format';

/** y = mx + c as LaTeX */
export function lineTex(slope: number, c: number): string {
  const sl = slope === 0 ? '' : slope === 1 ? 'x' : slope === -1 ? '-x' : `${slope}x`;
  if (!sl) return `y=${c}`;
  if (c === 0) return `y=${sl}`;
  return `y=${sl}${c > 0 ? '+' : '-'}${Math.abs(c)}`;
}

const derivativeAtPoint: GeneratorDef = {
  id: 'derivative-at-point',
  name: 'Derivative at a point',
  topic: 'functions',
  subtopic: 'derivatives',
  make(r) {
    const a = r.nonzero(-3, 3);
    const b = r.int(-4, 4);
    const c = r.int(-6, 6);
    const d = r.int(-5, 5);
    const coeffs = [a, b, c, d];
    const x0 = r.nonzero(-3, 3);
    const dc = polyDeriv(coeffs);
    const ans = polyEval(dc, x0);
    const noPowerDown = polyEval([a, b, c], x0); // forgot to multiply by the power
    const fVal = polyEval(coeffs, x0);
    const keptConst = ans + d;
    return {
      question: `Let ${m(`f(x)=${polyTex(coeffs)}`)}. Then ${m(`f'(${x0})=`)}`,
      correct: m(String(ans)),
      distractors: [m(String(noPowerDown)), m(String(fVal)), m(String(keptConst)), m(String(-ans)), m(String(polyEval(dc, -x0)))],
      explanation: `Differentiate term by term with ${m("(x^n)'=nx^{n-1}")}: ${m(`f'(x)=${polyTex(dc)}`)}. Substituting ${m(`x=${x0}`)}: ${m(`f'(${x0})=${ans}`)}.`,
      difficulty: 1,
      meta: { coeffs, x0, value: ans },
    };
  },
};

const tangentLine: GeneratorDef = {
  id: 'tangent-line',
  name: 'Tangent line equation',
  topic: 'functions',
  subtopic: 'derivatives',
  make(r) {
    const cubic = r.bool();
    const coeffs = cubic ? [r.nonzero(-2, 2), r.int(-3, 3), r.int(-4, 4), r.int(-4, 4)] : [r.nonzero(-3, 3), r.int(-5, 5), r.int(-5, 5)];
    const x0 = r.int(-2, 2);
    const y0 = polyEval(coeffs, x0);
    const k = polyEval(polyDeriv(coeffs), x0);
    const c = y0 - k * x0;
    const correct = m(lineTex(k, c));
    return {
      question: `The equation of the tangent line to the curve ${m(`y=${polyTex(coeffs)}`)} at the point ${m(`(${x0},${y0})`)} is`,
      correct,
      distractors: [m(lineTex(k, y0 + k * x0)), m(lineTex(y0 === k ? k + 1 : y0, c)), m(lineTex(k, y0)), m(lineTex(-k, y0 + k * x0)), m(lineTex(k, c + 1))],
      explanation: `Slope = ${m(`y'|_{x=${x0}}`)}: ${m(`y'=${polyTex(polyDeriv(coeffs))}`)}, so ${m(`k=${k}`)}. Point-slope form: ${m(`y-(${y0})=${k}(x-(${x0}))`)}, which simplifies to ${correct}.`,
      difficulty: cubic ? 2 : 1,
      meta: { coeffs, x0, y0, slope: k, intercept: c },
    };
  },
  fallback: (_r, res) => {
    const { slope, intercept } = res.meta as Record<string, number>;
    return [m(lineTex(slope + 1, intercept)), m(lineTex(slope, intercept - 1)), m(lineTex(-slope, intercept)), m(lineTex(slope - 1, intercept + 1)), m(lineTex(slope, -intercept + 2))];
  },
};

const cubicExtrema: GeneratorDef = {
  id: 'cubic-extrema',
  name: 'Extreme values of a cubic',
  topic: 'functions',
  subtopic: 'derivatives',
  make(r) {
    // f'(x) = 3(x-p)(x-q) with p+q even so that coefficients are integers
    let p = r.int(-3, 3);
    let q = r.int(-3, 3);
    while (q === p || (p + q) % 2 !== 0) q = r.int(-3, 3);
    if (p > q) [p, q] = [q, p];
    const d = r.int(-5, 5);
    const coeffs = [1, (-3 * (p + q)) / 2, 3 * p * q, d];
    const f = (x: number) => polyEval(coeffs, x);
    const wantMax = r.bool();
    // leading coefficient 1 > 0: local max at the smaller critical point p, local min at q
    const ans = wantMax ? f(p) : f(q);
    const other = wantMax ? f(q) : f(p);
    return {
      question: `The ${wantMax ? 'local maximum' : 'local minimum'} value of ${m(`f(x)=${polyTex(coeffs)}`)} is`,
      correct: m(String(ans)),
      distractors: [m(String(other)), m(String(wantMax ? p : q)), m(String(f(0) === ans ? ans + 2 : f(0))), m(String(-ans))],
      explanation: [
        `${m(`f'(x)=${polyTex(polyDeriv(coeffs))}=3(${p === 0 ? 'x' : `x${p > 0 ? '-' : '+'}${Math.abs(p)}`})(${q === 0 ? 'x' : `x${q > 0 ? '-' : '+'}${Math.abs(q)}`})`)}, so the critical points are ${m(`x=${p}`)} and ${m(`x=${q}`)}.`,
        `${m("f'")} is positive for ${m(`x<${p}`)}, negative on ${m(`(${p},${q})`)} and positive for ${m(`x>${q}`)}. So ${m('f')} has a local maximum at ${m(`x=${p}`)} and a local minimum at ${m(`x=${q}`)}.`,
        `${wantMax ? `Local maximum value: ${m(`f(${p})=${f(p)}`)}` : `Local minimum value: ${m(`f(${q})=${f(q)}`)}`}. (Careful: the question asks for the *value* ${m('f(x)')}, not the point ${m('x')}.)`,
      ].join('\n\n'),
      difficulty: 2,
      meta: { coeffs, wantMax, value: ans },
    };
  },
};

export const calculusGenerators = [derivativeAtPoint, tangentLine, cubicExtrema];
