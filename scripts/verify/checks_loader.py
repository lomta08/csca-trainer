import importlib
import sys
from pathlib import Path

AUTH = Path(__file__).resolve().parents[1] / "authoring"


def load_checks(subject: str) -> dict:
    """Collect the numeric checks from every Bank defined in scripts/authoring/bank_<subject>_*.py."""
    sys.path.insert(0, str(AUTH))
    import qb
    out: dict = {}
    for p in sorted(AUTH.glob(f"bank_{subject}_*.py")):
        mod = importlib.import_module(p.stem)
        for v in vars(mod).values():
            if isinstance(v, qb.Bank):
                out.update(v.checks)
    return out
