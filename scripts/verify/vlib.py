"""
Verification helpers. Each check recomputes an answer from the question's givens
(with sympy / plain Python) and decides whether an option string matches it.

The runner (run_all.py) asserts that exactly one option matches and that it is the
marked answer.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "src" / "content"

TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)
x, y, z, n, t, a, b, k, m, p = sp.symbols("x y z n t a b k m p")
LOCALS = {"x": x, "y": y, "z": z, "n": n, "t": t, "a": a, "b": b, "k": k, "m": m, "p": p, "pi": sp.pi, "oo": sp.oo,
          "sqrt": sp.sqrt, "log": sp.log, "ln": sp.log, "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
          "e": sp.E, "E": sp.E, "root": sp.root, "Abs": sp.Abs}


def load_questions(subject: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted((CONTENT / subject).glob("*.json")):
        for q in json.loads(f.read_text(encoding="utf8")):
            out[q["id"]] = q
    return out


# ---------------------------------------------------------------------------
# LaTeX → sympy

def _match_brace(s: str, i: int) -> int:
    """s[i] == '{' ; return index of matching '}'."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    raise ValueError(f"unbalanced braces in {s!r}")


def _arg(s: str, i: int) -> tuple[str, int]:
    """Read a LaTeX argument starting at i (either {...} or a single token). Returns (content, next index)."""
    while i < len(s) and s[i] == " ":
        i += 1
    if s[i] == "{":
        j = _match_brace(s, i)
        return s[i + 1 : j], j + 1
    if s[i] == "\\":
        mm = re.match(r"\\[A-Za-z]+", s[i:])
        return mm.group(0), i + len(mm.group(0))
    return s[i], i + 1


UNIT_COMMANDS = [r"\Omega", r"^{\circ}", r"^\circ", r"\degree", r"\%", r"\mu ", r"\micro", r"°", "℃", "Ω", "μ", "%"]


def clean(s: str, keep_text: bool = False) -> str:
    s = s.replace("$", "")
    s = re.sub(r"\\(left|right|displaystyle|big|Big|bigg)", "", s)
    s = s.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    s = re.sub(r"\\[,;:! ]", " ", s)
    s = s.replace("~", " ")
    if not keep_text:
        # drop \text{...} and \mathrm{...} (units, words)
        s = re.sub(r"\\(text|mathrm|textrm|operatorname)\{[^{}]*\}", " ", s)
    return s.strip()


def latex_to_py(s: str, complex_i: bool = False) -> str:
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if s.startswith(r"\frac", i):
            num, i = _arg(s, i + 5)
            den, i = _arg(s, i)
            out.append(f"(({latex_to_py(num, complex_i)})/({latex_to_py(den, complex_i)}))")
            continue
        if s.startswith(r"\sqrt", i):
            i += 5
            if i < len(s) and s[i] == "[":
                j = s.index("]", i)
                idx = s[i + 1 : j]
                i = j + 1
                rad, i = _arg(s, i)
                out.append(f"root({latex_to_py(rad, complex_i)},{idx})")
            else:
                rad, i = _arg(s, i)
                out.append(f"sqrt({latex_to_py(rad, complex_i)})")
            continue
        if s.startswith(r"\log_", i):
            base, i = _arg(s, i + 5)
            argument, i = _arg(s, i)
            out.append(f"log({latex_to_py(argument, complex_i)},{latex_to_py(base, complex_i)})")
            continue
        if c == "^":
            ex, i = _arg(s, i + 1)
            out.append(f"**({latex_to_py(ex, complex_i)})")
            continue
        if c == "_":  # subscripts are not used numerically
            _, i = _arg(s, i + 1)
            continue
        if c == "\\":
            mm = re.match(r"\\([A-Za-z]+)", s[i:])
            if not mm:
                i += 1
                continue
            cmd = mm.group(1)
            i += len(mm.group(0))
            rep = {"pi": " pi ", "cdot": "*", "times": "*", "infty": "oo", "ln": "ln", "lg": "log10", "sin": "sin",
                   "cos": "cos", "tan": "tan", "div": "/", "approx": "", "pm": "+-", "mid": "|", "le": "<=", "ge": ">=",
                   "leq": "<=", "geq": ">=", "lt": "<", "gt": ">", "neq": "!=", "ne": "!="}.get(cmd)
            if rep is None:
                raise ValueError(f"unsupported command \\{cmd}")
            out.append(rep)
            continue
        if c in "{}":
            out.append("(" if c == "{" else ")")
            i += 1
            continue
        if c == "i" and complex_i:
            out.append(" I ")
            i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


UNIT_TEXT = re.compile(r"(\\cdot|\\times)?\s*\\(text|mathrm)\{[^{}]*\}(\^\{?-?\d+\}?)?")


def to_sympy(tex: str, complex_i: bool = False, strip_units: bool = True):
    if strip_units:
        prev = None
        while prev != tex:
            prev, tex = tex, UNIT_TEXT.sub(" ", tex)
    s = clean(tex)
    if strip_units:
        s = re.sub(r"(\\cdot|\\times)\s*$", "", s.strip())
        for u in UNIT_COMMANDS:
            s = s.replace(u, " ")
        # remove plain unit words (not LaTeX commands): e.g. "12 m/s^2", "3.0 mol/L"
        s = re.sub(r"(?<![\\A-Za-z])[A-Za-z][A-Za-z·/]*(\^\{?-?\d\}?)?(?:/[A-Za-z]+(\^\{?-?\d\}?)?)*", " ", s)
        s = s.strip()
    py = latex_to_py(s, complex_i).replace("log10", "LOGTEN")
    py = py.replace("LOGTEN", "log10")
    loc = dict(LOCALS)
    loc["log10"] = lambda v: sp.log(v, 10)
    loc["I"] = sp.I
    return parse_expr(py, local_dict=loc, transformations=TRANSFORMS, evaluate=True)


def to_expr(tex: str, complex_i: bool = False):
    """Parse an algebraic expression (variables kept)."""
    s = clean(tex)
    py = latex_to_py(s, complex_i)
    loc = dict(LOCALS)
    loc["log10"] = lambda v: sp.log(v, 10)
    loc["I"] = sp.I
    return parse_expr(py, local_dict=loc, transformations=TRANSFORMS, evaluate=True)


# ---------------------------------------------------------------------------
# checks

class Check:
    def match(self, opt: str) -> bool:  # pragma: no cover
        raise NotImplementedError

    def describe(self) -> str:
        return self.__class__.__name__


class N(Check):
    """Numeric value. rel: relative tolerance (options are often rounded)."""

    def __init__(self, value, rel: float = 1e-9, abs_tol: float = 1e-12, complex_i: bool = False):
        self.value = complex(sp.N(value)) if complex_i else float(sp.N(value))
        self.rel, self.abs_tol, self.complex_i = rel, abs_tol, complex_i

    def match(self, opt: str) -> bool:
        v = to_sympy(opt, complex_i=self.complex_i, strip_units=not self.complex_i)
        v = complex(sp.N(v)) if self.complex_i else float(sp.N(v))
        tol = self.rel * abs(self.value) if self.value != 0 else self.abs_tol
        return abs(v - self.value) <= tol

    def describe(self) -> str:
        return f"N({self.value:g})"


def R(value, rel: float = 0.02):
    """Rounded numeric answer (physics/chemistry): 2 % tolerance by default."""
    return N(value, rel=rel)


class Expr(Check):
    """Algebraic expression in x (or other symbols) equal to `expr`."""

    def __init__(self, expr, complex_i: bool = False):
        self.expr = sp.sympify(expr)
        self.complex_i = complex_i

    def match(self, opt: str) -> bool:
        s = clean(opt)
        if "=" in s:
            s = s.split("=")[-1]
        e = to_expr(s, self.complex_i)
        return sp.simplify(e - self.expr) == 0


class Eqn(Check):
    """Equation (line, circle, conic): lhs-rhs proportional to `expr` (= 0)."""

    def __init__(self, expr):
        self.expr = sp.expand(sp.sympify(expr))

    def match(self, opt: str) -> bool:
        s = clean(opt)
        if "=" not in s:
            return False
        lhs, rhs = s.split("=", 1)
        e = sp.expand(to_expr(lhs) - to_expr(rhs))
        if e == 0:
            return False
        ratio = sp.simplify(e / self.expr)
        return ratio.free_symbols == set() and ratio != 0


class Pt(Check):
    """Point / tuple of numbers, e.g. (1,-2)."""

    def __init__(self, *coords):
        self.coords = [float(sp.N(c)) for c in coords]

    def match(self, opt: str) -> bool:
        s = clean(opt).strip()
        if not (s.startswith("(") and s.endswith(")")):
            return False
        parts = _split_top(s[1:-1])
        if len(parts) != len(self.coords):
            return False
        return all(abs(float(sp.N(to_sympy(p))) - c) < 1e-9 for p, c in zip(parts, self.coords))


def _split_top(s: str) -> list[str]:
    parts, depth, cur = [], 0, ""
    for ch in s:
        if ch in "({[":
            depth += 1
        elif ch in ")}]":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return parts


def parse_set(opt: str):
    s = clean(opt).replace(" ", "")
    s = s.replace(r"\{", "{").replace(r"\}", "}")
    if s in (r"\varnothing", r"\emptyset", "∅"):
        return sp.EmptySet
    if s == r"\mathbb{R}" or s == r"\mathbf{R}":
        return sp.Reals
    if s.startswith("{x|") or s.startswith(r"{x\mid"):
        body = s[s.index("|") + 1 : -1] if "|" in s else s[len(r"{x\mid") : -1]
        return _setbuilder(body)
    s = s.replace("and", "\\cup")
    pieces = re.split(r"\\cup", s)
    result = sp.EmptySet
    for p in pieces:
        if p.startswith("{"):
            items = [to_sympy(v) for v in _split_top(p[1:-1]) if v != ""]
            result = sp.Union(result, sp.FiniteSet(*items))
            continue
        mm = re.match(r"^([\[(])(.+)([\])])$", p)
        if not mm:
            raise ValueError(f"bad set {opt}")
        lo_s, hi_s = _split_top(mm.group(2))
        lo = -sp.oo if "infty" in lo_s else to_sympy(lo_s)
        hi = sp.oo if "infty" in hi_s else to_sympy(hi_s)
        result = sp.Union(result, sp.Interval(lo, hi, left_open=mm.group(1) == "(", right_open=mm.group(3) == ")"))
    return result


def _setbuilder(body: str):
    alts = re.split(r"\\text\{or\}|or|\\vee", body)
    result = sp.EmptySet
    for alt in alts:
        cond = latex_to_py(alt)
        # chain like -1<x<=3
        toks = re.split(r"(<=|>=|<|>)", cond)
        sset = sp.Reals
        vals = [to_sympy(tk) if tk.strip() != "x" else None for tk in toks[0::2]]
        ops = toks[1::2]
        for j, op in enumerate(ops):
            left, right = vals[j], vals[j + 1]
            if left is None:  # x op right
                iv = {"<": sp.Interval.open(-sp.oo, right), "<=": sp.Interval(-sp.oo, right), ">": sp.Interval.open(right, sp.oo), ">=": sp.Interval(right, sp.oo)}[op]
            else:  # left op x
                iv = {"<": sp.Interval.open(left, sp.oo), "<=": sp.Interval(left, sp.oo), ">": sp.Interval.open(-sp.oo, left), ">=": sp.Interval(-sp.oo, left)}[op]
            sset = sp.Intersection(sset, iv)
        result = sp.Union(result, sset)
    return result


class S(Check):
    """Set / interval answer."""

    def __init__(self, value):
        self.value = value

    def match(self, opt: str) -> bool:
        got = parse_set(opt)
        return sp.simplify(sp.SymmetricDifference(got, self.value)) == sp.EmptySet or got == self.value


class T(Check):
    """Text answer computed by the check script (normalised compare)."""

    def __init__(self, text: str):
        self.text = norm_text(text)

    def match(self, opt: str) -> bool:
        return norm_text(opt) == self.text


def norm_text(s: str) -> str:
    return re.sub(r"[\s$]", "", s).replace(r"\dfrac", r"\frac").lower()


class Fn(Check):
    """Custom predicate on the raw option text."""

    def __init__(self, fn, label: str = "custom"):
        self.fn, self.label = fn, label

    def match(self, opt: str) -> bool:
        return bool(self.fn(opt))


def first_number(opt: str) -> float:
    """First number in an option (handles a×10^b)."""
    s = clean(opt)
    mm = re.search(r"-?\d+(?:\.\d+)?(?:\s*\\times\s*10\^\{?(-?\d+)\}?)?", s)
    if not mm:
        raise ValueError(f"no number in {opt}")
    base = float(re.match(r"-?\d+(?:\.\d+)?", mm.group(0)).group(0))
    return base * (10 ** int(mm.group(1)) if mm.group(1) else 1)


def Num(value, rel: float = 0.02):
    """Match on the first number in the option text (for options mixing words and numbers)."""
    v = float(value)
    return Fn(lambda o: abs(first_number(o) - v) <= (rel * abs(v) if v else 1e-12), f"Num({v:g})")


def contains(*parts: str):
    """Option contains every given substring (after removing spaces and $) — use only for computed text."""
    ps = [norm_text(p) for p in parts]
    return Fn(lambda o: all(p in norm_text(o) for p in ps), f"contains{parts}")


def numbers(opt: str) -> list[float]:
    """All numbers in an option, in order (LaTeX fractions/roots inside $…$ are evaluated)."""
    vals: list[float] = []
    for seg in re.findall(r"\$([^$]+)\$", opt) or [opt]:
        try:
            vals.append(float(sp.N(to_sympy(seg))))
        except Exception:
            vals.extend(float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", seg))
    return vals


def Nums(*values, rel: float = 1e-9):
    """Option contains exactly these numbers in this order (e.g. "mean $16$, variance $18$")."""
    want = [float(sp.N(v)) for v in values]
    def f(o: str) -> bool:
        got = numbers(o)
        return len(got) == len(want) and all(abs(g - w) <= (rel * abs(w) if w else 1e-12) for g, w in zip(got, want))
    return Fn(f, f"Nums{tuple(want)}")


def CR(cx, cy, r):
    """'centre $(a,b)$, radius $r$' options."""
    return Nums(cx, cy, r)


PM = "\\pm"


def Foci(c, axis: str = "x"):
    r"""Options like $(\pm 4,0)$ or $(0,\pm\sqrt{5})$."""
    cv = float(sp.N(c))
    def f(o: str) -> bool:
        s = clean(o).replace(" ", "")
        if not (s.startswith("(") and s.endswith(")")):
            return False
        u, v = _split_top(s[1:-1])
        if axis == "x":
            return v == "0" and u.startswith(PM) and abs(float(sp.N(to_sympy(u[3:]))) - cv) < 1e-9
        return u == "0" and v.startswith(PM) and abs(float(sp.N(to_sympy(v[3:]))) - cv) < 1e-9
    return Fn(f, f"Foci({cv:g},{axis})")


def Asym(slope):
    r"""Options like $y=\pm\frac{4}{3}x$."""
    sv = float(sp.N(slope))
    def f(o: str) -> bool:
        s = clean(o).replace(" ", "")
        if not s.startswith("y=" + PM):
            return False
        body = s[len("y=" + PM):]
        if not body.endswith("x"):
            return False
        body = body[:-1]
        val = 1.0 if body == "" else float(sp.N(to_sympy(body)))
        return abs(val - sv) < 1e-9
    return Fn(f, f"Asym({sv:g})")
