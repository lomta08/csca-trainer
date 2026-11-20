"""
Heuristic check that every explanation reaches the marked answer:
the key content of the correct option (its maths, or its main words) must appear in the explanation.
Questions that fail are listed for manual review; reviewed exceptions live in EXPLANATION_REVIEWED.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Read by hand (2026-11-20): these explanations state the answer in other words.
EXPLANATION_REVIEWED = {
    "m-sol-13",
    "m-rat-10",
    "p-es-10",
    "p-dc-11",
    "p-mag-02",
    "p-mag-06",
    "p-ind-07",
    "p-ind-11",
    "p-new-07",
    "p-mom-07",
    "p-cir-06",
    "p-cir-07",
    "p-pe-05",
    "p-pe-09",
    "p-atm-04",
    "p-nuc-06",
    "p-int-03",
    "p-thm-02",
    "p-thm-11",
    "c-eqn-04",
    "c-lab-01",
    "c-lab-07",
    "c-lab-08",
    "c-gasp-01",
    "c-gasp-06",
    "c-gasp-08",
    "c-sep-05",
    "c-ind-07",
    "c-inor-01",
    "c-inor-07",
    "c-inor-08",
    "c-inor-09",
    "c-ion-10",
    "c-atom-05",
    "c-atom-06",
    "c-atom-10",
    "c-bond-01",
    "c-bond-09",
    "c-eq-08",
    "c-eq-10",
    "c-elec-02",
    "c-elec-06",
}


def norm(s):
    s = s.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    s = re.sub(r"\\(left|right|,|;|!| )", "", s)
    s = re.sub(r"\s+|\$", "", s)
    return s.lower()

def math_parts(opt):
    return [norm(m) for m in re.findall(r"\$([^$]+)\$", opt)]

def words(opt):
    txt = re.sub(r"\$[^$]+\$", " ", opt).lower()
    return [w for w in re.findall(r"[a-z]{4,}", txt) if w not in {"with", "that", "which", "than", "only", "from", "then", "into", "they", "their", "when", "each", "both", "same"}]

def ok(q):
    exp = norm(q["explanation"])
    expw = q["explanation"].lower()
    opt = q["options"][q["answer"]]
    parts = math_parts(opt)
    if parts and all(p in exp for p in parts):
        return True
    ws = words(opt)
    if ws and sum(w[:5] in expw for w in ws) >= max(1, (len(ws) + 1) // 2):
        return True
    # numeric answers: the number must appear
    nums = re.findall(r"-?\d+(?:\.\d+)?", opt)
    return bool(nums) and all(n in q["explanation"] for n in nums)

def main():
    fails = []
    total = 0
    for subj in ["math", "physics", "chemistry"]:
        for f in sorted((ROOT / "src" / "content" / subj).glob("*.json")):
            for q in json.loads(f.read_text(encoding="utf8")):
                total += 1
                if not ok(q) and q["id"] not in EXPLANATION_REVIEWED:
                    fails.append(q)
    for q in fails:
        print(f"{q['id']}: answer {q['options'][q['answer']]!r}")
    print(f"{total - len(fails)}/{total} explanations contain the marked answer; {len(fails)} need manual review")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
