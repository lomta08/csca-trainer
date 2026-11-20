# Progress

**Live URL:** **https://lomta08.github.io/csca-trainer/** (deployed by GitHub Actions on every push to `main`; repo: https://github.com/lomta08/csca-trainer)

Everything is done, pushed to GitHub, and verified locally and in CI.

## Final checklist

- [x] Every syllabus bullet for Math (17 subtopics), Physics (16) and Chemistry (17) has a lesson page and at least 8 questions (minimum per subtopic: 8; most have 10–22).
- [x] Question counts meet the minimums: **Math 263** (≥250), **Physics 185** (≥180), **Chemistry 162** (≥150). **3 fixed mocks per subject**, 48 questions each, no overlap between papers.
- [x] **27 math generators** (≥20), all unit-tested against independent solvers on 250 seeds each.
- [x] All 416 numeric answers are recomputed by sympy/Python scripts, and all 194 conceptual questions were re-solved in a second pass: 0 disagreements. See [VERIFICATION.md](VERIFICATION.md).
- [x] Mock exam: 48 questions, 60 min, 0–100 score, review with solutions, per-topic breakdown, time per question, history and score-trend chart, auto-submit at time-up (tested with a fake clock).
- [x] Practice (keyboard 1–4/A–D, Enter, F), mistakes notebook with 2-day spaced repetition, study plan generator with checklist, tutor view with export/import progress code and "Copy report", resources page, Chinese info page, periodic table/data page, printable formula sheets.
- [x] Mobile-friendly (checked at 390 px: no horizontal overflow on any page), dark mode (system or manual), KaTeX renders everywhere (KaTeX errors checked on every page by the e2e and screenshot scripts).
- [x] Tests and content validation pass; build has 0 TypeScript errors. *Locally:* `npm run verify` ✔, 60 unit tests ✔, 5 Playwright e2e tests ✔, `npm run build` ✔. *In CI:* all steps pass on GitHub Actions (Node 24).
- [x] Live on GitHub Pages: https://lomta08.github.io/csca-trainer/

## What was built (milestones)

1. Scaffold: Vite + React 19 + TypeScript, HashRouter, light/dark themes, layout, GitHub Actions CI + Pages workflow.
2. Question engine and practice mode, with a localStorage store wrapped in try/catch.
3. Math bank (263) + 27 generators + sympy verification + content validator.
4. Mock exams (random and fixed), timer, navigator, review, history chart.
5. Physics (185) and chemistry (162) banks + verification; periodic table/data page.
6. Dashboard, mistakes notebook, study plan, tutor view, settings (backup/restore), unlimited math drill.
7. 50 lessons + 3 formula sheets, resources and Chinese pages.
8. Playwright e2e tests, Lighthouse check, mobile/desktop/dark screenshot review and fixes, verification report, docs.

## Quality checks run

| Check | Result |
|---|---|
| `npm run validate:content` | ✔ 610 questions, all KaTeX valid, balanced answers |
| `npm run verify:numeric` | ✔ 416 recomputed answers, 0 failures |
| `npm run verify:review` | ✔ 194/194 conceptual questions agree |
| `npm run verify:explanations` | ✔ 610/610 |
| `npm test` | ✔ 60 tests |
| `npm run test:e2e` | ✔ 5 tests |
| `npm run build` | ✔ 0 TypeScript errors |
| Lighthouse (mobile) | Accessibility 100 · Best practices 100 · SEO 100 · Performance 83–86 |

Problems found by the screenshot review and fixed: a KaTeX CSS/JS version mismatch that broke square roots and subscripts, Markdown tables overflowing on phones, list bullets clipped, a duplicate "Next" button in the exam view, and a stale "continue" link after a mock.

## Known issues / ideas for later

- Performance score is 83–86 on Lighthouse's throttled-mobile simulation. The whole question bank (≈350 kB of JSON) ships in the first bundle so practice is instant. If this matters, the bank could be split per subject.
- csca.cn could not be fetched automatically (it is a JavaScript-only site), so exam facts follow your brief. Please double-check dates and formats on csca.cn.
- Progress lives in one browser. The Settings page has backup/restore, and the Tutor page has the progress code, but there is no automatic sync between devices (no backend, by design).
- Content ideas: more hard (difficulty 3) chemistry questions, a timed "speed drill" mode, and per-question time targets in practice mode.
