// Exact-arithmetic and LaTeX formatting helpers shared by the generators.

export function gcd(a: number, b: number): number {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b) [a, b] = [b, a % b];
  return a || 1;
}

/** Exact rational number with integer numerator/denominator. */
export class Frac {
  readonly n: number;
  readonly d: number;
  constructor(n: number, d = 1) {
    if (d === 0) throw new Error('zero denominator');
    if (d < 0) {
      n = -n;
      d = -d;
    }
    const g = gcd(n, d);
    this.n = n / g;
    this.d = d / g;
  }
  static of(x: number | Frac): Frac {
    return x instanceof Frac ? x : new Frac(x);
  }
  add(o: number | Frac): Frac {
    const b = Frac.of(o);
    return new Frac(this.n * b.d + b.n * this.d, this.d * b.d);
  }
  sub(o: number | Frac): Frac {
    const b = Frac.of(o);
    return new Frac(this.n * b.d - b.n * this.d, this.d * b.d);
  }
  mul(o: number | Frac): Frac {
    const b = Frac.of(o);
    return new Frac(this.n * b.n, this.d * b.d);
  }
  div(o: number | Frac): Frac {
    const b = Frac.of(o);
    return new Frac(this.n * b.d, this.d * b.n);
  }
  neg(): Frac {
    return new Frac(-this.n, this.d);
  }
  eq(o: number | Frac): boolean {
    const b = Frac.of(o);
    return this.n === b.n && this.d === b.d;
  }
  isInt(): boolean {
    return this.d === 1;
  }
  value(): number {
    return this.n / this.d;
  }
  /** LaTeX, e.g. -\frac{3}{4} */
  tex(): string {
    if (this.d === 1) return String(this.n);
    const sign = this.n < 0 ? '-' : '';
    return `${sign}\\frac{${Math.abs(this.n)}}{${this.d}}`;
  }
}

export const F = (n: number, d = 1) => new Frac(n, d);

/** Wrap in inline math. */
export const m = (s: string) => `$${s}$`;

/** Simplify sqrt(n) → [outside, inside] with n = outside² · inside. */
export function simplifySqrt(n: number): [number, number] {
  let out = 1;
  let inside = n;
  for (let k = 2; k * k <= inside; k++) {
    while (inside % (k * k) === 0) {
      inside /= k * k;
      out *= k;
    }
  }
  return [out, inside];
}

/** LaTeX for sqrt(n), simplified (e.g. 2\sqrt{3}). */
export function sqrtTex(n: number): string {
  if (n < 0) throw new Error('negative sqrt');
  const [o, i] = simplifySqrt(n);
  if (i === 1) return String(o);
  return o === 1 ? `\\sqrt{${i}}` : `${o}\\sqrt{${i}}`;
}

/** LaTeX for (p/q)·sqrt(r) in simplest form. */
export function fracSqrtTex(p: number, q: number, r: number): string {
  const [o, i] = simplifySqrt(r);
  const f = new Frac(p * o, q);
  if (i === 1) return f.tex();
  if (f.n === 0) return '0';
  const sign = f.n < 0 ? '-' : '';
  const num = Math.abs(f.n) === 1 ? `\\sqrt{${i}}` : `${Math.abs(f.n)}\\sqrt{${i}}`;
  return f.d === 1 ? `${sign}${num}` : `${sign}\\frac{${num}}{${f.d}}`;
}

/**
 * Polynomial in x from coefficients (highest power first), e.g. [1,-3,2] → x^2-3x+2.
 */
export function polyTex(coeffs: number[], v = 'x'): string {
  const deg = coeffs.length - 1;
  let s = '';
  coeffs.forEach((c, i) => {
    const p = deg - i;
    if (c === 0) return;
    const abs = Math.abs(c);
    const sign = c < 0 ? '-' : s ? '+' : '';
    let coef = abs === 1 && p > 0 ? '' : String(abs);
    const varPart = p === 0 ? '' : p === 1 ? v : `${v}^{${p}}`;
    if (p === 0) coef = String(abs);
    s += `${sign}${coef}${varPart}`;
  });
  return s || '0';
}

/** Evaluate polynomial (highest power first). */
export function polyEval(coeffs: number[], x: number): number {
  return coeffs.reduce((acc, c) => acc * x + c, 0);
}

export function polyDeriv(coeffs: number[]): number[] {
  const deg = coeffs.length - 1;
  return coeffs.slice(0, -1).map((c, i) => c * (deg - i));
}

/** "+ 3" / "- 3" style term for building expressions like x - 3. */
export function signed(n: number | Frac, withSpace = false): string {
  const f = Frac.of(n);
  const sp = withSpace ? ' ' : '';
  if (f.n < 0) return `${sp}-${sp}${f.neg().tex()}`;
  return `${sp}+${sp}${f.tex()}`;
}

/** x - a written nicely: a=3 → x-3, a=-2 → x+2, a=0 → x */
export function xMinus(a: number, v = 'x'): string {
  if (a === 0) return v;
  return a > 0 ? `${v}-${a}` : `${v}+${-a}`;
}

// ---- intervals -----------------------------------------------------------

export interface Interval {
  lo: number; // -Infinity allowed
  hi: number; // Infinity allowed
  loC: boolean; // closed at lo
  hiC: boolean; // closed at hi
}

export const iv = (lo: number, hi: number, loC: boolean, hiC: boolean): Interval => ({ lo, hi, loC: isFinite(lo) && loC, hiC: isFinite(hi) && hiC });

function endTex(x: number): string {
  if (x === -Infinity) return '-\\infty';
  if (x === Infinity) return '+\\infty';
  return Number.isInteger(x) ? String(x) : new Frac(Math.round(x * 1000), 1000).tex();
}

export function intervalTex(ivs: Interval[]): string {
  if (ivs.length === 0) return '\\varnothing';
  return ivs
    .map((i) => {
      if (i.lo === i.hi) return `\\{${endTex(i.lo)}\\}`;
      return `${i.loC ? '[' : '('}${endTex(i.lo)},${endTex(i.hi)}${i.hiC ? ']' : ')'}`;
    })
    .join('\\cup ');
}

export function inIntervals(ivs: Interval[], x: number): boolean {
  return ivs.some((i) => (x > i.lo || (i.loC && x === i.lo)) && (x < i.hi || (i.hiC && x === i.hi)));
}

/** Intersection of two interval unions (sorted, merged). */
export function intersect(a: Interval[], b: Interval[]): Interval[] {
  const out: Interval[] = [];
  for (const x of a)
    for (const y of b) {
      let lo: number, loC: boolean, hi: number, hiC: boolean;
      if (x.lo > y.lo) [lo, loC] = [x.lo, x.loC];
      else if (y.lo > x.lo) [lo, loC] = [y.lo, y.loC];
      else [lo, loC] = [x.lo, x.loC && y.loC];
      if (x.hi < y.hi) [hi, hiC] = [x.hi, x.hiC];
      else if (y.hi < x.hi) [hi, hiC] = [y.hi, y.hiC];
      else [hi, hiC] = [x.hi, x.hiC && y.hiC];
      if (lo < hi || (lo === hi && loC && hiC)) out.push({ lo, hi, loC, hiC });
    }
  return normalize(out);
}

export function complement(a: Interval[]): Interval[] {
  const s = normalize(a);
  const out: Interval[] = [];
  let lo = -Infinity;
  let loC = false;
  for (const x of s) {
    if (lo < x.lo || (lo === x.lo && loC && !x.loC)) out.push(iv(lo, x.lo, loC, !x.loC));
    lo = x.hi;
    loC = !x.hiC;
  }
  if (lo < Infinity) out.push(iv(lo, Infinity, loC, false));
  return out.filter((i) => i.lo < i.hi || (i.loC && i.hiC));
}

export function union(a: Interval[], b: Interval[]): Interval[] {
  return complement(intersect(complement(a), complement(b)));
}

export function normalize(a: Interval[]): Interval[] {
  const s = a.slice().sort((x, y) => x.lo - y.lo || (x.loC === y.loC ? 0 : x.loC ? -1 : 1));
  const out: Interval[] = [];
  for (const x of s) {
    const last = out[out.length - 1];
    if (last && (x.lo < last.hi || (x.lo === last.hi && (x.loC || last.hiC)))) {
      if (x.hi > last.hi) {
        last.hi = x.hi;
        last.hiC = x.hiC;
      } else if (x.hi === last.hi) last.hiC = last.hiC || x.hiC;
    } else out.push({ ...x });
  }
  return out;
}
