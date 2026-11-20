"""
Authoring helpers used to draft the initial question bank.

Each bank module creates `B = Bank(subject, topic)` and calls `B.q(...)` with the
CORRECT OPTION FIRST. `build.py` then writes src/content/<subject>/<topic>.json,
placing the correct option so that A/B/C/D are evenly used.

A question with `check=` is numerically verified by scripts/verify/run_all.py.
A question without a check is tagged "conceptual" and was second-pass reviewed by hand.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "verify"))
from vlib import *  # noqa: F401,F403,E402  (re-exported for bank modules)

ALL_BANKS: list["Bank"] = []


class Bank:
    def __init__(self, subject: str, topic: str):
        self.subject = subject
        self.topic = topic
        self.items: list[dict] = []
        self.checks: dict = {}
        ALL_BANKS.append(self)

    def q(self, id: str, subtopic: str, difficulty: int, question: str, options: list[str], explanation: str, check=None, tags=()):
        assert len(options) == 4, id
        assert difficulty in (1, 2, 3), id
        tags = list(tags)
        if check is None:
            tags.append("conceptual")
        else:
            tags.append("numeric")
            self.checks[id] = check
        self.items.append({
            "id": id,
            "subject": self.subject,
            "topic": self.topic,
            "subtopic": subtopic,
            "difficulty": difficulty,
            "question": question.strip(),
            "options": [o.strip() for o in options],
            "answer": 0,
            "explanation": explanation.strip(),
            "tags": tags,
        })
