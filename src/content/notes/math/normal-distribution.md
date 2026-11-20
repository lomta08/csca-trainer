## Key ideas

$X\sim N(\mu,\sigma^2)$ has a bell-shaped density curve:

- symmetric about the line $x=\mu$ (mean = median = mode = $\mu$);
- highest at $x=\mu$; the peak height is $\dfrac1{\sigma\sqrt{2\pi}}$;
- larger $\sigma$ → flatter and more spread out; smaller $\sigma$ → taller and narrower;
- the total area under the curve is $1$; areas are probabilities.

**The 68–95–99.7 rule**

$$P(\mu-\sigma<X<\mu+\sigma)\approx0.6827,\quad P(\mu-2\sigma<X<\mu+2\sigma)\approx0.9545,\quad P(\mu-3\sigma<X<\mu+3\sigma)\approx0.9973.$$

**Symmetry tricks** (no table needed):

- $P(X<\mu)=P(X>\mu)=0.5$;
- $P(X<\mu-a)=P(X>\mu+a)$;
- if $P(X<c_1)=P(X>c_2)$ then $\mu=\dfrac{c_1+c_2}2$;
- standardising: $Z=\dfrac{X-\mu}\sigma\sim N(0,1)$.

## Worked examples

**Example 1.** $X\sim N(2,\sigma^2)$ and $P(X<4)=0.8$. Find $P(0<X<2)$.

*Solution.* $P(2<X<4)=0.8-0.5=0.3$; by symmetry $P(0<X<2)=0.3$.

**Example 2.** Heights are $N(170,5^2)$ (cm). About what fraction is taller than $180$ cm?

*Solution.* $180=\mu+2\sigma$: $\dfrac{1-0.9545}{2}\approx0.023$, about $2.3\%$.

**Example 3.** $X\sim N(\mu,\sigma^2)$ with $P(X<-1)=P(X>3)$. Find $\mu$.

*Solution.* $\mu=\dfrac{-1+3}{2}=1$.

## Common traps

- Forgetting to halve the outside area ($1-0.9545$ covers **both** tails).
- Thinking a larger $\sigma$ moves the curve; it only spreads it ($\mu$ sets the position).
- Writing $N(\mu,\sigma)$ when the notation is $N(\mu,\sigma^2)$: $N(1,4)$ has $\sigma=2$.
