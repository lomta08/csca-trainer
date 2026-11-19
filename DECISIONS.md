# Decisions log

Choices made while working unattended. Each entry says what was decided and why.

1. **csca.cn could not be re-checked.** The site is a JavaScript single-page app, and an automated fetch returns only the word "CSCA". The exam format in the brief (Math/Physics/Chemistry: 60 min, 48 single-answer MCQs, 0–100; Professional Chinese: 90 min, 80 MCQs) is used as given. The Resources page links to the official pages and tells the student to confirm dates there.
2. **GitHub CLI (`gh`) is not installed on this machine**, so the repo could not be created or pushed overnight. Everything is committed locally on `main`, and the GitHub Actions workflow is ready. See PROGRESS.md → "To publish" for the 3 commands to run.
3. **HashRouter** (`/#/practice`) instead of BrowserRouter, so deep links and refreshes work on GitHub Pages without a 404 workaround.
4. **Vite `base` = `/csca-trainer/`** (overridable with `BASE_PATH`), matching the repo name.
5. **Content is JSON** (not TS), so it can be edited without a build toolchain and read directly by the Python verification scripts. In JSON every LaTeX backslash is written twice (`\frac`). The validator rejects control characters, which catches a single `\f`, `\t` or `\b` that JSON would otherwise silently turn into a form-feed, tab or backspace.
6. **Subtopics = syllabus bullets.** Math 17, Physics 16, Chemistry 17. Each subtopic has its own notes page and ≥ 8 questions.
7. **Mock score** = round(100 × correct / 48). Unanswered questions count as wrong (there is no negative marking on CSCA as far as is published).
8. **Fixed mocks** are fixed lists of bank question ids, chosen by a seeded script so that the three mocks per subject are disjoint and follow the syllabus topic weights. Random mocks draw from the whole bank with the same weights.
9. **Mock topic weights** (out of 48). Math: sets & inequalities 7, functions 19, geometry & algebra 15, probability & statistics 7. Physics: mechanics 24, electromagnetism 12, thermodynamics 4, optics 4, modern 4. Chemistry: basic concepts 13, properties & reactions 14, theories & laws 12, experiments 9. CSCA does not publish exact weights; these follow the syllabus's emphasis (gaokao-like papers weight functions and mechanics most).
10. **Spaced repetition**: a wrong answer adds the question to the notebook. A correct answer records the calendar day. The question leaves after correct answers on 2 different days. A new wrong answer resets its correct-day count. A question answered correctly today is "not due" until tomorrow, so retry sessions show due items first.
11. **Generated questions** have ids like `gen:quadratic-inequality:123456`. The seed rebuilds the exact question, so mistakes and flags work for generated questions without storing their text.
12. **Progress code for the tutor** is a compact JSON summary (per-subtopic accuracy, mock results, study time, streak, mistakes count), not the raw history, so it stays short enough to paste into a chat. A separate full backup/restore lives on the Settings page.
13. **Answer positions**: questions were written in any order, then `scripts/balance-answers.ts` permutes options deterministically so A/B/C/D are evenly used. Explanations never refer to a letter, so this is safe.
14. **Time studied** = time spent on question screens and lesson pages (active tab only, capped at 5 min per question), logged per calendar day. Streak = consecutive days with any activity, ending today or yesterday.
15. **g = 10 m/s²** in physics unless a question says otherwise; every question that uses g states it.
16. **TypeScript 5.9** is pinned rather than 7.x, for tooling compatibility.
