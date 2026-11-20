# Verification report

Every question in the bank was checked in at least two independent ways. All checks below run in CI (`.github/workflows/ci-deploy.yml`), so a broken question fails the build.

Last full run: 20 Nov 2026. Result: **all checks pass**.

## Summary

| Check | Math | Physics | Chemistry | Total |
|---|---|---|---|---|
| Questions in the bank | 263 | 185 | 162 | **610** |
| Numeric answers recomputed by sympy/Python | 240 | 124 | 52 | **416** |
| Conceptual questions re-solved from scratch (second pass) | 23 | 61 | 110 | **194** |
| Disagreements found and still open | 0 | 0 | 0 | **0** |
| Explanations that reach the marked answer | 263 | 185 | 162 | **610** |
| Answer positions A/B/C/D | 66/66/66/65 | 47/46/46/46 | 41/41/40/40 | balanced |
| Fixed mocks (48 questions, disjoint) | 3 | 3 | 3 | 9 |

Generated maths: **27 generators**, each tested on **250 seeds** (6,750 generated questions per test run) against an independent solver.

## 1. Numeric answers: `npm run verify:numeric`

`scripts/verify/run_all.py` loads every question and its check. The checks are defined next to each question in `scripts/authoring/bank_*.py` and collected by `verify_<subject>.py`. Each check **recomputes the answer from the question's givens** (sympy for algebra, calculus, sets and inequalities; plain Python for physics and chemistry arithmetic, enumeration for probability). It does not copy the marked option. For example:

- inequalities: `sp.solveset(...)` over the reals, compared with the option parsed as an interval union;
- derivatives and integrals: `sp.diff`, `sp.integrate`, `sp.limit`;
- probability: brute-force enumeration with `itertools` (dice, cards, arrangements);
- normal distribution: `statistics.NormalDist`, with σ chosen to match the given tail probability;
- physics/chemistry: formulas with the stated constants (g = 10 m/s², standard relative atomic masses).

The runner parses **every** option (LaTeX to sympy: fractions, roots, π, intervals, sets, points, equations, complex numbers, numbers with units) and requires that **exactly one option matches the recomputed answer, and that it is the marked option**. This catches wrong keys, duplicate correct answers and distractors that are accidentally correct. Rounded answers use a relative tolerance of 2% (stated per check where larger).

Bugs this caught during authoring (all fixed): two checks of my own that were wrong (a missing `abs`, and an absolute tolerance that made 10⁻¹⁷-sized values all "equal"), and parser issues with units and complex numbers. No question had a wrong key.

Every question must either have a check or carry the `conceptual` tag. The runner fails if a numeric question has no check.

## 2. Conceptual questions: second-pass review (`npm run verify:review`)

For the 194 questions without a numeric answer (definitions, laws, lab practice, "which statement is correct"), I printed each question and its options **without the marked answer**, solved it again from scratch, and recorded my answer in `scripts/verify/conceptual_review_*.txt`. `check_review.py` compares those answers with the marked ones.

Result: 194/194 agree, 0 disagreements.

## 3. Explanations reach the marked answer (`npm run verify:explanations`)

`explanation_check.py` checks that the content of the correct option (its formula, number or key words) appears in the explanation. 568/610 passed automatically. The other 42 state the answer in different words (e.g. "divides F by 4" for "one quarter of the original"). I read all 42 and confirmed each reaches the marked answer; they are listed in `EXPLANATION_REVIEWED`.

## 4. Schema and rendering (`npm run validate:content`)

`scripts/validate-content.ts` checks every question for:

- required fields and types; a valid subject/topic/subtopic pair; difficulty 1–3; exactly 4 options; answer index 0–3; unique ids;
- **no duplicate options** (after normalising whitespace and case); no "all/none of the above";
- explanations do not refer to option letters (positions can be shuffled);
- **every `$…$` segment compiles with KaTeX** (`throwOnError`), plus balanced `$` and no control characters (catches `\frac` written with one backslash in JSON);
- minimum counts (Math ≥ 250, Physics ≥ 180, Chemistry ≥ 150; every subtopic ≥ 8 questions);
- answer positions are balanced;
- a notes file for every subtopic and a formula sheet per subject, all KaTeX-valid;
- fixed mocks: 3 per subject, 48 existing questions each, no duplicates.

## 5. Generators (`npm test`, `tests/generators.test.ts`)

Each of the 27 generators is run on 250 seeds. For every generated question the test checks:

- 4 distinct options, a valid answer index, no `NaN`/`undefined`, and no filler options (all distractors come from modelled mistakes);
- the correct option is right according to an **independent** solver written in the test, not in the generator. Examples: sampling the inequality on a grid of points, a brute-force minimisation for point-to-line distance, scanning a fine grid for the extrema of a cubic, finite differences for derivatives, a real normal CDF for normal-distribution questions, and enumerating dice and balls;
- every distractor is **wrong** according to the same solver;
- answer positions are spread across A–D;
- the id `gen:<type>:<seed>` rebuilds the identical question.

## 6. Difficulty mix

| | Easy | Medium | Hard |
|---|---|---|---|
| Math | 28% | 49% | 22% |
| Physics | 30% | 48% | 21% |
| Chemistry | 30% | 48% | 20% |

## 7. App tests

- `npm test`: 60 unit tests (generators, scoring, spaced repetition, study plan, progress code/report, mock assembly).
- `npm run test:e2e`: Playwright runs a 5-question practice session answered with the keyboard, a full mock exam (navigator, flag, submit, score, per-topic review, history chart), auto-submit at time-up using a fake clock, a smoke test of every page with a KaTeX-error check, and the study plan plus tutor import round-trip.
- Lighthouse (mobile simulation, preview build): Accessibility 100, Best practices 100, SEO 100, Performance 83–86.
- Screenshots of 15 pages at 390 px and 1280 px, light and dark (`npm run screenshots`). They were reviewed by eye, and an automatic check confirms no horizontal overflow and no KaTeX errors on any page.
