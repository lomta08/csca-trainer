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
