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
