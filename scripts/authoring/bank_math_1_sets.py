from itertools import product
from qb import *  # noqa: F403

B = Bank("math", "sets-inequalities")
R_ = sp.S.Reals


def sol(expr):
    """Solution set of a univariate inequality over the reals."""
    return sp.solveset(expr, x, R_)


# ---------------------------------------------------------------- sets
B.q("m-sets-01", "sets", 1,
    r"Let $A=\{1,2,3,4\}$ and $B=\{2,4,6\}$. Then $A\cap B=$",
    [r"$\{2,4\}$", r"$\{1,2,3,4,6\}$", r"$\{1,3\}$", r"$\{6\}$"],
    r"The intersection contains the elements that belong to **both** sets: $2$ and $4$. So $A\cap B=\{2,4\}$.",
    S(sp.Intersection(sp.FiniteSet(1, 2, 3, 4), sp.FiniteSet(2, 4, 6))))

B.q("m-sets-02", "sets", 1,
    r"Let $A=\{x\mid -1<x<3\}$ and $B=\{x\mid x\ge 1\}$. Then $A\cup B=$",
    [r"$(-1,+\infty)$", r"$[1,3)$", r"$(-1,1)$", r"$[1,+\infty)$"],
    r"""On a number line, $A$ covers $(-1,3)$ and $B$ covers $[1,+\infty)$. Together they cover everything to the right of $-1$:
$$A\cup B=(-1,+\infty).$$
(The overlap $[1,3)$ is $A\cap B$, not $A\cup B$.)""",
    S(sp.Union(sp.Interval.open(-1, 3), sp.Interval(1, sp.oo))))

B.q("m-sets-03", "sets", 1,
    r"The universal set is $U=\{1,2,3,4,5,6\}$ and $A=\{1,3,5\}$. Then $\complement_U A=$",
    [r"$\{2,4,6\}$", r"$\{1,3,5\}$", r"$\{1,2,3,4,5,6\}$", r"$\varnothing$"],
    r"The complement of $A$ in $U$ is the set of elements of $U$ that are **not** in $A$: $\complement_U A=\{2,4,6\}$.",
    S(sp.Complement(sp.FiniteSet(*range(1, 7)), sp.FiniteSet(1, 3, 5))))

B.q("m-sets-04", "sets", 1,
    r"How many subsets does the set $\{a,b,c\}$ have?",
    [r"$8$", r"$6$", r"$7$", r"$9$"],
    r"A set with $n$ elements has $2^n$ subsets (each element is either in or out). Here $n=3$, so there are $2^3=8$ subsets, including $\varnothing$ and the set itself.",
    N(2 ** 3))

B.q("m-sets-05", "sets", 2,
    r"Let $A=\{x\in\mathbb{N}\mid x<3\}$. The number of **proper** subsets of $A$ is",
    [r"$7$", r"$3$", r"$8$", r"$6$"],
    r"""$\mathbb{N}$ (the natural numbers) includes $0$, so $A=\{0,1,2\}$ has $3$ elements.

Number of subsets $=2^3=8$; proper subsets exclude $A$ itself: $8-1=7$.

Common trap: forgetting $0$ gives $A=\{1,2\}$ and the wrong answer $3$.""",
    N(2 ** len([v for v in range(0, 3)]) - 1))

_roots = sp.solve(x ** 2 - 3 * x + 2, x)
_avals = sp.FiniteSet(0, *[sp.Rational(2) / r for r in _roots])
B.q("m-sets-06", "sets", 3,
    r"Let $A=\{x\mid x^2-3x+2=0\}$ and $B=\{x\mid ax-2=0\}$. If $B\subseteq A$, the set of all possible values of $a$ is",
    [r"$\{0,1,2\}$", r"$\{1,2\}$", r"$\{2\}$", r"$\{0,2\}$"],
    r"""$A=\{1,2\}$. Consider the cases for $B$:

- $a=0$: the equation $0\cdot x=2$ has no solution, so $B=\varnothing\subseteq A$. ✔
- $a\neq0$: $B=\{\tfrac{2}{a}\}$. We need $\tfrac2a=1$ (so $a=2$) or $\tfrac2a=2$ (so $a=1$).

So $a\in\{0,1,2\}$. The most common mistake is forgetting the empty-set case $a=0$.""",
    S(_avals))

B.q("m-sets-07", "sets", 1,
    r"Which of the following statements is correct?",
    [r"$\varnothing\subseteq\{0\}$", r"$0\in\varnothing$", r"$\{0\}=\varnothing$", r"$\{0\}\in\{0,1\}$"],
    r"""- The empty set is a subset of **every** set, so $\varnothing\subseteq\{0\}$ is true.
- $\varnothing$ has no elements, so $0\in\varnothing$ is false.
- $\{0\}$ has one element, so it is not empty.
- $\{0\}$ is a *subset* of $\{0,1\}$, not an *element* of it: use $\subseteq$, not $\in$.""")

_A8 = sp.Interval.open(1, sp.oo)  # domain of lg(x-1)
_B8 = sp.Interval.open(0, sp.oo)  # range of 2^x
B.q("m-sets-08", "sets", 2,
    r"Let $A=\{x\mid y=\lg(x-1)\}$ and $B=\{y\mid y=2^x\}$. Then $(\complement_{\mathbb{R}}A)\cap B=$",
    [r"$(0,1]$", r"$(-\infty,1]$", r"$(0,1)$", r"$[0,1]$"],
    r"""Read each set carefully — the variable before the bar tells you what the set contains.

- $A$ is a set of $x$-values: the **domain** of $y=\lg(x-1)$, so $x-1>0$, $A=(1,+\infty)$.
- $B$ is a set of $y$-values: the **range** of $y=2^x$, so $B=(0,+\infty)$.

$\complement_{\mathbb{R}}A=(-\infty,1]$, and $(-\infty,1]\cap(0,+\infty)=(0,1]$.""",
    S(sp.Intersection(sp.Complement(R_, _A8), _B8)))

B.q("m-sets-09", "sets", 2,
    r"Let $M=\{x\mid |x-1|<2\}$ and $N=\{x\mid x^2<4\}$. Then $M\cap N=$",
    [r"$(-1,2)$", r"$(-2,3)$", r"$(-1,3)$", r"$(-2,2)$"],
    r"""$|x-1|<2\iff -2<x-1<2\iff -1<x<3$, so $M=(-1,3)$.

$x^2<4\iff -2<x<2$, so $N=(-2,2)$.

Overlap: $M\cap N=(-1,2)$.""",
    S(sp.Intersection(sol(sp.Abs(x - 1) < 2), sol(x ** 2 < 4))))


def _count_sets10():
    good = set()
    for cand in set(sp.solve(a ** 2 - 2, a) + sp.solve(a ** 2 - a, a) + sp.solve(a ** 2 - 1, a)):
        A_ = {sp.Integer(1), sp.Integer(2), cand}
        B_ = {sp.Integer(1), sp.simplify(cand ** 2)}
        if len(A_) == 3 and len(B_) == 2 and B_ <= A_:
            good.add(cand)
    return len(good)


B.q("m-sets-10", "sets", 3,
    r"Let $A=\{1,2,a\}$ and $B=\{1,a^2\}$. If $A\cup B=A$, how many real values can $a$ take?",
    [r"$3$", r"$2$", r"$4$", r"$5$"],
    r"""$A\cup B=A$ means $B\subseteq A$, so $a^2\in\{1,2,a\}$. Elements of a set must be **distinct**.

- $a^2=1$: then $B=\{1,1\}$ is not a valid set. ✘
- $a^2=2$: $a=\pm\sqrt2$, giving $A=\{1,2,\pm\sqrt2\}$, $B=\{1,2\}$. ✔ (two values)
- $a^2=a$: $a=0$ or $a=1$. $a=1$ makes $A=\{1,2,1\}$ invalid; $a=0$ gives $A=\{1,2,0\}$, $B=\{1,0\}$. ✔

So $a\in\{\sqrt2,-\sqrt2,0\}$: $3$ values.""",
    N(_count_sets10()))

B.q("m-sets-11", "sets", 1,
    r"Let $A=\{x\mid x>2\}$ and $B=\{x\mid x<5\}$. How many integers belong to $A\cap B$?",
    [r"$2$", r"$3$", r"$4$", r"$1$"],
    r"$A\cap B=\{x\mid 2<x<5\}$. Its integers are $3$ and $4$ (the endpoints $2$ and $5$ are excluded), so there are $2$.",
    N(len([v for v in range(-10, 20) if 2 < v < 5])))

B.q("m-sets-12", "sets", 2,
    r"In a class of $40$ students, $25$ like mathematics, $20$ like physics and $8$ like neither. How many like both?",
    [r"$13$", r"$5$", r"$12$", r"$17$"],
    r"""Students who like at least one subject: $40-8=32$.

By inclusion–exclusion, $|M\cup P|=|M|+|P|-|M\cap P|$, so
$$|M\cap P|=25+20-32=13.$$""",
    N(25 + 20 - (40 - 8)))

# ------------------------------------------------- properties of inequalities
B.q("m-ineq-01", "inequality-properties", 1,
    r"If $a>b>0$, which of the following must be true?",
    [r"$\dfrac1a<\dfrac1b$", r"$a^2<b^2$", r"$-a>-b$", r"$\dfrac ab<1$"],
    r"""For positive numbers, a larger number has a smaller reciprocal: $a>b>0\Rightarrow \dfrac1a<\dfrac1b$.

The others fail: squaring positive numbers keeps the order ($a^2>b^2$); multiplying by $-1$ reverses it ($-a<-b$); and $\dfrac ab>1$.""")

B.q("m-ineq-02", "inequality-properties", 2,
    r"If $a<b<0$, which of the following is true?",
    [r"$a^2>b^2$", r"$\dfrac1a<\dfrac1b$", r"$ab<b^2$", r"$|a|<|b|$"],
    r"""Both numbers are negative and $a$ is further from $0$, so $|a|>|b|$ and therefore $a^2>b^2$.

Check with $a=-2$, $b=-1$: $a^2=4>1=b^2$ ✔; $\tfrac1a=-\tfrac12>-1=\tfrac1b$, so $\tfrac1a<\tfrac1b$ is false; $ab=2>1=b^2$, so $ab<b^2$ is false; $|a|=2>|b|=1$.""")

_f3 = x + 4 / x
_c3 = [r for r in sp.solve(sp.diff(_f3, x), x) if r > 0][0]
B.q("m-ineq-03", "inequality-properties", 1,
    r"For $x>0$, the minimum value of $x+\dfrac4x$ is",
    [r"$4$", r"$2$", r"$5$", r"$8$"],
    r"""By AM–GM, for $x>0$: $x+\dfrac4x\ge 2\sqrt{x\cdot\dfrac4x}=2\cdot2=4$.

Equality holds when $x=\dfrac4x$, i.e. $x=2$, so the minimum $4$ is attained.""",
    N(_f3.subs(x, _c3)))

_f4 = x + 1 / (x - 1)
_c4 = [r for r in sp.solve(sp.diff(_f4, x), x) if r > 1][0]
B.q("m-ineq-04", "inequality-properties", 2,
    r"For $x>1$, the minimum value of $x+\dfrac{1}{x-1}$ is",
    [r"$3$", r"$2$", r"$1$", r"$4$"],
    r"""Rewrite so the product is constant: $x+\dfrac1{x-1}=(x-1)+\dfrac1{x-1}+1$.

Since $x-1>0$, AM–GM gives $(x-1)+\dfrac1{x-1}\ge2$, so the expression is $\ge 3$, with equality at $x-1=1$, i.e. $x=2$.

Trap: applying AM–GM directly to $x$ and $\dfrac1{x-1}$ — their product is not constant.""",
    N(_f4.subs(x, _c4)))

B.q("m-ineq-05", "inequality-properties", 1,
    r"If $a>0$, $b>0$ and $a+b=2$, the maximum value of $ab$ is",
    [r"$1$", r"$2$", r"$\dfrac12$", r"$4$"],
    r"By AM–GM, $ab\le\left(\dfrac{a+b}{2}\right)^2=1$, with equality when $a=b=1$. So the maximum is $1$.",
    N(sp.maximum(a * (2 - a), a, sp.Interval(0, 2))))

_f6 = 1 / a + 4 / (1 - a)
B.q("m-ineq-06", "inequality-properties", 3,
    r"If $a>0$, $b>0$ and $a+b=1$, the minimum value of $\dfrac1a+\dfrac4b$ is",
    [r"$9$", r"$4$", r"$5$", r"$8$"],
    r"""Multiply by $a+b=1$:
$$\left(\frac1a+\frac4b\right)(a+b)=1+4+\frac ba+\frac{4a}{b}\ge5+2\sqrt{\frac ba\cdot\frac{4a}b}=5+4=9.$$
Equality when $\dfrac ba=\dfrac{4a}b$, i.e. $b=2a$, so $a=\tfrac13$, $b=\tfrac23$. Minimum: $9$.""",
    N(_f6.subs(a, [r for r in sp.solve(sp.diff(_f6, a), a) if 0 < r < 1][0])))

B.q("m-ineq-07", "inequality-properties", 1,
    r"Let $M=x^2+3$ and $N=2x+1$ for real $x$. Then",
    [r"$M>N$", r"$M<N$", r"$M=N$", r"It depends on $x$"],
    r"Compare by subtracting: $M-N=x^2-2x+2=(x-1)^2+1\ge1>0$ for every real $x$. Hence $M>N$ always.")

B.q("m-ineq-08", "inequality-properties", 2,
    r"If $-1<a<2$ and $1<b<3$, the range of $a-b$ is",
    [r"$(-4,1)$", r"$(-2,-1)$", r"$(0,5)$", r"$(-4,-1)$"],
    r"""Never subtract inequalities directly. First negate: $1<b<3\Rightarrow -3<-b<-1$. Now **add**:
$$-1+(-3)<a+(-b)<2+(-1),\quad\text{so}\quad -4<a-b<1.$$""",
    S(sp.Interval.open(-1 - 3, 2 - 1)))

_g9 = x * (1 - 2 * x)
B.q("m-ineq-09", "inequality-properties", 3,
    r"If $x>0$, $y>0$ and $2x+y=1$, the maximum value of $xy$ is",
    [r"$\dfrac18$", r"$\dfrac14$", r"$\dfrac12$", r"$\dfrac1{16}$"],
    r"""Write $xy=\dfrac12(2x)\cdot y\le\dfrac12\left(\dfrac{2x+y}{2}\right)^2=\dfrac12\cdot\dfrac14=\dfrac18$.

Equality when $2x=y=\tfrac12$, i.e. $x=\tfrac14$, $y=\tfrac12$.""",
    N(sp.maximum(_g9, x, sp.Interval(0, sp.Rational(1, 2)))))

B.q("m-ineq-10", "inequality-properties", 1,
    r"If $a>b$ and $c$ is any real number, which of the following must hold?",
    [r"$a+c>b+c$", r"$ac>bc$", r"$a^2>b^2$", r"$|a|>|b|$"],
    r"""Adding the same number to both sides keeps an inequality true, so $a+c>b+c$.

The others can fail: if $c\le0$ then $ac>bc$ is false; with $a=1,b=-2$ we get $a^2<b^2$ and $|a|<|b|$.""")

# -------------------------------------------------- quadratic inequalities
B.q("m-quad-01", "quadratic-inequalities", 1,
    r"The solution set of $x^2-5x+6<0$ is",
    [r"$(2,3)$", r"$(-\infty,2)\cup(3,+\infty)$", r"$(-3,-2)$", r"$[2,3]$"],
    r"""Factor: $x^2-5x+6=(x-2)(x-3)$. The parabola opens upward, so it is negative **between** its roots:
$$2<x<3.$$""",
    S(sol(x ** 2 - 5 * x + 6 < 0)))

B.q("m-quad-02", "quadratic-inequalities", 1,
    r"The solution set of $x^2-x-6\ge0$ is",
    [r"$(-\infty,-2]\cup[3,+\infty)$", r"$[-2,3]$", r"$(-\infty,-3]\cup[2,+\infty)$", r"$(-\infty,-2)\cup(3,+\infty)$"],
    r"""$x^2-x-6=(x+2)(x-3)$, roots $-2$ and $3$. Upward parabola: non-negative **outside** the roots, and the roots are included because of "$\ge$":
$$x\le-2\ \text{or}\ x\ge3.$$""",
    S(sol(x ** 2 - x - 6 >= 0)))

B.q("m-quad-03", "quadratic-inequalities", 2,
    r"The solution set of $-x^2+2x+3>0$ is",
    [r"$(-1,3)$", r"$(-\infty,-1)\cup(3,+\infty)$", r"$(-3,1)$", r"$(1,3)$"],
    r"""Multiply by $-1$ and **reverse** the sign: $x^2-2x-3<0$, i.e. $(x+1)(x-3)<0$. So $-1<x<3$.""",
    S(sol(-x ** 2 + 2 * x + 3 > 0)))

B.q("m-quad-04", "quadratic-inequalities", 2,
    r"The solution set of $x^2+2x+3<0$ is",
    [r"$\varnothing$", r"$\mathbb{R}$", r"$(-3,1)$", r"$(-1,3)$"],
    r"""Discriminant: $\Delta=4-12=-8<0$, so the upward parabola never touches the $x$-axis and $x^2+2x+3>0$ for **every** $x$ (indeed $x^2+2x+3=(x+1)^2+2$).

Hence $x^2+2x+3<0$ has no solution: the solution set is $\varnothing$.""",
    S(sol(x ** 2 + 2 * x + 3 < 0)))

B.q("m-quad-05", "quadratic-inequalities", 2,
    r"The solution set of $x^2-4x+4\le0$ is",
    [r"$\{2\}$", r"$\varnothing$", r"$\mathbb{R}$", r"$(-\infty,2]$"],
    r"$x^2-4x+4=(x-2)^2\ge0$ for all $x$, and it equals $0$ only at $x=2$. So $(x-2)^2\le0$ only when $x=2$: the solution set is $\{2\}$.",
    S(sol(x ** 2 - 4 * x + 4 <= 0)))

_s6 = sp.solve([a * sp.Rational(-1, 2) ** 2 + b * sp.Rational(-1, 2) + 2, a * sp.Rational(1, 3) ** 2 + b * sp.Rational(1, 3) + 2], [a, b])
B.q("m-quad-06", "quadratic-inequalities", 2,
    r"The solution set of $ax^2+bx+2>0$ is $\left(-\dfrac12,\dfrac13\right)$. Then $a+b=$",
    [r"$-14$", r"$14$", r"$-10$", r"$10$"],
    r"""The endpoints $-\tfrac12$ and $\tfrac13$ are the roots of $ax^2+bx+2=0$, and $a<0$ (the quadratic is positive only between its roots).

By Vieta: $-\dfrac12\cdot\dfrac13=\dfrac2a\Rightarrow a=-12$, and $-\dfrac12+\dfrac13=-\dfrac ba\Rightarrow -\dfrac16=\dfrac{b}{12}\Rightarrow b=-2$.

So $a+b=-14$.""",
    N(_s6[a] + _s6[b]))

B.q("m-quad-07", "quadratic-inequalities", 3,
    r"The inequality $x^2+mx+1>0$ holds for **all** real $x$. The range of $m$ is",
    [r"$(-2,2)$", r"$[-2,2]$", r"$(-\infty,-2)\cup(2,+\infty)$", r"$(0,2)$"],
    r"""An upward parabola is always positive exactly when it has no real roots: $\Delta=m^2-4<0$, so $-2<m<2$.

($m=\pm2$ gives $\Delta=0$: the quadratic touches $0$, so "$>0$ for all $x$" fails.)""",
    S(sp.solveset(m ** 2 - 4 < 0, m, R_)))

_k8 = sp.Union(sp.FiniteSet(0), sp.Intersection(sp.solveset(k ** 2 - 4 * k < 0, k, R_), sp.Interval.open(0, sp.oo)))
B.q("m-quad-08", "quadratic-inequalities", 3,
    r"The inequality $kx^2-kx+1>0$ holds for all real $x$. The range of $k$ is",
    [r"$[0,4)$", r"$(0,4)$", r"$[0,4]$", r"$(-\infty,0)\cup(4,+\infty)$"],
    r"""**Case $k=0$:** the inequality becomes $1>0$, which is always true. ✔

**Case $k\ne0$:** we need an upward parabola with no real roots: $k>0$ and $\Delta=k^2-4k<0$, i.e. $0<k<4$.

Combining: $0\le k<4$. Forgetting the case $k=0$ is the classic mistake.""",
    S(_k8))

B.q("m-quad-09", "quadratic-inequalities", 2,
    r"How many integers satisfy $x^2-3x-10\le0$?",
    [r"$8$", r"$7$", r"$6$", r"$9$"],
    r"$x^2-3x-10=(x+2)(x-5)\le0\iff -2\le x\le5$. The integers are $-2,-1,0,1,2,3,4,5$: there are $8$.",
    N(len([v for v in range(-50, 50) if v ** 2 - 3 * v - 10 <= 0])))

B.q("m-quad-10", "quadratic-inequalities", 1,
    r"The solution set of $(x-1)(x+2)<0$ is",
    [r"$(-2,1)$", r"$(-1,2)$", r"$(-\infty,-2)\cup(1,+\infty)$", r"$(1,2)$"],
    r"The roots are $1$ and $-2$. The product of two factors is negative when they have opposite signs, i.e. between the roots: $-2<x<1$.",
    S(sol((x - 1) * (x + 2) < 0)))

B.q("m-quad-11", "quadratic-inequalities", 3,
    r"Given $a>1$, the solution set of $x^2-(a+1)x+a<0$ is",
    [r"$(1,a)$", r"$(a,1)$", r"$(-\infty,1)\cup(a,+\infty)$", r"$\varnothing$"],
    r"""Factor: $x^2-(a+1)x+a=(x-1)(x-a)$. Since $a>1$, the smaller root is $1$ and the larger is $a$.

The upward parabola is negative between the roots: $1<x<a$. (If $a<1$ the answer would be $(a,1)$ and if $a=1$ it would be $\varnothing$ — always compare the roots first.)""")

_pq = sp.solve([1 + a + b, 16 + 4 * a + b], [a, b])
B.q("m-quad-12", "quadratic-inequalities", 2,
    r"The solution set of $x^2+px+q<0$ is $(1,4)$. Then $p+q=$",
    [r"$-1$", r"$9$", r"$1$", r"$-9$"],
    r"$1$ and $4$ are the roots of $x^2+px+q=0$, so $x^2+px+q=(x-1)(x-4)=x^2-5x+4$. Thus $p=-5$, $q=4$ and $p+q=-1$.",
    N(_pq[a] + _pq[b]))

# --------------------------------------------------- rational inequalities
B.q("m-rat-01", "rational-inequalities", 1,
    r"The solution set of $\dfrac{x-1}{x+2}<0$ is",
    [r"$(-2,1)$", r"$(-\infty,-2)\cup(1,+\infty)$", r"$[-2,1)$", r"$(-1,2)$"],
    r"A quotient is negative when numerator and denominator have opposite signs. Equivalent to $(x-1)(x+2)<0$, so $-2<x<1$.",
    S(sol((x - 1) / (x + 2) < 0)))

B.q("m-rat-02", "rational-inequalities", 1,
    r"The solution set of $\dfrac{x+3}{x-2}\ge0$ is",
    [r"$(-\infty,-3]\cup(2,+\infty)$", r"$(-\infty,-3]\cup[2,+\infty)$", r"$[-3,2)$", r"$[-3,2]$"],
    r"""Equivalent to $(x+3)(x-2)\ge0$ **with** $x\ne2$. The product is $\ge0$ for $x\le-3$ or $x\ge2$; remove $x=2$ (division by zero):
$$(-\infty,-3]\cup(2,+\infty).$$""",
    S(sol((x + 3) / (x - 2) >= 0)))

B.q("m-rat-03", "rational-inequalities", 2,
    r"The solution set of $\dfrac1x<1$ is",
    [r"$(-\infty,0)\cup(1,+\infty)$", r"$(1,+\infty)$", r"$(0,1)$", r"$(-\infty,1)$"],
    r"""Do **not** multiply by $x$ — its sign is unknown. Move everything to one side:
$$\frac1x-1<0\iff\frac{1-x}{x}<0\iff\frac{x-1}{x}>0.$$
Critical points $0$ and $1$: the quotient is positive for $x<0$ or $x>1$.""",
    S(sol(1 / x < 1)))

B.q("m-rat-04", "rational-inequalities", 2,
    r"The solution set of $\dfrac{2x-1}{x+1}\le1$ is",
    [r"$(-1,2]$", r"$[-1,2]$", r"$(-\infty,2]$", r"$(-\infty,-1)\cup[2,+\infty)$"],
    r"""$$\frac{2x-1}{x+1}-1\le0\iff\frac{2x-1-(x+1)}{x+1}\le0\iff\frac{x-2}{x+1}\le0.$$
This holds between the critical points, including $x=2$ (numerator zero) but excluding $x=-1$ (denominator zero): $(-1,2]$.""",
    S(sol((2 * x - 1) / (x + 1) <= 1)))

B.q("m-rat-05", "rational-inequalities", 3,
    r"The solution set of $\dfrac{3}{x-1}\ge1$ is",
    [r"$(1,4]$", r"$[1,4]$", r"$(-\infty,4]$", r"$(1,4)$"],
    r"""$$\frac3{x-1}-1\ge0\iff\frac{4-x}{x-1}\ge0\iff\frac{x-4}{x-1}\le0.$$
So $1<x\le4$ (the denominator cannot be zero, so $x\neq1$).""",
    S(sol(3 / (x - 1) >= 1)))

B.q("m-rat-06", "rational-inequalities", 3,
    r"The solution set of $\dfrac{(x-1)(x+2)}{x-3}\ge0$ is",
    [r"$[-2,1]\cup(3,+\infty)$", r"$[-2,1]\cup[3,+\infty)$", r"$(-\infty,-2]\cup[1,3)$", r"$(-2,1)\cup(3,+\infty)$"],
    r"""Critical points: $-2,1$ (numerator) and $3$ (denominator). Sign chart, from the right (all factors positive for large $x$): $+$ on $(3,\infty)$, $-$ on $(1,3)$, $+$ on $(-2,1)$, $-$ on $(-\infty,-2)$.

Include the zeros of the numerator, exclude $x=3$:
$$[-2,1]\cup(3,+\infty).$$""",
    S(sol((x - 1) * (x + 2) / (x - 3) >= 0)))

B.q("m-rat-07", "rational-inequalities", 2,
    r"The solution set of $\dfrac{x^2-4}{x+1}<0$ is",
    [r"$(-\infty,-2)\cup(-1,2)$", r"$(-2,-1)\cup(2,+\infty)$", r"$(-2,2)$", r"$(-\infty,-2)\cup(2,+\infty)$"],
    r"""$\dfrac{(x-2)(x+2)}{x+1}<0$. Critical points $-2,-1,2$. From the right: $+$ on $(2,\infty)$, $-$ on $(-1,2)$, $+$ on $(-2,-1)$, $-$ on $(-\infty,-2)$.

Negative parts: $(-\infty,-2)\cup(-1,2)$.""",
    S(sol((x ** 2 - 4) / (x + 1) < 0)))

B.q("m-rat-08", "rational-inequalities", 2,
    r"The solution set of $\dfrac{x}{x-3}>0$ is",
    [r"$(-\infty,0)\cup(3,+\infty)$", r"$(0,3)$", r"$(-\infty,0]\cup(3,+\infty)$", r"$(3,+\infty)$"],
    r"The quotient is positive when $x$ and $x-3$ have the same sign: both positive ($x>3$) or both negative ($x<0$).",
    S(sol(x / (x - 3) > 0)))

B.q("m-rat-09", "rational-inequalities", 3,
    r"The solution set of $\dfrac{x+1}{x^2+1}>0$ is",
    [r"$(-1,+\infty)$", r"$(-\infty,-1)$", r"$(-1,1)$", r"$(-\infty,-1)\cup(1,+\infty)$"],
    r"The denominator $x^2+1\ge1>0$ for every $x$, so the sign of the fraction is the sign of $x+1$. Thus $x+1>0$, i.e. $x>-1$. (Treating $x^2+1$ as if it could be zero or negative is a common slip.)",
    S(sol((x + 1) / (x ** 2 + 1) > 0)))

B.q("m-rat-10", "rational-inequalities", 2,
    r"How many integers satisfy $\dfrac{x+2}{x-3}\le0$?",
    [r"$5$", r"$6$", r"$4$", r"$7$"],
    r"$\dfrac{x+2}{x-3}\le0\iff -2\le x<3$ (include the numerator's zero, exclude $x=3$). Integers: $-2,-1,0,1,2$ — five of them.",
    N(len([v for v in range(-50, 50) if v != 3 and sp.Rational(v + 2, v - 3) <= 0])))
