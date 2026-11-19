// Test helpers: evaluate the small LaTeX subset that generators emit, independently of the generators.

/** Strip $…$ and \left/\right. */
export function strip(s: string): string {
  return s.replace(/\$/g, '').replace(/\\left|\\right/g, '').replace(/\\dfrac|\\tfrac/g, '\\frac').trim();
}

/** Evaluate a numeric LaTeX expression like -\frac{3\sqrt{2}}{4}, 2\pi/3, \lg 5. */
export function evalTex(tex: string): number {
  let s = strip(tex);
  // \frac{a}{b} → ((a)/(b)), innermost first
  const fracRe = /\\frac\{([^{}]*)\}\{([^{}]*)\}/;
  const sqrtRe = /\\sqrt\{([^{}]*)\}/;
  for (let guard = 0; guard < 50; guard++) {
    const before = s;
    s = s.replace(sqrtRe, 'Math.sqrt($1)').replace(fracRe, '(($1)/($2))');
    if (s === before) break;
  }
  s = s.replace(/\\sqrt(\d)/g, 'Math.sqrt($1)');
  s = s.replace(/\\lg\s*([\d.]+)/g, 'Math.log10($1)');
  s = s.replace(/\\pi/g, 'Math.PI');
  s = s.replace(/\\cdot|\\times/g, '*');
  // implicit multiplication: 2Math.sqrt / 3Math.PI / )(
  s = s.replace(/(\d|\))\s*(Math\.|\()/g, '$1*$2');
  s = s.replace(/\s+/g, '');
  if (!/^[-+*/().\d\sMathsqrtPIlog10e]*$/.test(s)) throw new Error(`cannot evaluate: ${tex} → ${s}`);
  // eslint-disable-next-line no-new-func
  return Function(`"use strict";return (${s});`)() as number;
}

export function tryEval(tex: string): number | null {
  try {
    const v = evalTex(tex);
    return Number.isFinite(v) ? v : null;
  } catch {
    return null;
  }
}

export interface PIv {
  lo: number;
  hi: number;
  loC: boolean;
  hiC: boolean;
}

/** Parse interval unions like (-\infty,1)\cup[3,+\infty), \varnothing, \mathbb{R}. */
export function parseIntervals(tex: string): PIv[] {
  const s = strip(tex).replace(/\s/g, '');
  if (s === '\\varnothing') return [];
  if (s === '\\mathbb{R}') return [{ lo: -Infinity, hi: Infinity, loC: false, hiC: false }];
  return s.split('\\cup').map((part) => {
    const mm = /^([[(])(.+),(.+)([\])])$/.exec(part);
    if (!mm) throw new Error(`bad interval ${part}`);
    const num = (x: string) => (x === '-\\infty' ? -Infinity : x === '+\\infty' ? Infinity : evalTex(x));
    return { lo: num(mm[2]), hi: num(mm[3]), loC: mm[1] === '[', hiC: mm[4] === ']' };
  });
}

export function member(ivs: PIv[], x: number): boolean {
  return ivs.some((i) => (x > i.lo || (i.loC && x === i.lo)) && (x < i.hi || (i.hiC && x === i.hi)));
}

/** Sample points: all quarter-integers in [-12, 12]. Endpoints in generators are integers. */
export const GRID: number[] = Array.from({ length: 97 }, (_, i) => -12 + i * 0.25);

/** Parse a+bi forms produced by cTex. */
export function parseComplex(tex: string): [number, number] {
  const s = strip(tex).replace(/\s/g, '');
  const mm = /^(.*?)([+-]?(?:\\frac\{\d+\}\{\d+\}|\d*)?)i$/.exec(s);
  if (!s.endsWith('i')) return [evalTex(s), 0];
  if (!mm) throw new Error(`bad complex ${tex}`);
  const re = mm[1] === '' ? 0 : evalTex(mm[1]);
  let imStr = mm[2];
  if (imStr === '' || imStr === '+') imStr = '1';
  if (imStr === '-') imStr = '-1';
  return [re, evalTex(imStr)];
}

export function close(a: number, b: number, eps = 1e-6): boolean {
  return Math.abs(a - b) < eps * Math.max(1, Math.abs(a), Math.abs(b));
}

/** Standard normal CDF via erf approximation (Abramowitz–Stegun 7.1.26, error < 1.5e-7). */
export function phi(z: number): number {
  const t = 1 / (1 + 0.3275911 * Math.abs(z / Math.SQRT2));
  const y = 1 - ((((1.061405429 * t - 1.453152027) * t + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-(z * z) / 2);
  return z >= 0 ? 0.5 * (1 + y) : 0.5 * (1 - y);
}

export function invPhi(p: number): number {
  let lo = -10, hi = 10;
  for (let i = 0; i < 200; i++) {
    const mid = (lo + hi) / 2;
    if (phi(mid) < p) lo = mid;
    else hi = mid;
  }
  return (lo + hi) / 2;
}
