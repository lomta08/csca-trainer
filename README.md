# CSCA Trainer

**Live site:** not published yet — the GitHub CLI was not available on the build machine. Publishing takes three commands; see [Publishing](#publishing). The site will then be at `https://<your-github-username>.github.io/csca-trainer/`.

A free, mobile-friendly practice site for the **CSCA** (China Scholastic Competency Assessment) Mathematics, Physics and Chemistry papers, taken in English. It is built for one student and their tutor.

## What's inside

- **610 original questions**: Math 263, Physics 185, Chemistry 162. Every syllabus subtopic has at least 8 questions, mixed about 30/50/20 easy/medium/hard. All 416 numeric answers are recomputed with sympy; all 194 conceptual questions were re-solved in a second pass ([VERIFICATION.md](VERIFICATION.md)).
- **Unlimited maths**: 27 question generators (inequalities, sets, domains, logs, trig, sequences, derivatives, tangents, extrema, lines, circles, conics, vectors, complex numbers, 3D distance, probability, statistics, normal distribution). Wrong options come from typical mistakes. Every generator is unit-tested against an independent solver.
- **Learn**: a lesson for each of the 50 syllabus subtopics, with key ideas, formulas, worked examples, common traps and a "Practice this topic" button.
- **Formula sheets**: one printable page per subject. **Chemistry data**: periodic table, constants, solubility rules.
- **Practice**: choose subject, topics, difficulty and number of questions. Instant feedback, step-by-step solutions, flagging, and keyboard shortcuts (1–4 / A–D to answer, Enter for next, F to flag).
- **Mock exams**: 48 questions, 60-minute timer, syllabus-weighted topic mix, question navigator, flag for review, no feedback until you submit, auto-submit at time-up. Scored 0–100 with a full review, per-topic breakdown, time per question, history and a score-trend chart. 3 fixed papers per subject plus unlimited random ones.
- **Mistakes notebook**: wrong answers are saved automatically. Spaced repetition: a question leaves the notebook after correct answers on 2 different days.
- **Study plan**: enter the exam date, subjects and hours per week to get a week-by-week checklist covering every topic, with mocks in the final weeks.
- **Dashboard**: countdown, progress per subject and topic, weakest topics, study streak, "continue where you left off".
- **Tutor view**: the student copies a short progress code; the tutor pastes it to see accuracy per topic, mock scores and time studied. "Copy report" produces a plain-text summary for a message.
- **Resources**: official links, exam-day tips, time strategy, how to choose subjects.
- Dark mode, no account needed. Progress is kept in the browser, with backup and restore on the Settings page.

## Development

```bash
npm install
npm run dev              # http://localhost:5173/csca-trainer/
npm run build            # type-check + production build into dist/
npm test                 # unit tests (Vitest)
npm run test:e2e         # Playwright end-to-end tests (run `npx playwright install chromium` once)
npm run verify           # content schema + sympy answer checks + explanation + review checks (needs Python 3 with sympy)
npm run screenshots      # with `npm run preview` running: screenshots of all pages, phone + desktop
```

Stack: Vite, React 19, TypeScript, KaTeX (react-markdown + remark-math + rehype-katex), plain CSS, HashRouter. There is no backend.

To add or edit questions, lessons or mocks, see **[CONTENT_GUIDE.md](CONTENT_GUIDE.md)**. Design decisions are in [DECISIONS.md](DECISIONS.md), status in [PROGRESS.md](PROGRESS.md).

## Publishing

The repository includes `.github/workflows/ci-deploy.yml`. On every push to `main` it validates and verifies the content, runs the unit and end-to-end tests, builds the site and deploys it to GitHub Pages.

On Windows (PowerShell), from this folder:

```powershell
winget install --id GitHub.cli          # once; then open a new terminal
gh auth login                           # once; choose GitHub.com → HTTPS → browser
gh repo create csca-trainer --public --source . --remote origin --push
```

Then, on GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions** (or run `gh api -X POST repos/{owner}/csca-trainer/pages -f build_type=workflow`). The first deployment finishes a few minutes after the push; the Actions tab shows the URL. If you use a different repository name, set `BASE_PATH=/<name>/` (see `vite.config.ts`).

## Disclaimer

All questions, lessons and explanations are original. Nothing is copied from past papers or third-party materials. This site is not affiliated with the China Scholarship Council. Confirm exam dates and requirements on [csca.cn](https://www.csca.cn).
