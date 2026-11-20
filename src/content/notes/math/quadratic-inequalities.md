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
