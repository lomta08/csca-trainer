# CSCA Trainer — Build Plan

Static Vite + React + TypeScript site that helps one student prepare for the CSCA
(China Scholastic Competency Assessment) Mathematics, Physics and Chemistry papers, taken in English.

## Milestones

| # | Milestone | Contents | Done when |
|---|-----------|----------|-----------|
| 1 | Scaffold + deploy pipeline | Vite/React/TS, routing (HashRouter), theme, layout, GitHub Actions workflow (CI + Pages) | `npm run build` passes, workflow file committed |
| 2 | Question engine + practice | Question schema/types, content loader, Markdown+KaTeX renderer, QuestionCard with keyboard support, practice setup → session → summary, flagging, localStorage store | Can practise any topic with instant feedback |
| 3 | Math content + generators + verification | 250+ hand-written math questions, 25+ seeded generators with distractors from typical mistakes, unit tests, sympy verification scripts, schema validator | `validate:content`, `verify:numeric`, `test` all pass |
| 4 | Mock exams | 48 Q / 60 min, syllabus-weighted random mocks, 3 fixed mocks per subject, navigator, flags, auto-submit, 0–100 score, review, per-topic breakdown, time per question, history + trend chart | Mock can be completed and reviewed |
| 5 | Physics + chemistry content | 180+ physics, 150+ chemistry, verification scripts, periodic table/data page | Counts met, all checks pass |
| 6 | Dashboard, mistakes, plan, tutor | Exam overview, countdown, progress per subject/topic, weakest topics, streak, continue; mistakes notebook with 2-day spaced repetition; study plan generator checklist; tutor view with export/import + copy report | Unit tests for SR + plan pass |
| 7 | Notes + formula sheets | One lesson per syllabus subtopic (definitions, formulas, 2–3 worked examples, traps, practice button); printable formula sheet per subject; resources + Chinese info pages | Every subtopic has notes |
| 8 | Polish + tests | Playwright e2e (practice + mock), screenshots on mobile/desktop, fix visual issues, accessibility, final checklist | Checklist all ticked |

## Architecture

- `src/content/syllabus.ts` — subjects → topics → subtopics (ids, names, mock weights, study-hour estimates).
- `src/content/<subject>/*.json` — hand-written question banks (one file per syllabus topic).
- `src/content/notes/<subject>/<subtopic>.md` — lessons (Markdown + LaTeX).
- `src/content/formulas/<subject>.md` — formula sheets.
- `src/content/mocks/fixed-mocks.json` — fixed mock exams (lists of question ids).
- `src/lib/generators/` — seeded random math generators (id `gen:<type>:<seed>` regenerates the same question).
- `src/lib/store.ts` — localStorage persistence (try/catch everywhere).
- `scripts/validate-content.ts` — schema validator (CI).
- `scripts/verify/*.py` — sympy recomputation of every numeric answer (CI).
