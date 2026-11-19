import type { GeneratorDef } from './core';
import { Frac, m } from './format';

const diceProbability: GeneratorDef = {
  id: 'dice-probability',
  name: 'Two dice probability',
  topic: 'probability-statistics',
  subtopic: 'classical-probability',
  make(r) {
    const variant = r.int(0, 2);
    let count = 0;
    let question: string;
    let how: string;
    let unordered = 0;
    let param = 0;
    if (variant === 0) {
      const s = r.int(3, 11);
      param = s;
      for (let a = 1; a <= 6; a++) for (let b = 1; b <= 6; b++) if (a + b === s) count++;
      for (let a = 1; a <= 6; a++) for (let b = a; b <= 6; b++) if (a + b === s) unordered++;
      question = `Two fair dice are rolled. The probability that the sum of the two numbers is ${m(String(s))} is`;
      how = `There are ${m('6\\times6=36')} equally likely ordered outcomes. Pairs with sum ${s}: ${count} (count ${m('(a,b)')} and ${m('(b,a)')} separately).`;
    } else if (variant === 1) {
      const s = r.int(8, 11);
      param = s;
      for (let a = 1; a <= 6; a++) for (let b = 1; b <= 6; b++) if (a + b >= s) count++;
      for (let a = 1; a <= 6; a++) for (let b = a; b <= 6; b++) if (a + b >= s) unordered++;
      question = `Two fair dice are rolled. The probability that the sum is at least ${m(String(s))} is`;
      how = `36 equally likely ordered outcomes; ${count} of them have sum ${m(`\\ge ${s}`)}.`;
    } else {
      const k = r.pick([2, 3]);
      param = k;
      for (let a = 1; a <= 6; a++) for (let b = 1; b <= 6; b++) if ((a * b) % k === 0) count++;
      for (let a = 1; a <= 6; a++) for (let b = a; b <= 6; b++) if ((a * b) % k === 0) unordered++;
      question = `Two fair dice are rolled. The probability that the product of the two numbers is a multiple of ${m(String(k))} is`;
      how = `Use the complement: the product is **not** a multiple of ${k} only when neither die is a multiple of ${k}: ${m(`${6 - Math.floor(6 / k)}\\times${6 - Math.floor(6 / k)}=${36 - count}`)} outcomes. So ${count} of the 36 outcomes work.`;
    }
    const ans = new Frac(count, 36);
    return {
      question,
      correct: m(ans.tex()),
      distractors: [m(new Frac(unordered, 21).tex()), m(new Frac(36 - count, 36).tex()), m(new Frac(count, 6).value() <= 1 ? new Frac(count, 6).tex() : new Frac(count + 1, 36).tex()), m(new Frac(count - 1 || 2, 36).tex()), m(new Frac(count + 1, 36).tex())],
      explanation: `${how}\n\n${m(`P=\\dfrac{${count}}{36}=${ans.tex()}`)}.`,
      difficulty: variant === 2 ? 2 : 1,
      meta: { variant, param, count, value: ans.value() },
    };
  },
};

function C(n: number, k: number): number {
  if (k < 0 || k > n) return 0;
  let v = 1;
  for (let i = 1; i <= k; i++) v = (v * (n - k + i)) / i;
  return Math.round(v);
}

const ballsProbability: GeneratorDef = {
  id: 'balls-probability',
  name: 'Drawing balls without replacement',
  topic: 'probability-statistics',
  subtopic: 'classical-probability',
  make(r) {
    const red = r.int(2, 5);
    const white = r.int(2, 4);
    const n = red + white;
    const variant = r.pick(['both-red', 'one-each', 'at-least-one-white'] as const);
    const total = C(n, 2);
    let fav: number;
    let what: string;
    let how: string;
    let withRep: Frac;
    if (variant === 'both-red') {
      fav = C(red, 2);
      what = 'both balls are red';
      how = `${m(`C_{${red}}^2=${fav}`)} ways to choose two red balls`;
      withRep = new Frac(red * red, n * n);
    } else if (variant === 'one-each') {
      fav = red * white;
      what = 'one ball is red and the other is white';
      how = `${m(`C_{${red}}^1C_{${white}}^1=${fav}`)} ways to choose one of each colour`;
      withRep = new Frac(2 * red * white, n * n);
    } else {
      fav = total - C(red, 2);
      what = 'at least one ball is white';
      how = `complement: ${m(`${total}-C_{${red}}^2=${total}-${C(red, 2)}=${fav}`)} ways`;
      withRep = new Frac(n * n - red * red, n * n);
    }
    const ans = new Frac(fav, total);
    const ordered = new Frac(fav, n * (n - 1)); // forgot that choosing is unordered
    return {
      question: `A bag contains ${red} red balls and ${white} white balls of the same size. Two balls are drawn at random at the same time. The probability that ${what} is`,
      correct: m(ans.tex()),
      distractors: [m(withRep.tex()), m(ordered.tex()), m(new Frac(1).sub(ans).tex()), m(new Frac(fav, n * n).tex())],
      explanation: `Number of ways to choose 2 of ${n} balls: ${m(`C_{${n}}^2=${total}`)}. Favourable: ${how}.\n\n${m(`P=\\dfrac{${fav}}{${total}}=${ans.tex()}`)}.`,
      difficulty: variant === 'at-least-one-white' ? 2 : 1,
      meta: { red, white, variant, value: ans.value() },
    };
  },
};

const meanVariance: GeneratorDef = {
  id: 'mean-variance',
  name: 'Mean and variance',
  topic: 'probability-statistics',
  subtopic: 'mean-variance',
  make(r) {
    const variant = r.int(0, 1);
    if (variant === 0) {
      // 5 values with integer mean
      const mean = r.int(3, 12);
      const devs = r.pick([[-2, -1, 0, 1, 2], [-3, -1, 0, 1, 3], [-4, -2, 0, 2, 4], [-2, -2, 0, 2, 2], [-3, 0, 0, 1, 2], [-1, -1, 0, 1, 1], [-4, 1, 1, 1, 1]]);
      const data = r.shuffle(devs.map((d) => mean + d));
      const ss = devs.reduce((s, d) => s + d * d, 0);
      const v = new Frac(ss, 5);
      return {
        question: `The variance of the data ${m(data.join(',\\ '))} is`,
        correct: m(v.tex()),
        distractors: [m(new Frac(ss, 4).tex()), m(String(ss)), m(String(Math.sqrt(v.value()) % 1 === 0 ? Math.sqrt(v.value()) + 1 : Math.round(Math.sqrt(v.value()) * 100) / 100)), m(new Frac(ss, 5).add(1).tex())],
        explanation: `Mean ${m(`\\bar x=${mean}`)}. Deviations: ${m(devs.slice().sort((a, b) => a - b).join(',\\ '))}. ${m(`s^2=\\dfrac{1}{n}\\sum(x_i-\\bar x)^2=\\dfrac{${ss}}{5}=${v.tex()}`)}. (CSCA/gaokao uses dividing by ${m('n')}.)`,
        difficulty: 1,
        meta: { variant, data, value: v.value() },
      };
    }
    const mu = r.int(2, 9);
    const s2 = r.int(1, 6);
    const a = r.pick([-3, -2, 2, 3, 4]);
    const b = r.nonzero(-5, 5);
    const newMean = a * mu + b;
    const newVar = a * a * s2;
    const ask = r.bool() ? 'var' : 'both';
    const opt = (mm: number, vv: number) => `mean ${m(String(mm))}, variance ${m(String(vv))}`;
    if (ask === 'var') {
      return {
        question: `A data set has mean ${m(String(mu))} and variance ${m(String(s2))}. Each value ${m('x_i')} is replaced by ${m(`${a === 1 ? '' : a === -1 ? '-' : a}x_i${b === 0 ? '' : b > 0 ? `+${b}` : b}`)}. The new variance is`,
        correct: m(String(newVar)),
        distractors: [m(String(Math.abs(a) * s2)), m(String(a * a * s2 + Math.abs(b))), m(String(Math.abs(a * s2 + b))), m(String(Math.abs(a) * s2 + 1))],
        explanation: `Adding a constant does not change spread; multiplying by ${m('a')} multiplies the variance by ${m('a^2')}: ${m(`D(ax+b)=a^2D(x)=${a * a}\\cdot${s2}=${newVar}`)}.`,
        difficulty: 2,
        meta: { variant, mu, s2, a, b, value: newVar },
      };
    }
    return {
      question: `A data set has mean ${m(String(mu))} and variance ${m(String(s2))}. Each value ${m('x_i')} is replaced by ${m(`${a === 1 ? '' : a === -1 ? '-' : a}x_i${b === 0 ? '' : b > 0 ? `+${b}` : b}`)}. The new data set has`,
      correct: opt(newMean, newVar),
      distractors: [opt(newMean, Math.abs(a) * s2), opt(a * mu, newVar), opt(newMean, a * a * s2 + Math.abs(b)), opt(a * mu + b * b, newVar), opt(newMean, newVar + Math.abs(a)), opt(newMean + 1, newVar)],
      explanation: `${m(`E(ax+b)=aE(x)+b=${a}\\cdot${mu}+(${b})=${newMean}`)}, and ${m(`D(ax+b)=a^2D(x)=${newVar}`)}.`,
      difficulty: 2,
      meta: { variant, mu, s2, a, b, mean: newMean, value: newVar },
    };
  },
};

const normalSymmetry: GeneratorDef = {
  id: 'normal-symmetry',
  name: 'Normal distribution symmetry',
  topic: 'probability-statistics',
  subtopic: 'normal-distribution',
  make(r) {
    const mu = r.int(-2, 100);
    const k = r.int(1, 10);
    const sigma = r.int(1, 5);
    const p = r.pick([0.1, 0.12, 0.15, 0.2, 0.25, 0.3, 0.35, 0.05, 0.08, 0.18]);
    const variant = r.int(0, 2);
    const f = (x: number) => String(Math.round(x * 1000) / 1000);
    let q: string;
    let ans: number;
    let wrong: number[];
    let how: string;
    if (variant === 0) {
      q = `${m(`P(X>${mu + k})=${f(p)}`)}. Then ${m(`P(${mu - k}<X<${mu + k})=`)}`;
      ans = 1 - 2 * p;
      wrong = [1 - p, 2 * p, 0.5 - p];
      how = `By symmetry about ${m(`\\mu=${mu}`)}, ${m(`P(X<${mu - k})=P(X>${mu + k})=${f(p)}`)}. So the middle part is ${m(`1-2\\times${f(p)}=${f(ans)}`)}.`;
    } else if (variant === 1) {
      q = `${m(`P(X<${mu - k})=${f(p)}`)}. Then ${m(`P(${mu}<X<${mu + k})=`)}`;
      ans = 0.5 - p;
      wrong = [1 - 2 * p, p, 1 - p];
      how = `${m(`P(X>${mu + k})=P(X<${mu - k})=${f(p)}`)} by symmetry, and ${m(`P(X>${mu})=0.5`)}. So ${m(`P(${mu}<X<${mu + k})=0.5-${f(p)}=${f(ans)}`)}.`;
    } else {
      const c = mu + k;
      const pc = 1 - p; // P(X < c)
      q = `${m(`P(X<${c})=${f(pc)}`)}. Then ${m(`P(X<${2 * mu - c})=`)}`;
      ans = p;
      wrong = [pc, 0.5 - p, 1 - 2 * p];
      how = `${m(`${2 * mu - c}`)} is the mirror image of ${m(String(c))} in ${m(`\\mu=${mu}`)}. So ${m(`P(X<${2 * mu - c})=P(X>${c})=1-${f(pc)}=${f(ans)}`)}.`;
    }
    return {
      question: `A random variable ${m(`X\\sim N(${mu},${sigma * sigma})`)} and ${q}`,
      correct: m(f(ans)),
      distractors: [...wrong.map((w) => m(f(w))), m(f(ans + 0.1)), m(f(Math.abs(ans - 0.05)))],
      explanation: `${how}\n\nThe value of ${m('\\sigma')} is not needed — only the symmetry of the normal curve about ${m('x=\\mu')}.`,
      difficulty: variant === 0 ? 1 : 2,
      meta: { mu, k, p, variant, value: ans },
    };
  },
};

export const probabilityGenerators = [diceProbability, ballsProbability, meanVariance, normalSymmetry];
