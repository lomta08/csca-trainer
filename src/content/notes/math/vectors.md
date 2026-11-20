## Key ideas

A vector has magnitude and direction. In coordinates $\vec a=(x_1,y_1)$, $\vec b=(x_2,y_2)$:

$$\vec a\pm\vec b=(x_1\pm x_2,\ y_1\pm y_2),\qquad \lambda\vec a=(\lambda x_1,\lambda y_1),\qquad |\vec a|=\sqrt{x_1^2+y_1^2}.$$

$\overrightarrow{AB}=B-A$ (end minus start). Triangle rule: $\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$. Parallelogram $ABCD$: $\overrightarrow{AB}+\overrightarrow{AD}=\overrightarrow{AC}$.

## Dot product

$$\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta=x_1x_2+y_1y_2,\qquad \cos\theta=\frac{\vec a\cdot\vec b}{|\vec a||\vec b|},\ \theta\in[0,\pi].$$

- $\vec a\perp\vec b\iff\vec a\cdot\vec b=0\iff x_1x_2+y_1y_2=0$.
- $\vec a\parallel\vec b\iff x_1y_2-x_2y_1=0$.
- $|\vec a|^2=\vec a\cdot\vec a$, so $|\vec a\pm\vec b|^2=|\vec a|^2\pm2\vec a\cdot\vec b+|\vec b|^2$.
- Projection (scalar) of $\vec a$ on $\vec b$: $|\vec a|\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec b|}$.
- Unit vector in the direction of $\vec a$: $\dfrac{\vec a}{|\vec a|}$.

## Worked examples

**Example 1.** $\vec a=(1,2)$, $\vec b=(-2,k)$, $\vec a\perp\vec b$. Find $k$ and $|\vec a+\vec b|$.

*Solution.* $-2+2k=0\Rightarrow k=1$. $\vec a+\vec b=(-1,3)$, $|\vec a+\vec b|=\sqrt{10}$.

**Example 2.** $|\vec a|=2$, $|\vec b|=1$, angle $60^\circ$. Find $|2\vec a-\vec b|$.

*Solution.* $\vec a\cdot\vec b=1$. $|2\vec a-\vec b|^2=4\cdot4-4\cdot1+1=13$, so $\sqrt{13}$.

**Example 3.** Find the angle between $\vec a=(1,\sqrt3)$ and $\vec b=(-1,\sqrt3)$.

*Solution.* $\cos\theta=\dfrac{-1+3}{2\cdot2}=\dfrac12$, $\theta=\dfrac\pi3$.

## Common traps

- Mixing up the parallel ($x_1y_2-x_2y_1=0$) and perpendicular ($x_1x_2+y_1y_2=0$) conditions.
- $\vec a\cdot\vec b<0$ means an **obtuse** angle (or $\pi$), not "negative angle".
- $|\vec a+\vec b|\ne|\vec a|+|\vec b|$ in general — square it first.
