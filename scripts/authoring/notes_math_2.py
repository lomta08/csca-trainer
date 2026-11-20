"""Writes math lesson notes (part 2) to src/content/notes/math/*.md. Original explanations."""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "src" / "content" / "notes" / "math"
OUT.mkdir(parents=True, exist_ok=True)
NOTES = {}

NOTES["lines-circles"] = r"""
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
"""

NOTES["conics"] = r"""
## Ellipse

Definition: $|PF_1|+|PF_2|=2a>|F_1F_2|$.

$\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ ($a>b>0$, foci on the $x$-axis) or $\dfrac{y^2}{a^2}+\dfrac{x^2}{b^2}=1$ (foci on the $y$-axis). **The larger denominator is $a^2$.**

$$c^2=a^2-b^2,\qquad e=\frac ca\in(0,1),\qquad \text{foci }(\pm c,0),\ \text{vertices }(\pm a,0),(0,\pm b).$$
Major axis $2a$, minor axis $2b$, focal distance $2c$. Perimeter of $\triangle PF_1F_2$: $2a+2c$.

## Hyperbola

Definition: $\big||PF_1|-|PF_2|\big|=2a<|F_1F_2|$.

$\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$ (foci on the $x$-axis) or $\dfrac{y^2}{a^2}-\dfrac{x^2}{b^2}=1$ (foci on the $y$-axis). **The positive term gives the axis.**

$$c^2=a^2+b^2,\qquad e=\frac ca>1,\qquad \text{asymptotes } y=\pm\frac bax\ \left(\text{or } y=\pm\frac abx\right).$$
Quick asymptotes: replace the $1$ by $0$ and solve. $e=\sqrt{1+\left(\frac ba\right)^2}$. The distance from a focus to an asymptote equals $b$.

## Parabola

Definition: distance to the focus = distance to the directrix.

| Equation | Focus | Directrix |
|---|---|---|
| $y^2=2px$ | $\left(\frac p2,0\right)$ | $x=-\frac p2$ |
| $y^2=-2px$ | $\left(-\frac p2,0\right)$ | $x=\frac p2$ |
| $x^2=2py$ | $\left(0,\frac p2\right)$ | $y=-\frac p2$ |
| $x^2=-2py$ | $\left(0,-\frac p2\right)$ | $y=\frac p2$ |

For $P(x_0,y_0)$ on $y^2=2px$: $|PF|=x_0+\dfrac p2$. A focal chord has length $x_1+x_2+p$.

## Worked examples

**Example 1.** Find $e$ and the foci of $\dfrac{x^2}{9}+\dfrac{y^2}{25}=1$.

*Solution.* $a^2=25$ (under $y^2$), $b^2=9$, $c=4$. Foci $(0,\pm4)$, $e=\dfrac45$.

**Example 2.** A hyperbola has asymptotes $y=\pm\dfrac34x$ and a focus $(5,0)$. Find its equation.

*Solution.* $\dfrac ba=\dfrac34$ and $a^2+b^2=25$: $a=4,b=3$. Equation $\dfrac{x^2}{16}-\dfrac{y^2}9=1$.

**Example 3.** Find the focus of $y=\tfrac14x^2$.

*Solution.* Rewrite $x^2=4y$: $2p=4$, focus $(0,1)$.

## Common traps

- Ellipse: $c^2=a^2-b^2$; hyperbola: $c^2=a^2+b^2$ — do not mix them up.
- Not putting a parabola in standard form first ($y=2x^2$ means $x^2=\tfrac12y$).
- Deciding the axis from the order of the terms instead of from the larger denominator / positive term.
- For hyperbola focal-distance problems, check which branch the point lies on.
"""

NOTES["vectors"] = r"""
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
"""

NOTES["complex-numbers"] = r"""
## Key ideas

$i^2=-1$. A complex number $z=a+bi$ ($a,b\in\mathbb R$) has **real part** $a$ and **imaginary part** $b$ (not $bi$).

- $z$ is real if $b=0$; **purely imaginary** if $a=0$ and $b\ne0$.
- $a+bi=c+di\iff a=c$ and $b=d$.
- Conjugate $\bar z=a-bi$; $z\bar z=a^2+b^2=|z|^2$.
- Modulus $|z|=\sqrt{a^2+b^2}$ = distance from the origin to $(a,b)$ in the complex plane.
- Powers of $i$ repeat with period $4$: $i,\ -1,\ -i,\ 1$.

## Operations

$$(a+bi)(c+di)=(ac-bd)+(ad+bc)i,\qquad \frac{a+bi}{c+di}=\frac{(a+bi)(c-di)}{c^2+d^2}.$$

Modulus rules: $|z_1z_2|=|z_1||z_2|$, $\left|\dfrac{z_1}{z_2}\right|=\dfrac{|z_1|}{|z_2|}$.

Geometry: $|z-z_0|=r$ is a circle with centre $z_0$; $|z-z_1|=|z-z_2|$ is the perpendicular bisector of $z_1z_2$.

## Worked examples

**Example 1.** Simplify $\dfrac{3+i}{1+i}$.

*Solution.* $\dfrac{(3+i)(1-i)}{2}=\dfrac{3-3i+i-i^2}{2}=\dfrac{4-2i}{2}=2-i$.

**Example 2.** $z=(1-i)^2+\dfrac{2}{i}$. Find $|z|$.

*Solution.* $(1-i)^2=-2i$ and $\dfrac2i=-2i$, so $z=-4i$, $|z|=4$.

**Example 3.** $(m^2-1)+(m+1)i$ is purely imaginary. Find the real number $m$.

*Solution.* $m^2-1=0$ and $m+1\ne0$, so $m=1$.

## Common traps

- Writing $i^2=1$.
- Forgetting "$b\ne0$" for purely imaginary numbers.
- Saying the imaginary part of $3-2i$ is $-2i$ (it is $-2$).
- Dividing without multiplying by the **conjugate** of the denominator.
"""

NOTES["solid-geometry"] = r"""
## Space rectangular coordinates

A point is $(x,y,z)$. For $A(x_1,y_1,z_1)$, $B(x_2,y_2,z_2)$:
$$|AB|=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2},\qquad \text{midpoint}\left(\tfrac{x_1+x_2}2,\tfrac{y_1+y_2}2,\tfrac{z_1+z_2}2\right).$$

Symmetric points of $(x,y,z)$: about the $xOy$ plane $(x,y,-z)$; about the $z$-axis $(-x,-y,z)$; about the origin $(-x,-y,-z)$. Distance to the $z$-axis: $\sqrt{x^2+y^2}$.

## Surface area and volume

| Solid | Volume | Surface |
|---|---|---|
| Prism / cylinder | $V=Sh$ | cylinder: $2\pi r^2+2\pi rh$ |
| Pyramid / cone | $V=\tfrac13Sh$ | cone lateral: $\pi rl$ ($l$ = slant height) |
| Sphere | $V=\tfrac43\pi R^3$ | $S=4\pi R^2$ |
| Frustum of cone | $V=\tfrac13\pi h(r^2+rR+R^2)$ | |

Box diagonal: $\sqrt{a^2+b^2+c^2}$; cube diagonal $a\sqrt3$. A box (or cube) inscribed in a sphere: the sphere's **diameter** is the box diagonal. Regular tetrahedron with edge $a$: $V=\dfrac{\sqrt2}{12}a^3$.

## Lines and planes (key theorems)

- Two lines perpendicular to the same plane are parallel.
- A line is perpendicular to a plane if it is perpendicular to **two intersecting** lines in the plane.
- A line parallel to a line in a plane (and not in it) is parallel to the plane.
- Two lines in space can be parallel, intersecting or **skew**.

## Worked examples

**Example 1.** Find the distance between $A(1,-2,3)$ and $B(3,0,2)$.

*Solution.* $\sqrt{4+4+1}=3$.

**Example 2.** A cube has surface area $24$. Find the volume of its circumscribed sphere.

*Solution.* Edge $2$, diagonal $2\sqrt3$, $R=\sqrt3$, $V=\tfrac43\pi(\sqrt3)^3=4\sqrt3\pi$.

**Example 3.** A cone has base radius $3$ and slant height $5$. Find its volume.

*Solution.* Height $h=\sqrt{25-9}=4$, $V=\tfrac13\pi\cdot9\cdot4=12\pi$.

## Common traps

- Forgetting the $\tfrac13$ for cones and pyramids.
- Using the slant height as the height.
- Radius vs diameter of a circumscribed sphere.
"""

NOTES["classical-probability"] = r"""
## Key ideas

**Classical probability:** if all $n$ outcomes are equally likely and $m$ are favourable, $P(A)=\dfrac mn$.

Count carefully:

- **Ordered or not?** Rolling two dice gives $36$ ordered outcomes. Drawing $2$ balls "at the same time" is unordered: $C_n^2$ outcomes.
- Combinations $C_n^k=\dfrac{n!}{k!(n-k)!}$; permutations $A_n^k=\dfrac{n!}{(n-k)!}$.
- Small cases: **list** them systematically (tree or table).

**Rules**

- Complement: $P(\bar A)=1-P(A)$ — great for "at least one".
- Mutually exclusive events: $P(A\cup B)=P(A)+P(B)$.
- In general: $P(A\cup B)=P(A)+P(B)-P(AB)$.
- Independent events: $P(AB)=P(A)P(B)$.
- $n$ independent trials with success probability $p$: $P(k\text{ successes})=C_n^kp^k(1-p)^{n-k}$.

## Worked examples

**Example 1.** Two dice are rolled. Find $P(\text{sum}=8)$.

*Solution.* $(2,6),(3,5),(4,4),(5,3),(6,2)$: $5$ of $36$, so $\dfrac5{36}$.

**Example 2.** From $4$ red and $2$ white balls, $2$ are drawn. Find $P(\text{at least one white})$.

*Solution.* $P(\text{no white})=\dfrac{C_4^2}{C_6^2}=\dfrac6{15}$, so the answer is $1-\dfrac25=\dfrac35$.

**Example 3.** A and B each solve a problem independently with probabilities $0.6$ and $0.5$. Find $P(\text{the problem is solved})$.

*Solution.* $1-0.4\times0.5=0.8$.

## Common traps

- Treating unordered outcomes as ordered (or the reverse) in the numerator but not the denominator.
- Listing "sum = 2, 3, …, 12" as equally likely outcomes — they are not.
- Adding probabilities of events that can happen together.
"""

NOTES["mean-variance"] = r"""
## Key ideas

For data $x_1,\dots,x_n$:

$$\bar x=\frac1n\sum x_i,\qquad s^2=\frac1n\sum(x_i-\bar x)^2=\frac1n\sum x_i^2-\bar x^2,\qquad s=\sqrt{s^2}.$$

- **Median:** the middle value after sorting (average of the two middle values if $n$ is even).
- **Mode:** the most frequent value. **Range:** max − min.
- Variance and standard deviation measure **spread**: smaller means more stable/consistent.
- With frequencies $f_i$: $\bar x=\dfrac{\sum f_ix_i}{\sum f_i}$.

**Linear transformation** $y_i=ax_i+b$: $$\bar y=a\bar x+b,\qquad s_y^2=a^2s_x^2,\qquad s_y=|a|s_x.$$

**Random variables:** $E(X)=\sum x_ip_i$, $D(X)=\sum(x_i-E X)^2p_i=E(X^2)-[E(X)]^2$, $E(aX+b)=aE(X)+b$, $D(aX+b)=a^2D(X)$.

## Worked examples

**Example 1.** Find the variance of $3,5,7,9,11$.

*Solution.* $\bar x=7$; deviations $-4,-2,0,2,4$; $s^2=\dfrac{16+4+0+4+16}{5}=8$.

**Example 2.** Data have mean $10$ and standard deviation $2$. Each value is multiplied by $3$ and $5$ is subtracted. Find the new mean and variance.

*Solution.* Mean $3\cdot10-5=25$; variance $9\cdot4=36$.

**Example 3.** $X$ takes $1,2,3$ with probabilities $0.2,0.5,0.3$. Find $E(X)$.

*Solution.* $0.2+1.0+0.9=2.1$.

## Common traps

- Dividing by $n-1$: the CSCA (gaokao) definition divides by $n$.
- Forgetting to **square** $a$ in $D(aX+b)$, or thinking $b$ changes the variance.
- Finding the median without sorting the data first.
"""

NOTES["normal-distribution"] = r"""
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
"""

for k, v in NOTES.items():
    (OUT / f"{k}.md").write_text(v.strip() + "\n", encoding="utf8")
    print("wrote", k)
