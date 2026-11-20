"""
Write the drafted banks to src/content/<subject>/<topic>.json with balanced answer positions.

    python scripts/authoring/build.py

NOTE: after the initial import, the JSON files are the source of truth (the tutor may edit
them directly). Re-running this script overwrites those JSON files, so only re-run it if
you have not edited the JSON by hand.
"""
from __future__ import annotations

import importlib
import json
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[1]

import qb  # noqa: E402

MODULES = sorted(p.stem for p in HERE.glob("bank_*.py"))


def main() -> None:
    for m in MODULES:
        importlib.import_module(m)
    by_subject: dict[str, list] = {}
    for bank in qb.ALL_BANKS:
        by_subject.setdefault(bank.subject, []).extend(bank.items)
    for subject, items in by_subject.items():
        rng = random.Random(f"positions-{subject}")
        positions = [i % 4 for i in range(len(items))]
        rng.shuffle(positions)
        for item, pos in zip(items, positions):
            correct = item["options"][0]
            wrong = item["options"][1:]
            opts = wrong[:]
            opts.insert(pos, correct)
            item["options"] = opts
            item["answer"] = pos
    files: dict[tuple[str, str], list] = {}
    for bank in qb.ALL_BANKS:
        files.setdefault((bank.subject, bank.topic), []).extend(bank.items)
    for (subject, topic), items in files.items():
        out = ROOT / "src" / "content" / subject / f"{topic}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf8")
        print(f"wrote {out.relative_to(ROOT)} ({len(items)} questions)")


if __name__ == "__main__":
    main()
