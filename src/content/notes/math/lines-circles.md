## Lines

Slope through $(x_1,y_1),(x_2,y_2)$: $k=\dfrac{y_2-y_1}{x_2-x_1}=\tan\alpha$ ($\alpha$ = inclination angle, $0\le\alpha<\pi$; vertical lines have no slope).

| Form | Equation |
|---|---|
| Point–slope | $y-y_0=k(x-x_0)$ |
| Slope–intercept | $y=kx+b$ |
| Intercept | $\dfrac xa+\dfrac yb=1$ |
| General | $Ax+By+C=0$ |

For $l_1:A_1x+B_1y+C_1=0$ and $l_2:A_2x+B_2y+C_2=0$:

- parallel: $A_1B_2-A_2B_1=0$ and the lines are not identical (with slopes: $k_1=k_2$, $b_1\ne b_2$);
- perpendicular: $A_1A_2+B_1B_2=0$ (with slopes: $k_1k_2=-1$).

**Distances:** point to line $d=\dfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$; parallel lines $d=\dfrac{|C_1-C_2|}{\sqrt{A^2+B^2}}$ (same $A,B$); two points $\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$; midpoint $\left(\frac{x_1+x_2}2,\frac{y_1+y_2}2\right)$.

## Circles

Standard form $(x-a)^2+(y-b)^2=r^2$: centre $(a,b)$, radius $r$.
General form $x^2+y^2+Dx+Ey+F=0$: centre $\left(-\dfrac D2,-\dfrac E2\right)$, $r=\dfrac12\sqrt{D^2+E^2-4F}$ (needs $D^2+E^2-4F>0$).

**Line and circle:** compare the distance $d$ from the centre to the line with $r$: $d<r$ intersect (2 points), $d=r$ tangent, $d>r$ separate. Chord length $=2\sqrt{r^2-d^2}$.

## Worked examples

**Example 1.** Find the line through $(2,-1)$ perpendicular to $2x-y+3=0$.

*Solution.* Given slope $2$, so the new slope is $-\tfrac12$: $y+1=-\tfrac12(x-2)$, i.e. $x+2y=0$.

**Example 2.** Find the centre and radius of $x^2+y^2+2x-4y-4=0$.

*Solution.* $(x+1)^2+(y-2)^2=9$: centre $(-1,2)$, radius $3$.

**Example 3.** Find the chord cut by $3x+4y-5=0$ on $x^2+y^2=4$.

*Solution.* $d=\dfrac{5}{5}=1$, chord $=2\sqrt{4-1}=2\sqrt3$.

## Common traps

- Sign of the centre: $(x-2)^2+(y+3)^2=r^2$ has centre $(2,-3)$.
- Forgetting vertical lines ($x=x_0$) when you assume a slope exists.
- For parallel lines, also rule out coincident lines.
- Using the parallel-line distance formula without first making $A,B$ equal.
