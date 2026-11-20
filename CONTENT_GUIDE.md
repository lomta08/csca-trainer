# Content guide: adding or editing questions

All content lives in `src/content/`. You never need to touch the React code.

```
src/content/
  syllabus.ts                 subjects → topics → subtopics (ids used everywhere)
  math/*.json                 question banks, one file per syllabus topic
  physics/*.json
  chemistry/*.json
  notes/<subject>/<subtopic>.md   lessons (Markdown + LaTeX)
  formulas/<subject>.md           formula sheets
  mocks/fixed-mocks.json          the fixed mock exams (lists of question ids)
```

## 1. Add a question

Open the JSON file for the topic, e.g. `src/content/math/functions.json`, and add an object to the array:

```json
{
  "id": "m-trig-23",
  "subject": "math",
  "topic": "functions",
  "subtopic": "trigonometry",
  "difficulty": 2,
  "question": "If $\\tan\\alpha=\\dfrac12$, then $\\tan2\\alpha=$",
  "options": ["$\\dfrac43$", "$1$", "$\\dfrac34$", "$\\dfrac23$"],
  "answer": 0,
  "explanation": "$\\tan2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}=\\dfrac{1}{1-\\frac14}=\\dfrac43$.",
  "tags": ["numeric"]
}
```

| Field | Rules |
|---|---|
| `id` | unique; lowercase letters, digits and dashes. Convention: `m-`, `p-`, `c-` + short topic + number |
| `subject` | `math`, `physics` or `chemistry` (must match the folder) |
| `topic`, `subtopic` | ids from `src/content/syllabus.ts`; the subtopic must belong to the topic |
| `difficulty` | `1` easy, `2` medium, `3` hard (aim for roughly 30/50/20) |
| `question`, `explanation` | Markdown. Inline maths `$...$`, display maths `$$...$$` |
| `options` | exactly 4 different strings |
| `answer` | index of the correct option: `0`=A, `1`=B, `2`=C, `3`=D |
| `tags` | free labels. Use `"conceptual"` for questions without a numeric answer |

### Writing LaTeX inside JSON

JSON needs **two backslashes** for every LaTeX backslash: write `\\frac`, `\\sqrt`, `\\pi`, `\\mathrm{H_2O}`.
A single backslash is either rejected or silently changes the text: `\f`, `\t` and `\b` become invisible control characters. The validator catches all of these.

Tips:

- Chemistry formulas: `$\\mathrm{H_2SO_4}$`, ions `$\\mathrm{SO_4^{2-}}$`, arrows `\\rightarrow`, `\\rightleftharpoons`.
- Units outside the maths: `"$20$ m/s"`, or inside it: `"$20\\ \\text{m/s}$"`.
- Physics: say "(take $g=10\\ \\text{m/s}^2$)" whenever $g$ is used.
- Chemistry: list the relative atomic masses used, e.g. "(Relative atomic masses: Na $23$, O $16$)".
- Never refer to option letters in the explanation ("so the answer is B"). End the explanation with the answer itself.
- Avoid "all of the above" / "none of the above".

## 2. Check your work

```bash
npm run validate:content   # schema, KaTeX, duplicates, counts, mocks
npm run verify             # also numeric recomputation, explanations, conceptual review
npm run dev                # look at it in the browser: http://localhost:5173/csca-trainer/
```

### Numeric questions: add a verification check

Every question needs either a numeric check or the `conceptual` tag. For a new numeric question, add a check to `EXTRA` in `scripts/verify/verify_<subject>.py`. The check must **recompute** the answer from the givens:

```python
from vlib import *            # N, R, S, Expr, Eqn, Pt, T, Nums, Num, CR, Foci, Asym ...
import sympy as sp

EXTRA = {
    "m-trig-23": N(sp.tan(2 * sp.atan(sp.Rational(1, 2)))),   # exact value
    "p-kin-15": R(20 * 3 + 0.5 * 2 * 3**2),                  # rounded, 2% tolerance
}
```

`run_all.py` then checks that exactly one option matches, and that it is the marked one.

### Conceptual questions: second-pass review

Solve the question yourself without looking at the key, then add a line `m-xxx-01 B` to `scripts/verify/conceptual_review_3.txt` (create the file if needed). `npm run verify:review` compares your answer with the key.

## 3. Lessons and formula sheets

Edit `src/content/notes/<subject>/<subtopic>.md` or `src/content/formulas/<subject>.md`. These are plain Markdown files, so use **single** backslashes here (`\frac`), unlike JSON.

## 4. Fixed mock exams

`src/content/mocks/fixed-mocks.json` lists the question ids of each fixed paper. To rebuild the three disjoint papers per subject after adding many questions, run `npm run build:mocks`. Old attempt history still refers to the mock ids, so scores stay comparable only if you keep the old papers. Rebuilding is optional.

## 5. How the initial bank was written

The first 610 questions were drafted in `scripts/authoring/bank_*.py`, using Python raw strings so LaTeX did not need doubled backslashes. Each numeric question has its check right next to it. `python scripts/authoring/build.py` wrote the JSON files and placed the correct option so that A/B/C/D are evenly used. **The JSON files are now the source of truth.** Re-running `build.py` would overwrite any edits you made to the JSON by hand, so don't, unless you edit the Python files instead.
