"""
Recompute every numeric answer and check it against the marked option.

    python scripts/verify/run_all.py          # all subjects
    python scripts/verify/run_all.py math     # one subject

Rules enforced:
  * every question is either covered by a check in verify_<subject>.py, or tagged "conceptual";
  * for checked questions exactly ONE option matches the recomputed answer, and it is the marked one;
  * every check refers to an existing question.
Writes scripts/verify/report.json (used for VERIFICATION.md).
"""
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vlib import load_questions  # noqa: E402

SUBJECTS = ["math", "physics", "chemistry"]


def run(subject: str) -> dict:
    qs = load_questions(subject)
    try:
        mod = importlib.import_module(f"verify_{subject}")
        checks = mod.CHECKS
    except ModuleNotFoundError:
        checks = {}
    failures: list[str] = []
    for cid in checks:
        if cid not in qs:
            failures.append(f"{cid}: check refers to a question that does not exist")
    checked = conceptual = 0
    for qid, q in qs.items():
        if qid in checks:
            chk = checks[qid]
            matches = []
            for i, opt in enumerate(q["options"]):
                try:
                    if chk.match(opt):
                        matches.append(i)
                except Exception as e:  # unparsable option counts as "does not match"
                    if i == q["answer"]:
                        failures.append(f"{qid}: could not evaluate the marked option {opt!r}: {e}")
            if matches != [q["answer"]]:
                letters = "".join("ABCD"[i] for i in matches) or "none"
                failures.append(f"{qid}: recomputed answer {chk.describe()} matches option(s) {letters}, marked {'ABCD'[q['answer']]}  options={q['options']}")
            checked += 1
        elif "conceptual" in q.get("tags", []):
            conceptual += 1
        else:
            failures.append(f"{qid}: no verification check and not tagged 'conceptual'")
    return {"subject": subject, "total": len(qs), "checked": checked, "conceptual": conceptual, "failures": failures}


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    subjects = sys.argv[1:] or SUBJECTS
    results = [run(s) for s in subjects]
    bad = 0
    for r in results:
        status = "OK" if not r["failures"] else f"{len(r['failures'])} FAILURE(S)"
        print(f"{r['subject']:10s} total {r['total']:4d}  numeric-checked {r['checked']:4d}  conceptual {r['conceptual']:4d}  {status}")
        for f in r["failures"]:
            print("   ✗", f)
        bad += len(r["failures"])
    if len(subjects) == len(SUBJECTS):
        out = Path(__file__).resolve().parent / "report.json"
        out.write_text(json.dumps(results, indent=2), encoding="utf8")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
