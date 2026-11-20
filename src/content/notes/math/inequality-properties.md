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
