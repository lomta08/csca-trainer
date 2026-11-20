import importlib
import sys
from pathlib import Path

AUTH = Path(__file__).resolve().parents[1] / "authoring"


def load_checks(subject: str) -> dict:
    sys.path.insert(0, str(AUTH))
    import qb  # noqa: F401
    out: dict = {}
    for p in sorted(AUTH.glob(f"bank_{subject}_*.py")):
        mod = importlib.import_module(p.stem)
        out.update(mod.B.checks)
    return out
