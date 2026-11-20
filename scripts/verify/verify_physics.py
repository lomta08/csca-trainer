"""Numeric checks for physics. Checks for the initial bank live next to each question in
scripts/authoring/bank_physics_*.py; add checks for questions you write directly in JSON to EXTRA."""
from checks_loader import load_checks

EXTRA: dict = {}
CHECKS = {**load_checks("physics"), **EXTRA}
