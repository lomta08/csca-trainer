"""Writes math lesson notes (part 1) to src/content/notes/math/*.md. Original explanations."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "src" / "content" / "notes" / "math"
OUT.mkdir(parents=True, exist_ok=True)

NOTES = {}

NOTES["sets"] = r"""
## Key ideas

A **set** is a well-defined collection of distinct objects, called its **elements**. We write $a\in A$ ("$a$ belongs to $A$") or $a\notin A$.

- Elements are **distinct** (no repeats) and their order does not matter: $\{1,2\}=\{2,1\}$.
- **Representations:** listing $\{1,3,5\}$; description (set-builder) $\{x\mid x^2<4\}$; intervals $(-2,2)$; Venn diagrams.
- Read the letter before the bar: $\{x\mid y=\sqrt{x}\}$ is a set of $x$-values (a domain), while $\{y\mid y=\sqrt x\}$ is a set of $y$-values (a range).
- Standard sets: $\mathbb N$ (natural numbers, **including $0$**), $\mathbb N^*$ or $\mathbb N_+$ (positive integers), $\mathbb Z$, $\mathbb Q$, $\mathbb R$, and the empty set $\varnothing$.

## Relations and operations

| Name | Notation | Meaning |
|---|---|---|
| Subset | $A\subseteq B$ | every element of $A$ is in $B$ |
| Proper subset | $A\subsetneqq B$ | $A\subseteq B$ and $A\ne B$ |
| Intersection | $A\cap B$ | in $A$ **and** in $B$ |
| Union | $A\cup B$ | in $A$ **or** in $B$ (or both) |
| Complement | $\complement_U A$ | in the universal set $U$ but not in $A$ |

Useful facts:

- $\varnothing\subseteq A$ for every set $A$.
- A set with $n$ elements has $2^n$ subsets and $2^n-1$ proper subsets.
- $A\cap B=A\iff A\subseteq B$, and $A\cup B=B\iff A\subseteq B$.
- Counting: $|A\cup B|=|A|+|B|-|A\cap B|$.

## Worked examples

**Example 1.** $A=\{x\mid -1\le x<3\}$, $B=\{x\mid x>1\}$. Find $A\cap B$, $A\cup B$ and $A\cap\complement_{\mathbb R}B$.

*Solution.* Draw both on a number line. $A\cap B=(1,3)$; $A\cup B=[-1,+\infty)$. Since $\complement_{\mathbb R}B=(-\infty,1]$, we get $A\cap\complement_{\mathbb R}B=[-1,1]$. Note how the endpoint $1$ switches from open to closed in the complement.

**Example 2.** $A=\{1,2\}$ and $B=\{x\mid ax=1\}$ with $B\subseteq A$. Find all $a$.

*Solution.* If $a=0$, $B=\varnothing\subseteq A$ ✔. Otherwise $B=\{\tfrac1a\}$, so $\tfrac1a=1$ or $\tfrac1a=2$, giving $a=1$ or $a=\tfrac12$. Answer: $a\in\{0,1,\tfrac12\}$.

**Example 3.** How many subsets $M$ satisfy $\{1\}\subseteq M\subseteq\{1,2,3,4\}$?

*Solution.* $M$ must contain $1$; each of $2,3,4$ may be in or out: $2^3=8$ sets.

## Common traps

- Forgetting the **empty-set case** when a set depends on a parameter ($B\subseteq A$ allows $B=\varnothing$).
- Forgetting that elements must be **distinct** — check answers like $a=1$ in $\{1,a\}$.
- Treating $0\in\mathbb N$ as false: in CSCA/Chinese textbooks $\mathbb N$ contains $0$.
- Confusing $\in$ (element) with $\subseteq$ (subset): $\{0\}\subseteq\{0,1\}$ but $\{0\}\notin\{0,1\}$.
"""

NOTES["inequality-properties"] = r"""
## Key ideas

Inequalities behave like equations **except** when you multiply or divide by a negative number.

| Rule | Statement |
|---|---|
| Transitivity | $a>b,\ b>c\Rightarrow a>c$ |
| Add anything | $a>b\Rightarrow a+c>b+c$ |
| Multiply by positive | $a>b,\ c>0\Rightarrow ac>bc$ |
| Multiply by negative | $a>b,\ c<0\Rightarrow ac<bc$ (**flip**) |
| Add inequalities | $a>b,\ c>d\Rightarrow a+c>b+d$ |
| Multiply (positives) | $a>b>0,\ c>d>0\Rightarrow ac>bd$ |
| Powers | $a>b>0\Rightarrow a^n>b^n$ |
| Reciprocals | $a>b>0\Rightarrow\dfrac1a<\dfrac1b$ |

**Comparing two expressions:** subtract and decide the sign of $A-B$ (complete the square if needed), or for positive quantities compare $\dfrac AB$ with $1$.

## AM–GM inequality

For $a,b>0$: $$\frac{a+b}{2}\ge\sqrt{ab},$$ with equality **only** when $a=b$.

- If the **sum** $a+b=S$ is fixed, the product $ab$ is largest ($\le S^2/4$) when $a=b$.
- If the **product** $ab=P$ is fixed, the sum $a+b$ is smallest ($\ge2\sqrt P$) when $a=b$.

Checklist before using AM–GM: **positive**, **constant** sum or product, **equality** actually reachable ("一正二定三相等").

## Worked examples

**Example 1.** If $-2<a<1$ and $3<b<5$, find the range of $2a-b$.

*Solution.* $-4<2a<2$ and $-5<-b<-3$. Adding: $-9<2a-b<-1$.

**Example 2.** For $x>0$, find the minimum of $f(x)=2x+\dfrac8x$.

*Solution.* $2x+\dfrac8x\ge2\sqrt{2x\cdot\frac8x}=2\cdot4=8$, equality when $2x=\frac8x$, i.e. $x=2$. Minimum $8$.

**Example 3.** For $x>2$, find the minimum of $x+\dfrac{4}{x-2}$.

*Solution.* Write it as $(x-2)+\dfrac4{x-2}+2\ge2\sqrt4+2=6$, with equality at $x-2=2$, $x=4$.

## Common traps

- Subtracting inequalities directly: from $a>b$ and $c>d$ you **cannot** conclude $a-c>b-d$.
- Multiplying by an expression of unknown sign (like $x$ or $a-1$) without considering cases.
- Using AM–GM when the equality condition is impossible (e.g. $\sqrt{x^2+2}+\dfrac1{\sqrt{x^2+2}}$ never reaches $2$).
"""

NOTES["quadratic-inequalities"] = r"""
## Key ideas

To solve $ax^2+bx+c>0$ (or $<,\ \ge,\ \le$) think of the **graph** of $y=ax^2+bx+c$.

1. Make the leading coefficient positive (multiply by $-1$ and **flip** the sign if needed).
2. Find the roots (factorise or use the formula). Compute $\Delta=b^2-4ac$.
3. Read the answer from the upward parabola.

| | $\Delta>0$, roots $x_1<x_2$ | $\Delta=0$, root $x_0$ | $\Delta<0$ |
|---|---|---|---|
| $ax^2+bx+c>0$ ($a>0$) | $x<x_1$ or $x>x_2$ | $x\ne x_0$ | all $\mathbb R$ |
| $ax^2+bx+c<0$ ($a>0$) | $x_1<x<x_2$ | $\varnothing$ | $\varnothing$ |

"Outside the roots for $>$, between the roots for $<$" — when $a>0$.

## Roots and coefficients (Vieta)

If the roots are $x_1,x_2$: $x_1+x_2=-\dfrac ba$, $x_1x_2=\dfrac ca$. If the solution set of $ax^2+bx+c<0$ is $(m,n)$, then $m,n$ are the roots and $a>0$.

**Always true for all $x$:** $ax^2+bx+c>0$ for every real $x$ $\iff$ ($a>0$ and $\Delta<0$), **or** $a=b=0,\ c>0$.

## Worked examples

**Example 1.** Solve $-2x^2+x+3\ge0$.

*Solution.* Multiply by $-1$: $2x^2-x-3\le0$, i.e. $(2x-3)(x+1)\le0$. Roots $-1$ and $\tfrac32$. Answer $\left[-1,\tfrac32\right]$.

**Example 2.** The solution set of $x^2+bx+c<0$ is $(-1,3)$. Solve $cx^2+bx+1>0$.

*Solution.* $-1,3$ are roots: $b=-(-1+3)=-2$, $c=-3$. Solve $-3x^2-2x+1>0\iff3x^2+2x-1<0\iff(3x-1)(x+1)<0$, so $-1<x<\tfrac13$.

**Example 3.** Find $m$ such that $mx^2-mx-1<0$ for all real $x$.

*Solution.* $m=0$: $-1<0$ ✔. $m\ne0$: need $m<0$ and $\Delta=m^2+4m<0$, i.e. $-4<m<0$. Answer $-4<m\le0$.

## Common traps

- Forgetting to flip the sign when making $a$ positive.
- Forgetting the case where the leading coefficient is a parameter equal to $0$.
- Writing $(x_1,x_2)$ before checking which root is smaller (compare $a$ and $1$ in $(x-1)(x-a)<0$).
"""

NOTES["rational-inequalities"] = r"""
## Key ideas

A rational (fractional) inequality has the unknown in a denominator, e.g. $\dfrac{x-1}{x+2}\ge0$.

**Method:**

1. Move everything to one side so the other side is $0$; combine into a single fraction $\dfrac{P(x)}{Q(x)}$.
2. A quotient has the same sign as the product: $\dfrac PQ>0\iff PQ>0$, and $\dfrac PQ\ge0\iff PQ\ge0$ **and** $Q\ne0$.
3. Mark the zeros of $P$ and $Q$ on a number line (the **critical points**) and use a sign chart.
4. Include zeros of the numerator for $\ge,\le$; **never** include zeros of the denominator.

**Sign chart (wiggle) rule:** with all factors written as $(x-r)$, the expression is positive to the right of the largest critical point and changes sign at each simple root.

## Worked examples

**Example 1.** Solve $\dfrac{2x+1}{x-3}\le1$.

*Solution.* $\dfrac{2x+1}{x-3}-1\le0\iff\dfrac{x+4}{x-3}\le0$. Critical points $-4$ (include) and $3$ (exclude): $[-4,3)$.

**Example 2.** Solve $\dfrac{(x+1)(x-2)}{x}<0$.

*Solution.* Critical points $-1,0,2$. From the right: $+$ on $(2,\infty)$, $-$ on $(0,2)$, $+$ on $(-1,0)$, $-$ on $(-\infty,-1)$. Answer $(-\infty,-1)\cup(0,2)$.

**Example 3.** Solve $\dfrac{1}{x-1}>1$.

*Solution.* $\dfrac{1-(x-1)}{x-1}>0\iff\dfrac{2-x}{x-1}>0\iff\dfrac{x-2}{x-1}<0$, so $1<x<2$.

## Common traps

- **Cross-multiplying** by a denominator whose sign is unknown. Instead, move everything to one side.
- Including a zero of the denominator because the inequality is "$\ge$".
- Forgetting that a factor which is always positive (like $x^2+1$) can be ignored — it does not change the sign.
"""

NOTES["function-properties"] = r"""
## Key ideas

A **function** $f:A\to B$ assigns to every $x$ in the domain $A$ exactly one value $f(x)$.

**Domain** — find all $x$ for which the formula makes sense:

| Expression | Condition |
|---|---|
| $\dfrac1{g(x)}$ | $g(x)\ne0$ |
| $\sqrt{g(x)}$ (even root) | $g(x)\ge0$ |
| $\dfrac1{\sqrt{g(x)}}$ | $g(x)>0$ |
| $\log_a g(x)$ | $g(x)>0$ |
| $\tan x$ | $x\ne\dfrac\pi2+k\pi$ |
| $x^0$ | $x\ne0$ |

**Range** — use completing the square, monotonicity, AM–GM, or substitution. On a closed interval compare the vertex/critical values **and** the endpoints.

**Monotonicity** — $f$ is increasing on $I$ if $x_1<x_2\Rightarrow f(x_1)<f(x_2)$. For composite functions: same direction → increasing, opposite → decreasing ("同增异减").

**Parity** (needs a domain symmetric about $0$):

- even: $f(-x)=f(x)$, graph symmetric about the $y$-axis;
- odd: $f(-x)=-f(x)$, graph symmetric about the origin; if $0$ is in the domain, $f(0)=0$.

**Periodicity** — $T>0$ is a period if $f(x+T)=f(x)$ for all $x$. If $f(x+a)=-f(x)$ then $2a$ is a period.

## Worked examples

**Example 1.** Find the domain of $f(x)=\sqrt{2-x}+\lg(x+1)$.

*Solution.* $2-x\ge0$ and $x+1>0$, so $-1<x\le2$: domain $(-1,2]$.

**Example 2.** $f$ is odd on $\mathbb R$ and $f(x)=x^2-2x$ for $x>0$. Find $f(x)$ for $x<0$.

*Solution.* For $x<0$, $-x>0$: $f(-x)=x^2+2x$. Oddness gives $f(x)=-f(-x)=-x^2-2x$.

**Example 3.** Find the range of $y=x^2-2x$ on $[-1,2]$.

*Solution.* $y=(x-1)^2-1$; vertex $x=1$ is inside, minimum $-1$. Endpoints: $y(-1)=3$, $y(2)=0$. Range $[-1,3]$.

## Common traps

- Simplifying the formula before finding the domain (e.g. $\dfrac{x^2-1}{x-1}$ still excludes $x=1$).
- Writing an increasing interval as a union "$(-\infty,-1)\cup(1,\infty)$" — say "on $(-\infty,-1)$ and on $(1,\infty)$".
- Checking parity without first checking that the domain is symmetric.
- Using a formula valid only for $x>0$ at a negative $x$.
"""

NOTES["elementary-functions"] = r"""
## Laws of exponents and logarithms

For $a,b>0$ and real $m,n$:
$$a^m a^n=a^{m+n},\quad \frac{a^m}{a^n}=a^{m-n},\quad (a^m)^n=a^{mn},\quad a^{-n}=\frac1{a^n},\quad a^{\frac mn}=\sqrt[n]{a^m}.$$

$\log_a N=b\iff a^b=N$ (with $a>0$, $a\ne1$, $N>0$). Hence $\log_a1=0$, $\log_aa=1$, $a^{\log_aN}=N$.

$$\log_a(MN)=\log_aM+\log_aN,\quad \log_a\frac MN=\log_aM-\log_aN,\quad \log_aM^n=n\log_aM$$
$$\text{change of base: }\log_ab=\frac{\log_cb}{\log_ca},\qquad \log_ab\cdot\log_ba=1,\qquad \log_{a^m}b^n=\frac nm\log_ab.$$

$\lg x=\log_{10}x$ and $\ln x=\log_ex$ ($e\approx2.718$).

## Graphs and properties

| Function | Domain | Range | Monotonic | Fixed point |
|---|---|---|---|---|
| $y=a^x$ | $\mathbb R$ | $(0,+\infty)$ | increasing if $a>1$, decreasing if $0<a<1$ | $(0,1)$ |
| $y=\log_ax$ | $(0,+\infty)$ | $\mathbb R$ | increasing if $a>1$, decreasing if $0<a<1$ | $(1,0)$ |
| $y=x^\alpha$ | depends on $\alpha$ | | increasing on $(0,\infty)$ if $\alpha>0$ | $(1,1)$ |

$y=a^x$ and $y=\log_ax$ are inverse functions: their graphs are symmetric about $y=x$.

**Comparing values:** compare each number with benchmarks $0$ and $1$ ($a^0=1$, $\log_a1=0$, $\log_aa=1$), or use monotonicity with a common base.

## Worked examples

**Example 1.** Evaluate $\log_2 24-\log_2 3+8^{\frac23}$.

*Solution.* $\log_2\dfrac{24}{3}=\log_28=3$ and $8^{\frac23}=(2^3)^{\frac23}=4$. Total $7$.

**Example 2.** Compare $a=0.3^{0.2}$, $b=\log_{0.3}2$, $c=2^{0.3}$.

*Solution.* $0<a<1$ (base below 1, positive exponent), $b<0$ (base below 1, argument above 1), $c>1$. So $b<a<c$.

**Example 3.** Solve $\log_3(x+1)+\log_3(x-1)=1$.

*Solution.* Domain $x>1$. $\log_3(x^2-1)=1\Rightarrow x^2-1=3\Rightarrow x=\pm2$; only $x=2$ is in the domain.

## Common traps

- $\log_a(M+N)\ne\log_aM+\log_aN$.
- Forgetting the domain $x>0$ inside a logarithm, especially after combining logs.
- Rejecting nothing after a substitution $t=a^x$: remember $t>0$.
- A negative exponent means a reciprocal, not a negative number.
"""

NOTES["trigonometry"] = r"""
## Angles and definitions

Radians: $180^\circ=\pi$ rad, so $1^\circ=\dfrac{\pi}{180}$ rad. Arc length $l=r\alpha$, sector area $S=\tfrac12lr=\tfrac12r^2\alpha$.

For a point $(x,y)$ at distance $r$ on the terminal side: $\sin\alpha=\dfrac yr$, $\cos\alpha=\dfrac xr$, $\tan\alpha=\dfrac yx$.

Signs by quadrant (**ASTC**): I all positive; II $\sin$; III $\tan$; IV $\cos$.

| $\alpha$ | $0$ | $\frac\pi6$ | $\frac\pi4$ | $\frac\pi3$ | $\frac\pi2$ |
|---|---|---|---|---|---|
| $\sin$ | $0$ | $\frac12$ | $\frac{\sqrt2}2$ | $\frac{\sqrt3}2$ | $1$ |
| $\cos$ | $1$ | $\frac{\sqrt3}2$ | $\frac{\sqrt2}2$ | $\frac12$ | $0$ |
| $\tan$ | $0$ | $\frac{\sqrt3}3$ | $1$ | $\sqrt3$ | — |

## Identities

$$\sin^2\alpha+\cos^2\alpha=1,\qquad \tan\alpha=\frac{\sin\alpha}{\cos\alpha}$$

**Reduction formulas:** for $k\pi\pm\alpha$ the function name stays the same; for $\frac\pi2\pm\alpha$ sine ↔ cosine. The sign is that of the original function in the quadrant (treating $\alpha$ as acute). E.g. $\sin(\pi-\alpha)=\sin\alpha$, $\cos(\pi+\alpha)=-\cos\alpha$, $\sin(\tfrac\pi2+\alpha)=\cos\alpha$.

**Sum and double angle:**
$$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta,\qquad \cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$$
$$\tan(\alpha\pm\beta)=\frac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta},\qquad \sin2\alpha=2\sin\alpha\cos\alpha$$
$$\cos2\alpha=\cos^2\alpha-\sin^2\alpha=2\cos^2\alpha-1=1-2\sin^2\alpha$$

**Auxiliary angle:** $a\sin x+b\cos x=\sqrt{a^2+b^2}\,\sin(x+\varphi)$, so its maximum is $\sqrt{a^2+b^2}$.

## Graphs

For $y=A\sin(\omega x+\varphi)+B$: amplitude $|A|$, period $T=\dfrac{2\pi}{|\omega|}$, range $[B-|A|,B+|A|]$. $y=\tan x$ has period $\pi$.

Shifting: $y=\sin\omega x\to y=\sin(\omega x+\varphi)=\sin\omega\left(x+\frac\varphi\omega\right)$ moves the graph **left** by $\dfrac\varphi\omega$ (if $\varphi>0$).

## Solving triangles

Law of sines $\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin C}=2R$; law of cosines $c^2=a^2+b^2-2ab\cos C$; area $S=\tfrac12ab\sin C$.

## Worked examples

**Example 1.** $\cos\alpha=-\dfrac{5}{13}$, $\alpha\in\left(\dfrac\pi2,\pi\right)$. Find $\sin2\alpha$.

*Solution.* $\sin\alpha=+\dfrac{12}{13}$ (quadrant II). $\sin2\alpha=2\cdot\dfrac{12}{13}\cdot\left(-\dfrac5{13}\right)=-\dfrac{120}{169}$.

**Example 2.** Find the period and maximum of $y=\sqrt3\sin2x+\cos2x$.

*Solution.* $y=2\sin\left(2x+\frac\pi6\right)$: period $\pi$, maximum $2$.

**Example 3.** In $\triangle ABC$, $b=2$, $c=3$, $A=60^\circ$. Find $a$.

*Solution.* $a^2=4+9-2\cdot2\cdot3\cdot\tfrac12=7$, so $a=\sqrt7$.

## Common traps

- Choosing the wrong sign after $\sin^2+\cos^2=1$ — always use the quadrant.
- Forgetting to divide the phase by $\omega$ when shifting graphs.
- Missing the second solution with the law of sines ($\sin B=\tfrac{\sqrt3}2$ gives $60^\circ$ or $120^\circ$).
- Mixing degrees and radians on a calculator-free paper.
"""

NOTES["sequences"] = r"""
## Key ideas

A sequence $\{a_n\}$ is a list $a_1,a_2,a_3,\dots$. $S_n=a_1+\dots+a_n$ and
$$a_n=\begin{cases}S_1,&n=1\\S_n-S_{n-1},&n\ge2\end{cases}\qquad\text{(always check } n=1\text{)}.$$

## Arithmetic and geometric sequences

| | Arithmetic (difference $d$) | Geometric (ratio $q\ne0$) |
|---|---|---|
| Definition | $a_{n+1}-a_n=d$ | $\dfrac{a_{n+1}}{a_n}=q$ |
| General term | $a_n=a_1+(n-1)d$ | $a_n=a_1q^{n-1}$ |
| Sum | $S_n=\dfrac{n(a_1+a_n)}2=na_1+\dfrac{n(n-1)}2d$ | $S_n=\dfrac{a_1(1-q^n)}{1-q}$ ($q\ne1$); $S_n=na_1$ ($q=1$) |
| Middle term | $2b=a+c$ | $b^2=ac$ |
| Index property | $m+n=p+q\Rightarrow a_m+a_n=a_p+a_q$ | $m+n=p+q\Rightarrow a_ma_n=a_pa_q$ |

Also: $a_n=a_m+(n-m)d$; in an arithmetic sequence $S_{2k-1}=(2k-1)a_k$.

## Useful techniques

- **Telescoping:** $\dfrac1{n(n+1)}=\dfrac1n-\dfrac1{n+1}$.
- **Subtract a shifted copy** for $\sum n\cdot q^n$ (arithmetic × geometric).
- **Recursions:** $a_{n+1}=pa_n+r$ — rewrite as $a_{n+1}+t=p(a_n+t)$ to get a geometric sequence.
- The max of $S_n$ for an arithmetic sequence with $d<0$: add up the terms while they are non-negative.

## Worked examples

**Example 1.** Arithmetic: $a_2=5$, $a_6=17$. Find $a_{10}$ and $S_{10}$.

*Solution.* $4d=12$, $d=3$, $a_1=2$. $a_{10}=2+27=29$; $S_{10}=\dfrac{10(2+29)}{2}=155$.

**Example 2.** Geometric with positive terms: $a_1=2$, $a_3=18$. Find $S_4$.

*Solution.* $q^2=9$, $q=3$. $S_4=\dfrac{2(3^4-1)}{3-1}=80$.

**Example 3.** $S_n=3n^2-n$. Find $a_n$.

*Solution.* For $n\ge2$: $a_n=3n^2-n-[3(n-1)^2-(n-1)]=6n-4$. $a_1=S_1=2=6\cdot1-4$ ✔. So $a_n=6n-4$.

## Common traps

- Using $q^n$ instead of $q^{n-1}$, or $nd$ instead of $(n-1)d$.
- Using the geometric sum formula when $q=1$.
- Forgetting that $a_n=S_n-S_{n-1}$ is only valid for $n\ge2$.
- $b^2=ac$ does not determine the sign of $b$: check whether terms must be positive.
"""

NOTES["derivatives"] = r"""
## Definition and meaning

$$f'(x_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$$

- Geometric meaning: the **slope of the tangent** at $(x_0,f(x_0))$. Tangent line: $y-f(x_0)=f'(x_0)(x-x_0)$.
- Physical meaning: velocity $v(t)=s'(t)$, acceleration $a(t)=v'(t)$.

## Rules

| $f(x)$ | $f'(x)$ |
|---|---|
| $C$ | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x\ln a$ |
| $\ln x$ | $\dfrac1x$ |
| $\log_ax$ | $\dfrac1{x\ln a}$ |

$$(u\pm v)'=u'\pm v',\quad (uv)'=u'v+uv',\quad \left(\frac uv\right)'=\frac{u'v-uv'}{v^2},\quad [f(g(x))]'=f'(g(x))\,g'(x).$$

## Applications

- $f'(x)>0$ on an interval ⇒ $f$ increasing there; $f'(x)<0$ ⇒ decreasing.
- **Local extremum** at $x_0$: $f'(x_0)=0$ **and** $f'$ changes sign ($+\to-$: maximum; $-\to+$: minimum).
- **Max/min on $[a,b]$:** compare $f$ at critical points inside $[a,b]$ and at the endpoints.
- Counting zeros: use the extreme values and the end behaviour.

## Basic integrals

$\displaystyle\int_a^bf(x)\,dx=F(b)-F(a)$ where $F'=f$. Area between curves on $[a,b]$: $\displaystyle\int_a^b(\text{upper}-\text{lower})\,dx$. Examples: $\int x^n dx=\dfrac{x^{n+1}}{n+1}$, $\int\cos x\,dx=\sin x$, $\int\dfrac1x dx=\ln|x|$.

## Worked examples

**Example 1.** Tangent to $y=x^3-2x$ at $x=1$.

*Solution.* $y(1)=-1$, $y'=3x^2-2$, $k=1$. Tangent: $y+1=x-1$, i.e. $y=x-2$.

**Example 2.** Find the extrema of $f(x)=x^3-3x^2+1$.

*Solution.* $f'(x)=3x(x-2)$: $+$ for $x<0$, $-$ on $(0,2)$, $+$ for $x>2$. Local max $f(0)=1$, local min $f(2)=-3$.

**Example 3.** $f(x)=x^2-a\ln x$ has an extremum at $x=1$. Find $a$.

*Solution.* $f'(x)=2x-\dfrac ax$, $f'(1)=2-a=0\Rightarrow a=2$. Check: $f'(x)=\dfrac{2(x^2-1)}x$ changes sign at $1$ ✔.

## Common traps

- $f'(x_0)=0$ alone does not guarantee an extremum ($f(x)=x^3$ at $0$).
- Tangent **at** a point vs tangent **through** a point (the point may not be on the curve).
- In $\lim\dfrac{f(x_0+2h)-f(x_0)}{h}$ the answer is $2f'(x_0)$.
- Forgetting the domain (e.g. $x>0$ for $\ln x$) when finding monotonic intervals.
"""

for k, v in NOTES.items():
    (OUT / f"{k}.md").write_text(v.strip() + "\n", encoding="utf8")
    print("wrote", k)
