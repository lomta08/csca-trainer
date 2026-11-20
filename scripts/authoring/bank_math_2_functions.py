from statistics import NormalDist  # noqa: F401
from qb import *  # noqa: F403

B = Bank("math", "functions")
R_ = sp.S.Reals


def sol(expr, v=x):
    return sp.solveset(expr, v, R_)


def is_odd(expr_tex):
    e = to_expr(expr_tex.split("=")[-1])
    return sp.simplify(e.subs(x, -x) + e) == 0 and sp.simplify(e.subs(x, -x) - e) != 0


def order_text(vals: dict) -> str:
    return "<".join(sorted(vals, key=lambda kk: float(vals[kk])))


# ------------------------------------------- domain, range, monotonicity, parity
B.q("m-fun-01", "function-properties", 2,
    r"The domain of $f(x)=\dfrac{\sqrt{x+1}}{x-2}$ is",
    [r"$[-1,2)\cup(2,+\infty)$", r"$[-1,+\infty)$", r"$(-1,2)\cup(2,+\infty)$", r"$(2,+\infty)$"],
    r"""Two conditions: the square root needs $x+1\ge0$, i.e. $x\ge-1$; the denominator needs $x\ne2$.

Domain: $[-1,2)\cup(2,+\infty)$.""",
    S(sp.Complement(sol(x + 1 >= 0), sp.FiniteSet(2))))

B.q("m-fun-02", "function-properties", 2,
    r"The domain of $f(x)=\lg(3-x)+\dfrac{1}{\sqrt{x+2}}$ is",
    [r"$(-2,3)$", r"$[-2,3)$", r"$(-2,3]$", r"$(-\infty,3)$"],
    r"""- $\lg(3-x)$ needs $3-x>0$, so $x<3$.
- $\dfrac1{\sqrt{x+2}}$ needs $x+2>0$ (a square root in a denominator must be **strictly** positive), so $x>-2$.

Domain: $(-2,3)$.""",
    S(sp.Intersection(sol(3 - x > 0), sol(x + 2 > 0))))

_pw = sp.Piecewise((x ** 2 + 1, x <= 0), (2 * x, True))
B.q("m-fun-03", "function-properties", 2,
    r"Let $f(x)=\begin{cases}x^2+1,&x\le0\\2x,&x>0\end{cases}$. Then $f(f(-1))=$",
    [r"$4$", r"$2$", r"$5$", r"$3$"],
    r"Work from the inside: $-1\le0$, so $f(-1)=(-1)^2+1=2$. Then $2>0$, so $f(2)=2\cdot2=4$.",
    N(_pw.subs(x, _pw.subs(x, -1))))

B.q("m-fun-04", "function-properties", 1,
    r"Which of the following functions is odd?",
    [r"$f(x)=x^3+x$", r"$f(x)=x^2+1$", r"$f(x)=x+1$", r"$f(x)=x^4-x^2$"],
    r"""A function is odd if $f(-x)=-f(x)$ for all $x$ in a symmetric domain.

$(-x)^3+(-x)=-(x^3+x)$ ✔. The functions $x^2+1$ and $x^4-x^2$ are even, and $x+1$ is neither ($f(-1)=0$ but $-f(1)=-2$).""",
    Fn(is_odd, "is_odd"))

B.q("m-fun-05", "function-properties", 2,
    r"Which function is **even** and **increasing** on $(0,+\infty)$?",
    [r"$y=x^2+1$", r"$y=x^3$", r"$y=-x^2$", r"$y=2^x$"],
    r"""- $y=x^2+1$: even, and increasing for $x>0$ ✔
- $y=x^3$: odd.
- $y=-x^2$: even but **decreasing** on $(0,+\infty)$.
- $y=2^x$: neither even nor odd.""")

_f6 = lambda v: v ** 2 + 2 * v  # noqa: E731
B.q("m-fun-06", "function-properties", 2,
    r"$f(x)$ is an odd function on $\mathbb{R}$, and $f(x)=x^2+2x$ for $x>0$. Then $f(-1)=$",
    [r"$-3$", r"$3$", r"$-1$", r"$1$"],
    r"For an odd function $f(-1)=-f(1)$. Since $1>0$, $f(1)=1+2=3$. Therefore $f(-1)=-3$. (Substituting $-1$ into $x^2+2x$ gives $-1$, which is wrong: that formula only holds for $x>0$.)",
    N(-_f6(1)))

B.q("m-fun-07", "function-properties", 2,
    r"$f(x)$ is an even function on $\mathbb{R}$, and $f(x)=2^x-1$ for $x\ge0$. Then $f(-2)=$",
    [r"$3$", r"$-\dfrac34$", r"$-3$", r"$\dfrac34$"],
    r"Even means $f(-x)=f(x)$, so $f(-2)=f(2)=2^2-1=3$.",
    N(2 ** 2 - 1))

B.q("m-fun-08", "function-properties", 2,
    r"The range of $y=x^2-2x+3$ ($x\in\mathbb{R}$) is",
    [r"$[2,+\infty)$", r"$[3,+\infty)$", r"$(2,+\infty)$", r"$\mathbb{R}$"],
    r"Complete the square: $y=(x-1)^2+2\ge2$, with equality at $x=1$. So the range is $[2,+\infty)$.",
    S(sp.Interval(sp.minimum(x ** 2 - 2 * x + 3, x, R_), sp.oo)))

_f9 = x ** 2 - 4 * x + 1
B.q("m-fun-09", "function-properties", 3,
    r"The range of $f(x)=x^2-4x+1$ on the interval $[0,3]$ is",
    [r"$[-3,1]$", r"$[-2,1]$", r"$[-3,-2]$", r"$[1,3]$"],
    r"""$f(x)=(x-2)^2-3$. The vertex $x=2$ lies inside $[0,3]$, so the minimum is $f(2)=-3$.

The maximum is at the endpoint farther from $2$: $f(0)=1$ (while $f(3)=-2$). Range: $[-3,1]$.

Trap: using only the endpoints gives $[-2,1]$.""",
    S(sp.Interval(sp.minimum(_f9, x, sp.Interval(0, 3)), sp.maximum(_f9, x, sp.Interval(0, 3)))))

B.q("m-fun-10", "function-properties", 3,
    r"$f(x)=x^2+2(a-1)x+2$ is decreasing on $(-\infty,4]$. The range of $a$ is",
    [r"$(-\infty,-3]$", r"$[-3,+\infty)$", r"$(-\infty,3]$", r"$[5,+\infty)$"],
    r"""The parabola opens upward with axis $x=1-a$ and is decreasing on $(-\infty,1-a]$.

For it to be decreasing on all of $(-\infty,4]$ we need $4\le1-a$, i.e. $a\le-3$.""",
    S(sp.solveset(1 - a >= 4, a, R_)))

B.q("m-fun-11", "function-properties", 2,
    r"If $f(x+1)=x^2+2x$, then $f(x)=$",
    [r"$x^2-1$", r"$x^2+1$", r"$x^2-2x$", r"$x^2+4x+3$"],
    r"""Let $t=x+1$, so $x=t-1$:
$$f(t)=(t-1)^2+2(t-1)=t^2-2t+1+2t-2=t^2-1.$$
Rename the variable: $f(x)=x^2-1$.""",
    Expr(sp.expand((x - 1) ** 2 + 2 * (x - 1))))

B.q("m-fun-12", "function-properties", 2,
    r"For all real $x$, $f(x+2)=-f(x)$. The smallest positive period of $f(x)$ (if $f$ is not constant) is",
    [r"$4$", r"$2$", r"$1$", r"$8$"],
    r"Apply the rule twice: $f(x+4)=f((x+2)+2)=-f(x+2)=-(-f(x))=f(x)$. So $4$ is a period. (Shifting by $2$ changes the sign, so $2$ is not a period unless $f\equiv0$.)")

B.q("m-fun-13", "function-properties", 2,
    r"$f(x)$ is an odd function on $\mathbb{R}$ with period $4$, and $f(1)=2$. Then $f(7)=$",
    [r"$-2$", r"$2$", r"$0$", r"$7$"],
    r"Use the period to move close to $0$: $f(7)=f(7-8)=f(-1)$. Then oddness gives $f(-1)=-f(1)=-2$.",
    N(-2 if (7 % 4) == 3 else (2 if (7 % 4) == 1 else 0)))

B.q("m-fun-14", "function-properties", 1,
    r"Which statement about $f(x)=\dfrac1x$ is correct?",
    [r"$f(x)$ is decreasing on $(0,+\infty)$", r"$f(x)$ is decreasing on its whole domain", r"$f(x)$ is increasing on $(-\infty,0)$", r"$f(x)$ is an even function"],
    r"""$f$ decreases on $(-\infty,0)$ and on $(0,+\infty)$ **separately**, but not on the whole domain: for example $f(-1)=-1<f(1)=1$ although $-1<1$.

It is odd, not even, since $f(-x)=-f(x)$.""")

_f15 = (a * 2 ** x - 1) / (2 ** x + 1)
_a15 = sp.solve(_f15.subs(x, 0), a)[0]
B.q("m-fun-15", "function-properties", 3,
    r"If $f(x)=\dfrac{a\cdot2^x-1}{2^x+1}$ is an odd function on $\mathbb{R}$, then $a=$",
    [r"$1$", r"$-1$", r"$2$", r"$0$"],
    r"""An odd function defined at $0$ has $f(0)=0$: $\dfrac{a-1}{2}=0$, so $a=1$.

Check: $f(x)=\dfrac{2^x-1}{2^x+1}$; multiplying top and bottom of $f(-x)$ by $2^x$ gives $\dfrac{1-2^x}{1+2^x}=-f(x)$ ✔.""",
    N(_a15) if sp.simplify(_f15.subs(a, _a15).subs(x, -x) + _f15.subs(a, _a15)) == 0 else N(999))

B.q("m-fun-16", "function-properties", 2,
    r"For $f(x)=\ln(x^2+1)$, which statement is correct?",
    [r"$f$ is even and increasing on $(0,+\infty)$", r"$f$ is odd and increasing on $(0,+\infty)$", r"$f$ is even and decreasing on $(0,+\infty)$", r"$f$ is neither even nor odd"],
    r"""$f(-x)=\ln((-x)^2+1)=f(x)$, so $f$ is even.

On $(0,+\infty)$, $x^2+1$ increases and $\ln$ is increasing, so $f$ increases there.""")

B.q("m-fun-17", "function-properties", 3,
    r"$f(x)$ is even on $\mathbb{R}$, increasing on $[0,+\infty)$, and $f(2)=0$. The solution set of $f(x-1)<0$ is",
    [r"$(-1,3)$", r"$(-2,2)$", r"$(1,3)$", r"$(-\infty,-1)\cup(3,+\infty)$"],
    r"""Because $f$ is even and increasing on $[0,\infty)$, $f(t)<0=f(2)\iff |t|<2$.

So $f(x-1)<0\iff|x-1|<2\iff-1<x<3$.""",
    S(sol(sp.Abs(x - 1) < 2)))

B.q("m-fun-18", "function-properties", 2,
    r"The domain of $f(x)=\sqrt{4-x^2}$ is",
    [r"$[-2,2]$", r"$(-2,2)$", r"$[0,2]$", r"$(-\infty,-2]\cup[2,+\infty)$"],
    r"We need $4-x^2\ge0$, i.e. $x^2\le4$, so $-2\le x\le2$.",
    S(sol(4 - x ** 2 >= 0)))

_f19 = x / (x ** 2 + 1)
B.q("m-fun-19", "function-properties", 3,
    r"For $x>0$, the maximum value of $f(x)=\dfrac{x}{x^2+1}$ is",
    [r"$\dfrac12$", r"$1$", r"$2$", r"$\dfrac14$"],
    r"""Divide top and bottom by $x>0$: $f(x)=\dfrac{1}{x+\frac1x}$. By AM–GM $x+\dfrac1x\ge2$, so $f(x)\le\dfrac12$, with equality at $x=1$.""",
    N(sp.maximum(_f19, x, sp.Interval.open(0, sp.oo))))

_ff = lambda v: 2 * v + 1  # noqa: E731
_gg = lambda v: v ** 2  # noqa: E731
B.q("m-fun-20", "function-properties", 2,
    r"Let $f(x)=2x+1$ and $g(x)=x^2$. Then $f(g(2))-g(f(2))=$",
    [r"$-16$", r"$16$", r"$0$", r"$-4$"],
    r"$f(g(2))=f(4)=9$ and $g(f(2))=g(5)=25$, so the difference is $9-25=-16$. Composition is not commutative.",
    N(_ff(_gg(2)) - _gg(_ff(2))))

# ------------------------------------------- power, exponential, logarithmic
B.q("m-exp-01", "elementary-functions", 1,
    r"$\log_2 32=$",
    [r"$5$", r"$16$", r"$4$", r"$6$"],
    r"$32=2^5$, so $\log_2 32=5$.",
    N(sp.log(32, 2)))

B.q("m-exp-02", "elementary-functions", 1,
    r"$27^{\frac23}=$",
    [r"$9$", r"$18$", r"$3$", r"$\dfrac19$"],
    r"$27^{\frac23}=\left(27^{\frac13}\right)^2=3^2=9$.",
    N(sp.Integer(27) ** sp.Rational(2, 3)))

B.q("m-exp-03", "elementary-functions", 1,
    r"$\lg 25+\lg 4=$",
    [r"$2$", r"$\lg 29$", r"$100$", r"$1$"],
    r"$\lg25+\lg4=\lg(25\times4)=\lg100=2$.",
    N(sp.log(25, 10) + sp.log(4, 10)))

B.q("m-exp-04", "elementary-functions", 1,
    r"$\log_3 18-\log_3 2=$",
    [r"$2$", r"$\log_3 16$", r"$9$", r"$3$"],
    r"$\log_3 18-\log_3 2=\log_3\dfrac{18}{2}=\log_3 9=2$.",
    N(sp.log(18, 3) - sp.log(2, 3)))

B.q("m-exp-05", "elementary-functions", 2,
    r"$2^{\log_2 5}+\ln e^{2}=$",
    [r"$7$", r"$5$", r"$10$", r"$3$"],
    r"By definition $a^{\log_a N}=N$, so $2^{\log_2 5}=5$; and $\ln e^2=2$. Total: $7$.",
    N(5 + sp.log(sp.E ** 2)))

_v6 = {"a": sp.Integer(2) ** sp.Rational(3, 10), "b": sp.Rational(3, 10) ** 2, "c": sp.log(sp.Rational(3, 10), 2)}
B.q("m-exp-06", "elementary-functions", 2,
    r"Let $a=2^{0.3}$, $b=0.3^{2}$, $c=\log_2 0.3$. Then",
    [r"$c<b<a$", r"$a<b<c$", r"$b<c<a$", r"$c<a<b$"],
    r"""Compare with $0$ and $1$:
- $a=2^{0.3}>2^0=1$;
- $b=0.3^2=0.09\in(0,1)$;
- $c=\log_2 0.3<\log_2 1=0$.

So $c<b<a$.""",
    T(order_text(_v6)))

B.q("m-exp-07", "elementary-functions", 2,
    r"For any $a>0$, $a\ne1$, the graph of $y=a^{x-1}+2$ always passes through the point",
    [r"$(1,3)$", r"$(0,3)$", r"$(1,2)$", r"$(0,1)$"],
    r"$a^0=1$ for every valid $a$. Make the exponent $0$: $x=1$, then $y=1+2=3$. Fixed point $(1,3)$.",
    Pt(1, sp.Integer(1) + 2))

B.q("m-exp-08", "elementary-functions", 2,
    r"For any $a>0$, $a\ne1$, the graph of $y=\log_a(x+3)-1$ always passes through the point",
    [r"$(-2,-1)$", r"$(-3,-1)$", r"$(-2,0)$", r"$(1,-1)$"],
    r"$\log_a1=0$ for every base. Make the argument $1$: $x+3=1\Rightarrow x=-2$, then $y=0-1=-1$. Fixed point $(-2,-1)$.",
    Pt(sp.solve(x + 3 - 1, x)[0], -1))

B.q("m-exp-09", "elementary-functions", 3,
    r"The solution set of $\log_2(x-1)<1$ is",
    [r"$(1,3)$", r"$(-\infty,3)$", r"$(0,3)$", r"$(3,+\infty)$"],
    r"""Remember the domain: $x-1>0$. Since $\log_2$ is increasing, $\log_2(x-1)<1=\log_2 2\iff x-1<2$.

So $0<x-1<2$, i.e. $1<x<3$. (Forgetting the domain gives $(-\infty,3)$.)""",
    S(sp.Intersection(sol(x - 1 > 0), sol(x - 1 < 2))))

_r10 = [r for r in sp.solve(t ** 2 - 3 * t - 4, t) if r > 0]
B.q("m-exp-10", "elementary-functions", 2,
    r"The real solution of $4^x-3\cdot2^x-4=0$ is",
    [r"$x=2$", r"$x=-1$", r"$x=2$ or $x=-1$", r"$x=4$"],
    r"""Let $t=2^x>0$. Then $4^x=t^2$ and $t^2-3t-4=0$, so $(t-4)(t+1)=0$.

$t=-1$ is impossible because $2^x>0$. So $2^x=4$ and $x=2$.""",
    Fn(lambda o: clean(o).replace(" ", "") == f"x={sp.log(_r10[0], 2)}", "x=2 only"))

_al = sp.solve(sp.Integer(4) ** a - 2, a)[0]
B.q("m-exp-11", "elementary-functions", 2,
    r"The graph of the power function $f(x)=x^{\alpha}$ passes through $(4,2)$. Then $f(9)=$",
    [r"$3$", r"$81$", r"$\dfrac92$", r"$18$"],
    r"$4^\alpha=2\Rightarrow \alpha=\dfrac12$, so $f(x)=\sqrt x$ and $f(9)=3$.",
    N(sp.Integer(9) ** _al))

B.q("m-exp-12", "elementary-functions", 3,
    r"The increasing interval of $y=\log_{\frac12}(x^2-2x-3)$ is",
    [r"$(-\infty,-1)$", r"$(3,+\infty)$", r"$(-\infty,1)$", r"$(1,+\infty)$"],
    r"""Domain first: $x^2-2x-3>0\Rightarrow x<-1$ or $x>3$.

The outer function $\log_{\frac12}u$ is **decreasing**, so $y$ increases where $u=x^2-2x-3$ decreases. Inside the domain $u$ decreases on $(-\infty,-1)$.

Increasing interval: $(-\infty,-1)$. (Answers like $(-\infty,1)$ forget the domain.)""")

B.q("m-exp-13", "elementary-functions", 2,
    r"Which function is decreasing on $(0,+\infty)$?",
    [r"$y=\left(\dfrac12\right)^x$", r"$y=2^x$", r"$y=\log_2 x$", r"$y=x^{\frac12}$"],
    r"An exponential $a^x$ is decreasing when $0<a<1$, so $y=\left(\tfrac12\right)^x$ decreases. The other three are all increasing on $(0,+\infty)$.")

_a14 = sp.log(6, 2)
_b14 = sp.log(6, 3)
B.q("m-exp-14", "elementary-functions", 3,
    r"If $2^a=3^b=6$, then $\dfrac1a+\dfrac1b=$",
    [r"$1$", r"$6$", r"$\dfrac16$", r"$5$"],
    r"""$a=\log_2 6$ and $b=\log_3 6$, so $\dfrac1a=\log_6 2$ and $\dfrac1b=\log_6 3$ (change of base: $\dfrac1{\log_a b}=\log_b a$).

$\dfrac1a+\dfrac1b=\log_62+\log_63=\log_66=1$.""",
    N(sp.nsimplify(sp.N(1 / _a14 + 1 / _b14, 30))))

B.q("m-exp-15", "elementary-functions", 1,
    r"$\log_2 3\cdot\log_3 4=$",
    [r"$2$", r"$\log_2 7$", r"$12$", r"$1$"],
    r"Change of base: $\log_23\cdot\log_34=\dfrac{\lg3}{\lg2}\cdot\dfrac{\lg4}{\lg3}=\dfrac{\lg4}{\lg2}=\log_24=2$.",
    N(sp.nsimplify(sp.N(sp.log(3, 2) * sp.log(4, 3), 30))))

# candidate bases from log_a 2 = ±1, plus decoys; keep those that satisfy the condition
_avals16 = [sp.Integer(2), sp.Rational(1, 2), sp.Integer(4), sp.Rational(1, 4)]
B.q("m-exp-16", "elementary-functions", 3,
    r"For $a>0$, $a\ne1$, the difference between the maximum and minimum of $f(x)=\log_a x$ on $[2,4]$ is $1$. The sum of all possible values of $a$ is",
    [r"$\dfrac52$", r"$2$", r"$\dfrac12$", r"$4$"],
    r"""$\log_a x$ is monotonic, so max − min $=|\log_a4-\log_a2|=|\log_a2|=1$.

$\log_a2=1\Rightarrow a=2$; $\log_a2=-1\Rightarrow a=\dfrac12$. Both are valid, sum $=\dfrac52$.""",
    N(sum(v for v in _avals16 if abs(abs(float(sp.log(4, v) - sp.log(2, v))) - 1) < 1e-12)))

B.q("m-exp-17", "elementary-functions", 2,
    r"$e^{\ln 3}+\lg 0.01=$",
    [r"$1$", r"$5$", r"$3$", r"$-1$"],
    r"$e^{\ln3}=3$ and $\lg0.01=\lg10^{-2}=-2$, so the sum is $1$.",
    N(3 + sp.log(sp.Rational(1, 100), 10)))

_v18 = {"a": sp.log(3, sp.Rational(1, 2)), "b": sp.Rational(1, 2) ** 3, "c": sp.sqrt(3)}
B.q("m-exp-18", "elementary-functions", 2,
    r"Let $a=\log_{0.5}3$, $b=0.5^{3}$, $c=3^{0.5}$. Then",
    [r"$a<b<c$", r"$b<a<c$", r"$c<b<a$", r"$a<c<b$"],
    r"""- $a=\log_{0.5}3<0$ (base below 1, argument above 1);
- $b=0.5^3=0.125\in(0,1)$;
- $c=\sqrt3>1$.

So $a<b<c$.""",
    T(order_text(_v18)))

B.q("m-exp-19", "elementary-functions", 1,
    r"The domain of $y=\log_2(x-3)$ is",
    [r"$(3,+\infty)$", r"$[3,+\infty)$", r"$(0,+\infty)$", r"$(-\infty,3)$"],
    r"The argument of a logarithm must be **positive**: $x-3>0$, so $x>3$.",
    S(sol(x - 3 > 0)))

B.q("m-exp-20", "elementary-functions", 2,
    r"If $\lg 2=a$ and $\lg 3=b$, then $\lg 12=$",
    [r"$2a+b$", r"$a+2b$", r"$2ab$", r"$a^2b$"],
    r"$\lg12=\lg(2^2\cdot3)=2\lg2+\lg3=2a+b$.",
    Expr(2 * a + b))
