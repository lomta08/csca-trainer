"""
Second-pass review of conceptual (non-numeric) questions.

conceptual_review_*.txt hold answers worked out from scratch WITHOUT looking at the marked answer
(format: "<question id> <letter>"). This script compares them with the marked answers and checks
that every conceptual question has been reviewed. If you add or reorder a conceptual question,
solve it yourself and add a line.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def main() -> int:
    qs = {}
    for subj in ["math", "physics", "chemistry"]:
        for f in (ROOT / "src" / "content" / subj).glob("*.json"):
            for q in json.loads(f.read_text(encoding="utf8")):
                qs[q["id"]] = q
    reviewed = {}
    for f in sorted(HERE.glob("conceptual_review_*.txt")):
        for line in f.read_text(encoding="utf8").splitlines():
            if line.strip():
                qid, letter = line.split()
                reviewed[qid] = letter
    conceptual = {i for i, q in qs.items() if "conceptual" in q["tags"]}
    problems = []
    for qid in sorted(conceptual):
        if qid not in reviewed:
            problems.append(f"{qid}: not reviewed yet")
        elif "ABCD"[qs[qid]["answer"]] != reviewed[qid]:
            problems.append(f"{qid}: reviewer says {reviewed[qid]}, marked {'ABCD'[qs[qid]['answer']]}")
    for p in problems:
        print("✗", p)
    print(f"{len(conceptual)} conceptual questions; {len(conceptual) - len(problems)} independently re-solved and agree")
    return 1 if problems else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())
