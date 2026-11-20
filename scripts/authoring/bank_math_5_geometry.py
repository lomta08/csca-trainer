from qb import *  # noqa: F403

B = Bank("math", "geometry-algebra")
R_ = sp.S.Reals


def dist_pl(px, py, A, Bc, C):
    return sp.Abs(A * px + Bc * py + C) / sp.sqrt(A ** 2 + Bc ** 2)


def vec(*c):
    return sp.Matrix(c)


def angle(u, v):
    return sp.acos(u.dot(v) / (u.norm() * v.norm()))


def quadrant(zv):
    re_, im_ = sp.re(zv), sp.im(zv)
    if re_ > 0 and im_ > 0:
        return "First quadrant"
    if re_ < 0 and im_ > 0:
        return "Second quadrant"
    if re_ < 0 and im_ < 0:
        return "Third quadrant"
    return "Fourth quadrant"


I = sp.I

# ---------------------------------------------------------- lines & circles
B.q("m-line-01", "lines-circles", 1,
    r"The slope of the line through $(1,2)$ and $(3,6)$ is",
    [r"$2$", r"$\dfrac12$", r"$4$", r"$-2$"],
    r"$k=\dfrac{y_2-y_1}{x_2-x_1}=\dfrac{6-2}{3-1}=2$.",
    N(sp.Rational(6 - 2, 3 - 1)))

B.q("m-line-02", "lines-circles", 2,
    r"The line through $(1,2)$ parallel to $2x-y+1=0$ is",
    [r"$2x-y=0$", r"$x+2y-5=0$", r"$2x-y+3=0$", r"$2x+y-4=0$"],
    r"A parallel line has the same left side: $2x-y+c=0$. Substitute $(1,2)$: $2-2+c=0$, $c=0$. So $2x-y=0$.",
    Eqn(2 * x - y - (2 * 1 - 2)))

B.q("m-line-03", "lines-circles", 2,
    r"The line through $(0,1)$ perpendicular to $x+2y-3=0$ is",
    [r"$2x-y+1=0$", r"$x+2y-2=0$", r"$2x+y-1=0$", r"$x-2y+2=0$"],
    r"The given line has slope $-\dfrac12$, so a perpendicular line has slope $2$ (product $-1$). Through $(0,1)$: $y=2x+1$, i.e. $2x-y+1=0$.",
    Eqn(y - (-1 / sp.Rational(-1, 2) * x + 1)))

B.q("m-line-04", "lines-circles", 1,
    r"The distance between the parallel lines $3x+4y-5=0$ and $3x+4y+5=0$ is",
    [r"$2$", r"$10$", r"$1$", r"$0$"],
    r"For $Ax+By+C_1=0$ and $Ax+By+C_2=0$: $d=\dfrac{|C_1-C_2|}{\sqrt{A^2+B^2}}=\dfrac{10}{5}=2$.",
    N(dist_pl(0, sp.Rational(5, 4), 3, 4, 5)))

B.q("m-line-05", "lines-circles", 1,
    r"The distance from the point $(1,1)$ to the line $3x+4y+3=0$ is",
    [r"$2$", r"$10$", r"$\dfrac{7}{5}$", r"$\dfrac45$"],
    r"$d=\dfrac{|3\cdot1+4\cdot1+3|}{\sqrt{3^2+4^2}}=\dfrac{10}5=2$.",
    N(dist_pl(1, 1, 3, 4, 3)))

_cx6, _cy6 = sp.Rational(4, 2), sp.Rational(-6, 2)
B.q("m-line-06", "lines-circles", 1,
    r"The circle $x^2+y^2-4x+6y=0$ has",
    [r"centre $(2,-3)$, radius $\sqrt{13}$", r"centre $(-2,3)$, radius $\sqrt{13}$", r"centre $(2,-3)$, radius $13$", r"centre $(-2,3)$, radius $13$"],
    r"Complete the squares: $(x-2)^2+(y+3)^2=4+9=13$. Centre $(2,-3)$, radius $\sqrt{13}$.",
    CR(_cx6, _cy6, sp.sqrt(_cx6 ** 2 + _cy6 ** 2)))

_d7 = dist_pl(1, 0, 1, -1, 1)
B.q("m-line-07", "lines-circles", 2,
    r"The line $x-y+1=0$ and the circle $(x-1)^2+y^2=2$ are",
    [r"Tangent", r"Intersecting at two points", r"Separate (no common point)", r"Intersecting, and the line passes through the centre"],
    r"Distance from the centre $(1,0)$ to the line: $d=\dfrac{|1-0+1|}{\sqrt2}=\sqrt2$, which equals the radius $\sqrt2$. So the line is tangent to the circle.",
    T("Tangent" if sp.simplify(_d7 - sp.sqrt(2)) == 0 else ("Separate (no common point)" if _d7 > sp.sqrt(2) else "Intersecting at two points")))

_d8 = dist_pl(0, 0, 1, 1, -2)
B.q("m-line-08", "lines-circles", 2,
    r"The line $x+y-2=0$ cuts the circle $x^2+y^2=4$. The length of the chord is",
    [r"$2\sqrt2$", r"$\sqrt2$", r"$4$", r"$2$"],
    r"Distance from the centre to the line: $d=\dfrac{|-2|}{\sqrt2}=\sqrt2$. Half-chord $=\sqrt{r^2-d^2}=\sqrt{4-2}=\sqrt2$, so the chord is $2\sqrt2$.",
    N(2 * sp.sqrt(4 - _d8 ** 2)))

B.q("m-line-09", "lines-circles", 2,
    r"The circle with centre $(1,2)$ that is tangent to the $x$-axis is",
    [r"$(x-1)^2+(y-2)^2=4$", r"$(x-1)^2+(y-2)^2=1$", r"$(x+1)^2+(y+2)^2=4$", r"$(x-1)^2+(y-2)^2=2$"],
    r"Tangent to the $x$-axis means the radius equals the distance from the centre to the $x$-axis, $|2|=2$. So $(x-1)^2+(y-2)^2=4$.",
    Eqn((x - 1) ** 2 + (y - 2) ** 2 - 2 ** 2))

_c10 = ((-1 + 3) / sp.Integer(2), (2 + 4) / sp.Integer(2))
B.q("m-line-10", "lines-circles", 2,
    r"The circle with diameter $AB$, where $A(-1,2)$ and $B(3,4)$, is",
    [r"$(x-1)^2+(y-3)^2=5$", r"$(x-1)^2+(y-3)^2=20$", r"$(x+1)^2+(y+3)^2=5$", r"$(x-2)^2+(y-1)^2=5$"],
    r"Centre = midpoint $(1,3)$; radius $=\dfrac12|AB|=\dfrac12\sqrt{16+4}=\sqrt5$. Equation: $(x-1)^2+(y-3)^2=5$.",
    Eqn((x - _c10[0]) ** 2 + (y - _c10[1]) ** 2 - ((3 - _c10[0]) ** 2 + (4 - _c10[1]) ** 2)))

B.q("m-line-11", "lines-circles", 2,
    r"The line with $x$-intercept $2$ and $y$-intercept $-3$ is",
    [r"$3x-2y-6=0$", r"$2x-3y-6=0$", r"$3x+2y-6=0$", r"$2x+3y+6=0$"],
    r"Intercept form: $\dfrac x2+\dfrac y{-3}=1$. Multiply by $6$: $3x-2y=6$, i.e. $3x-2y-6=0$.",
    Eqn(x / 2 + y / (-3) - 1))

B.q("m-line-12", "lines-circles", 2,
    r"The lines $ax+2y+1=0$ and $x+(a-1)y-1=0$ are perpendicular. Then $a=$",
    [r"$\dfrac23$", r"$2$", r"$-1$", r"$\dfrac32$"],
    r"$A_1x+B_1y+C_1=0\perp A_2x+B_2y+C_2=0\iff A_1A_2+B_1B_2=0$: $a\cdot1+2(a-1)=0$, so $a=\dfrac23$.",
    N(sp.solve(a * 1 + 2 * (a - 1), a)[0]))


def _parallel_vals():
    out = []
    for av in sp.solve(a * (a - 1) - 2 * 1, a):
        l1 = sp.Matrix([av, 2, 1])
        l2 = sp.Matrix([1, av - 1, -1])
        if sp.Matrix.hstack(l1, l2).rank() == 2:  # not the same line
            out.append(av)
    return out


B.q("m-line-13", "lines-circles", 3,
    r"The lines $ax+2y+1=0$ and $x+(a-1)y-1=0$ are parallel (and distinct). Then $a=$",
    [r"$2$", r"$-1$", r"$2$ or $-1$", r"$1$"],
    r"""Parallel requires $A_1B_2-A_2B_1=0$: $a(a-1)-2=0$, so $a=2$ or $a=-1$.

Now exclude coincident lines. $a=-1$: the lines are $-x+2y+1=0$ and $x-2y-1=0$, which are the **same** line. $a=2$: $2x+2y+1=0$ and $x+y-1=0$ are distinct ✔. So $a=2$.""",
    N(_parallel_vals()[0]) if len(_parallel_vals()) == 1 else N(999))

B.q("m-line-14", "lines-circles", 3,
    r"$P$ is a point on the circle $x^2+y^2=1$. The maximum distance from $P$ to the line $3x+4y-10=0$ is",
    [r"$3$", r"$2$", r"$1$", r"$\dfrac{11}{5}$"],
    r"Distance from the centre to the line: $\dfrac{|-10|}5=2>1$, so the line misses the circle. The farthest point is on the far side: $2+r=3$.",
    N(dist_pl(0, 0, 3, 4, -10) + 1))

B.q("m-line-15", "lines-circles", 3,
    r"For every real $k$, the line $y=kx+1$ and the circle $x^2+y^2=4$",
    [r"intersect at two points", r"are tangent", r"are separate", r"may be tangent or separate depending on $k$"],
    r"Every line $y=kx+1$ passes through $(0,1)$, and $0^2+1^2=1<4$, so this point is **inside** the circle. A line through an interior point always meets the circle at two points.")

B.q("m-line-16", "lines-circles", 1,
    r"The midpoint of $A(2,-1)$ and $B(-4,5)$ is",
    [r"$(-1,2)$", r"$(-2,4)$", r"$(3,-3)$", r"$(-1,3)$"],
    r"Midpoint $=\left(\dfrac{2+(-4)}2,\dfrac{-1+5}2\right)=(-1,2)$.",
    Pt(sp.Rational(2 - 4, 2), sp.Rational(-1 + 5, 2)))

# --------------------------------------------------------------- conics
B.q("m-con-01", "conics", 1,
    r"The foci of the ellipse $\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$ are",
    [r"$(\pm4,0)$", r"$(0,\pm4)$", r"$(\pm5,0)$", r"$(\pm\sqrt{34},0)$"],
    r"$a^2=25$ (under $x^2$, so the major axis is horizontal), $b^2=9$, $c^2=a^2-b^2=16$, $c=4$. Foci $(\pm4,0)$.",
    Foci(sp.sqrt(25 - 9), "x"))

B.q("m-con-02", "conics", 2,
    r"The eccentricity of the ellipse $\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$ is",
    [r"$\dfrac12$", r"$\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt7}{2}$", r"$\dfrac14$"],
    r"$a=2$, $c=\sqrt{4-3}=1$, so $e=\dfrac ca=\dfrac12$.",
    N(sp.sqrt(4 - 3) / 2))

B.q("m-con-03", "conics", 2,
    r"The asymptotes of the hyperbola $\dfrac{x^2}{9}-\dfrac{y^2}{16}=1$ are",
    [r"$y=\pm\dfrac43x$", r"$y=\pm\dfrac34x$", r"$y=\pm\dfrac{16}9x$", r"$y=\pm\dfrac53x$"],
    r"For $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$ the asymptotes are $y=\pm\dfrac bax$. Here $a=3$, $b=4$: $y=\pm\dfrac43x$.",
    Asym(sp.Rational(4, 3)))

B.q("m-con-04", "conics", 1,
    r"The focus of the parabola $y^2=8x$ is",
    [r"$(2,0)$", r"$(4,0)$", r"$(0,2)$", r"$(-2,0)$"],
    r"Compare with $y^2=2px$: $2p=8$, $p=4$, focus $\left(\dfrac p2,0\right)=(2,0)$.",
    Pt(sp.Rational(8, 4), 0))

B.q("m-con-05", "conics", 1,
    r"The directrix of the parabola $x^2=4y$ is",
    [r"$y=-1$", r"$y=1$", r"$x=-1$", r"$y=-2$"],
    r"$x^2=2py$ with $2p=4$, so $\dfrac p2=1$. Focus $(0,1)$, directrix $y=-1$.",
    Eqn(y + sp.Rational(4, 4)))

_a6, _c6 = 5, 3
B.q("m-con-06", "conics", 2,
    r"An ellipse has foci $(\pm3,0)$ and major axis of length $10$. Its equation is",
    [r"$\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$", r"$\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$", r"$\dfrac{x^2}{16}+\dfrac{y^2}{25}=1$", r"$\dfrac{x^2}{100}+\dfrac{y^2}{91}=1$"],
    r"$2a=10\Rightarrow a=5$; $c=3$; $b^2=a^2-c^2=16$. Foci on the $x$-axis: $\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$.",
    Eqn(x ** 2 / _a6 ** 2 + y ** 2 / (_a6 ** 2 - _c6 ** 2) - 1))

B.q("m-con-07", "conics", 2,
    r"$P$ is a point on the ellipse $\dfrac{x^2}{16}+\dfrac{y^2}{9}=1$ with foci $F_1$, $F_2$. Then $|PF_1|+|PF_2|=$",
    [r"$8$", r"$6$", r"$4$", r"$2\sqrt7$"],
    r"By the definition of an ellipse, $|PF_1|+|PF_2|=2a=2\cdot4=8$.",
    N(2 * sp.sqrt(16)))

B.q("m-con-08", "conics", 2,
    r"$F_1$, $F_2$ are the foci of the ellipse $\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$ and $P$ is on the ellipse. The perimeter of $\triangle PF_1F_2$ is",
    [r"$16$", r"$10$", r"$18$", r"$13$"],
    r"$|PF_1|+|PF_2|=2a=10$ and $|F_1F_2|=2c=2\sqrt{25-16}=6$. Perimeter $=16$.",
    N(2 * 5 + 2 * sp.sqrt(25 - 16)))

B.q("m-con-09", "conics", 2,
    r"One asymptote of the hyperbola $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$ $(a,b>0)$ is $y=2x$. Its eccentricity is",
    [r"$\sqrt5$", r"$\dfrac{\sqrt5}{2}$", r"$\sqrt3$", r"$2$"],
    r"$\dfrac ba=2$, so $e=\dfrac ca=\sqrt{\dfrac{a^2+b^2}{a^2}}=\sqrt{1+\left(\dfrac ba\right)^2}=\sqrt5$.",
    N(sp.sqrt(1 + 2 ** 2)))

_P10 = (3, 2 * sp.sqrt(3))
B.q("m-con-10", "conics", 2,
    r"A point $P$ on the parabola $y^2=4x$ has $x$-coordinate $3$. The distance from $P$ to the focus is",
    [r"$4$", r"$3$", r"$2\sqrt3$", r"$5$"],
    r"Distance to the focus = distance to the directrix $x=-1$ (definition of a parabola): $3-(-1)=4$.",
    N(sp.sqrt((_P10[0] - 1) ** 2 + _P10[1] ** 2)))

B.q("m-con-11", "conics", 3,
    r"The ellipse $\dfrac{x^2}{m}+\dfrac{y^2}{4}=1$ has its foci on the $y$-axis and eccentricity $\dfrac12$. Then $m=$",
    [r"$3$", r"$\dfrac{16}3$", r"$2$", r"$5$"],
    r"Foci on the $y$-axis means $a^2=4$, $b^2=m$ (with $m<4$). $e^2=\dfrac{c^2}{a^2}=\dfrac{4-m}4=\dfrac14$, so $m=3$. ($\tfrac{16}3$ would put the foci on the $x$-axis.)",
    N([v for v in sp.solve((4 - m) / 4 - sp.Rational(1, 4), m) if 0 < v < 4][0]))

B.q("m-con-12", "conics", 3,
    r"The equation $\dfrac{x^2}{k-2}+\dfrac{y^2}{5-k}=1$ represents an ellipse with foci on the $x$-axis. The range of $k$ is",
    [r"$\left(\dfrac72,5\right)$", r"$(2,5)$", r"$\left(2,\dfrac72\right)$", r"$(5,+\infty)$"],
    r"Need both denominators positive and the $x^2$ denominator larger: $k-2>5-k>0$. So $k>\dfrac72$ and $k<5$.",
    S(sp.Intersection(sp.solveset(k - 2 > 5 - k, k, R_), sp.solveset(5 - k > 0, k, R_))))

B.q("m-con-13", "conics", 3,
    r"$F_1$, $F_2$ are the left and right foci of $\dfrac{x^2}{4}-\dfrac{y^2}{5}=1$. $P$ is on the right branch with $|PF_1|=6$. Then $|PF_2|=$",
    [r"$2$", r"$10$", r"$4$", r"$8$"],
    r"On the right branch $|PF_1|-|PF_2|=2a=4$, so $|PF_2|=2$. This is possible because the minimum of $|PF_2|$ on the right branch is $c-a=3-2=1\le2$.",
    N(6 - 2 * 2) if 6 - 4 >= sp.sqrt(4 + 5) - 2 else N(999))

B.q("m-con-14", "conics", 2,
    r"The length of the major axis of the ellipse $4x^2+y^2=16$ is",
    [r"$8$", r"$4$", r"$16$", r"$2$"],
    r"Divide by $16$: $\dfrac{x^2}4+\dfrac{y^2}{16}=1$. Then $a^2=16$, $a=4$, major axis $2a=8$ (along the $y$-axis).",
    N(2 * sp.sqrt(16)))

B.q("m-con-15", "conics", 2,
    r"The focus of the parabola $y=2x^2$ is",
    [r"$\left(0,\dfrac18\right)$", r"$\left(\dfrac12,0\right)$", r"$\left(0,\dfrac12\right)$", r"$\left(0,1\right)$"],
    r"First rewrite in standard form: $x^2=\dfrac12y$, so $2p=\dfrac12$, $\dfrac p2=\dfrac18$. Focus $\left(0,\dfrac18\right)$. (Reading $y=2x^2$ as if it were $y^2=2x$ is a common slip.)",
    Pt(0, sp.Rational(1, 2) / 4))

B.q("m-con-16", "conics", 2,
    r"The parabola with vertex at the origin and focus $(0,-2)$ is",
    [r"$x^2=-8y$", r"$x^2=8y$", r"$y^2=-8x$", r"$x^2=-4y$"],
    r"Focus on the negative $y$-axis: $x^2=-2py$ with $\dfrac p2=2$, $p=4$. So $x^2=-8y$.",
    Eqn(x ** 2 + 4 * 2 * y))

_c17 = sp.sqrt(25 - 9)
_a17 = _c17 / 2
B.q("m-con-17", "conics", 3,
    r"A hyperbola has the same foci as the ellipse $\dfrac{x^2}{25}+\dfrac{y^2}{9}=1$ and eccentricity $2$. Its equation is",
    [r"$\dfrac{x^2}{4}-\dfrac{y^2}{12}=1$", r"$\dfrac{x^2}{12}-\dfrac{y^2}{4}=1$", r"$\dfrac{x^2}{4}-\dfrac{y^2}{20}=1$", r"$\dfrac{y^2}{4}-\dfrac{x^2}{12}=1$"],
    r"Ellipse: $c^2=25-9=16$, foci $(\pm4,0)$. Hyperbola: $c=4$, $e=\dfrac ca=2\Rightarrow a=2$, $b^2=c^2-a^2=12$. Equation $\dfrac{x^2}4-\dfrac{y^2}{12}=1$.",
    Eqn(x ** 2 / _a17 ** 2 - y ** 2 / (_c17 ** 2 - _a17 ** 2) - 1))

_xs18 = sp.solve((x - 1) ** 2 - 4 * x, x)
_pts18 = [(xv, xv - 1) for xv in _xs18]
B.q("m-con-18", "conics", 3,
    r"The line $y=x-1$ passes through the focus of the parabola $y^2=4x$ and meets it at $A$ and $B$. Then $|AB|=$",
    [r"$8$", r"$6$", r"$4$", r"$4\sqrt2$"],
    r"""Substitute: $(x-1)^2=4x\Rightarrow x^2-6x+1=0$, so $x_1+x_2=6$.

For a focal chord, $|AB|=|AF|+|BF|=(x_1+1)+(x_2+1)=x_1+x_2+2=8$.""",
    N(sp.sqrt((_pts18[0][0] - _pts18[1][0]) ** 2 + (_pts18[0][1] - _pts18[1][1]) ** 2)))

B.q("m-con-19", "conics", 3,
    r"A chord of the ellipse $\dfrac{x^2}{4}+\dfrac{y^2}{2}=1$ has midpoint $\left(1,\dfrac12\right)$. The slope of the chord is",
    [r"$-1$", r"$1$", r"$-\dfrac12$", r"$-2$"],
    r"""Point-difference method: subtract $\dfrac{x_1^2}4+\dfrac{y_1^2}2=1$ and $\dfrac{x_2^2}4+\dfrac{y_2^2}2=1$:
$$\frac{(x_1+x_2)(x_1-x_2)}4+\frac{(y_1+y_2)(y_1-y_2)}2=0.$$
With $x_1+x_2=2$ and $y_1+y_2=1$: $\dfrac{2}{4}+\dfrac12k=0$, so $k=-1$.""",
    N(-sp.Integer(2) * 1 / (4 * sp.Rational(1, 2))))

B.q("m-con-20", "conics", 2,
    r"The eccentricity of the hyperbola $x^2-y^2=1$ is",
    [r"$\sqrt2$", r"$1$", r"$2$", r"$\dfrac{\sqrt2}{2}$"],
    r"$a^2=b^2=1$, $c^2=a^2+b^2=2$, so $e=\dfrac ca=\sqrt2$.",
    N(sp.sqrt(1 + 1) / 1))

_c21 = sp.sqrt(4 + 12)
B.q("m-con-21", "conics", 3,
    r"The distance from a focus of the hyperbola $\dfrac{x^2}{4}-\dfrac{y^2}{12}=1$ to an asymptote is",
    [r"$2\sqrt3$", r"$2$", r"$4$", r"$\sqrt3$"],
    r"Focus $(4,0)$, asymptote $\sqrt3x-y=0$. $d=\dfrac{|4\sqrt3|}{\sqrt{3+1}}=2\sqrt3$. In general this distance always equals $b$.",
    N(dist_pl(_c21, 0, sp.sqrt(3), -1, 0)))

B.q("m-con-22", "conics", 1,
    r"Which equation represents a hyperbola whose foci lie on the $y$-axis?",
    [r"$\dfrac{y^2}{4}-\dfrac{x^2}{9}=1$", r"$\dfrac{x^2}{4}-\dfrac{y^2}{9}=1$", r"$\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$", r"$\dfrac{y^2}{9}+\dfrac{x^2}{4}=1$"],
    r"A hyperbola has a minus sign; its foci are on the axis of the **positive** squared term. In $\dfrac{y^2}4-\dfrac{x^2}9=1$ the $y^2$ term is positive. The last two equations are ellipses.")

# ------------------------------------------------------------------ vectors
B.q("m-vec-01", "vectors", 2,
    r"Given $\vec a=(1,2)$ and $\vec b=(3,-1)$, $\vec a+2\vec b=$",
    [r"$(7,0)$", r"$(4,1)$", r"$(5,3)$", r"$(7,4)$"],
    r"$2\vec b=(6,-2)$, so $\vec a+2\vec b=(1+6,\,2-2)=(7,0)$.",
    Pt(*(vec(1, 2) + 2 * vec(3, -1))))

B.q("m-vec-02", "vectors", 1,
    r"Given $\vec a=(2,3)$ and $\vec b=(-1,4)$, $\vec a\cdot\vec b=$",
    [r"$10$", r"$14$", r"$5$", r"$(-2,12)$"],
    r"$\vec a\cdot\vec b=2\cdot(-1)+3\cdot4=10$. The dot product is a number, not a vector.",
    N(vec(2, 3).dot(vec(-1, 4))))

B.q("m-vec-03", "vectors", 1,
    r"If $\vec a=(3,-4)$, then $|\vec a|=$",
    [r"$5$", r"$1$", r"$7$", r"$25$"],
    r"$|\vec a|=\sqrt{3^2+(-4)^2}=\sqrt{25}=5$.",
    N(vec(3, -4).norm()))

B.q("m-vec-04", "vectors", 1,
    r"Given $\vec a=(1,2)$ and $\vec b=(x,4)$ with $\vec a\parallel\vec b$, then $x=$",
    [r"$2$", r"$-8$", r"$8$", r"$-2$"],
    r"Parallel: $x_1y_2-x_2y_1=0$, i.e. $1\cdot4-2x=0$, $x=2$.",
    N(sp.solve(1 * 4 - 2 * x, x)[0]))

B.q("m-vec-05", "vectors", 1,
    r"Given $\vec a=(1,2)$ and $\vec b=(x,1)$ with $\vec a\perp\vec b$, then $x=$",
    [r"$-2$", r"$2$", r"$\dfrac12$", r"$-\dfrac12$"],
    r"Perpendicular: $\vec a\cdot\vec b=x+2=0$, so $x=-2$.",
    N(sp.solve(vec(1, 2).dot(vec(x, 1)), x)[0]))

B.q("m-vec-06", "vectors", 2,
    r"$|\vec a|=2$, $|\vec b|=3$ and the angle between them is $60^\circ$. Then $\vec a\cdot\vec b=$",
    [r"$3$", r"$6$", r"$3\sqrt3$", r"$\dfrac32$"],
    r"$\vec a\cdot\vec b=|\vec a||\vec b|\cos60^\circ=2\cdot3\cdot\dfrac12=3$.",
    N(2 * 3 * sp.cos(sp.pi / 3)))

B.q("m-vec-07", "vectors", 3,
    r"$|\vec a|=1$, $|\vec b|=2$ and the angle between them is $120^\circ$. Then $|\vec a+\vec b|=$",
    [r"$\sqrt3$", r"$\sqrt7$", r"$3$", r"$1$"],
    r"$|\vec a+\vec b|^2=|\vec a|^2+2\vec a\cdot\vec b+|\vec b|^2=1+2\cdot(1\cdot2\cdot(-\tfrac12))+4=3$, so $|\vec a+\vec b|=\sqrt3$.",
    N(sp.sqrt(1 + 2 * (1 * 2 * sp.cos(2 * sp.pi / 3)) + 4)))

B.q("m-vec-08", "vectors", 2,
    r"The angle between $\vec a=(1,1)$ and $\vec b=(0,2)$ is",
    [r"$\dfrac\pi4$", r"$\dfrac\pi3$", r"$\dfrac\pi2$", r"$\dfrac{3\pi}{4}$"],
    r"$\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}=\dfrac{2}{\sqrt2\cdot2}=\dfrac{\sqrt2}2$, so $\theta=\dfrac\pi4$.",
    N(angle(vec(1, 1), vec(0, 2))))

B.q("m-vec-09", "vectors", 3,
    r"Unit vectors $\vec a$, $\vec b$ satisfy $|\vec a-\vec b|=1$. The angle between $\vec a$ and $\vec b$ is",
    [r"$\dfrac\pi3$", r"$\dfrac\pi6$", r"$\dfrac{2\pi}3$", r"$\dfrac\pi2$"],
    r"$|\vec a-\vec b|^2=1-2\vec a\cdot\vec b+1=1$, so $\vec a\cdot\vec b=\dfrac12=\cos\theta$, giving $\theta=\dfrac\pi3$.",
    N(sp.acos((1 + 1 - 1) / sp.Integer(2))))

B.q("m-vec-10", "vectors", 2,
    r"The projection (scalar) of $\vec a=(2,3)$ onto the direction of $\vec b=(1,0)$ is",
    [r"$2$", r"$3$", r"$\sqrt{13}$", r"$1$"],
    r"The scalar projection is $|\vec a|\cos\theta=\dfrac{\vec a\cdot\vec b}{|\vec b|}=\dfrac{2}{1}=2$.",
    N(vec(2, 3).dot(vec(1, 0)) / vec(1, 0).norm()))

B.q("m-vec-11", "vectors", 2,
    r"In $\triangle ABC$, $\overrightarrow{AB}=(2,1)$ and $\overrightarrow{AC}=(1,3)$. Then $\overrightarrow{BC}=$",
    [r"$(-1,2)$", r"$(1,-2)$", r"$(3,4)$", r"$(-1,-2)$"],
    r"$\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}=(1-2,\,3-1)=(-1,2)$.",
    Pt(*(vec(1, 3) - vec(2, 1))))

B.q("m-vec-12", "vectors", 1,
    r"In parallelogram $ABCD$, $\overrightarrow{AB}+\overrightarrow{AD}=$",
    [r"$\overrightarrow{AC}$", r"$\overrightarrow{BD}$", r"$\overrightarrow{DB}$", r"$\overrightarrow{CA}$"],
    r"Parallelogram rule: since $\overrightarrow{AD}=\overrightarrow{BC}$, $\overrightarrow{AB}+\overrightarrow{AD}=\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}$.")

B.q("m-vec-13", "vectors", 2,
    r"Given $\vec a=(1,m)$ and $\vec b=(2,-1)$ with $(\vec a+\vec b)\perp\vec b$, then $m=$",
    [r"$7$", r"$-7$", r"$3$", r"$-3$"],
    r"$\vec a+\vec b=(3,m-1)$. Perpendicular: $(3,m-1)\cdot(2,-1)=6-(m-1)=0$, so $m=7$.",
    N(sp.solve((vec(1, m) + vec(2, -1)).dot(vec(2, -1)), m)[0]))

B.q("m-vec-14", "vectors", 1,
    r"The unit vector in the same direction as $\vec a=(3,4)$ is",
    [r"$\left(\dfrac35,\dfrac45\right)$", r"$\left(\dfrac45,\dfrac35\right)$", r"$\left(-\dfrac35,-\dfrac45\right)$", r"$(1,1)$"],
    r"Divide by the length $|\vec a|=5$: $\dfrac{\vec a}{|\vec a|}=\left(\dfrac35,\dfrac45\right)$. The opposite vector $\left(-\tfrac35,-\tfrac45\right)$ is a unit vector too, but in the opposite direction.",
    Pt(*(vec(3, 4) / vec(3, 4).norm())))

# --------------------------------------------------------- complex numbers
B.q("m-cpx-01", "complex-numbers", 1,
    r"Simplify $(1+i)(1-i)$.",
    [r"$2$", r"$0$", r"$1-i$", r"$-2$"],
    r"$(1+i)(1-i)=1-i^2=1-(-1)=2$.",
    N((1 + I) * (1 - I), complex_i=True))

B.q("m-cpx-02", "complex-numbers", 1,
    r"Simplify the complex number $i(1+i)$.",
    [r"$-1+i$", r"$1+i$", r"$1-i$", r"$-1-i$"],
    r"$i(1+i)=i+i^2=i-1=-1+i$.",
    N(I * (1 + I), complex_i=True))

B.q("m-cpx-03", "complex-numbers", 1,
    r"The modulus of the complex number $3+4i$ is",
    [r"$5$", r"$7$", r"$25$", r"$1$"],
    r"$|a+bi|=\sqrt{a^2+b^2}=\sqrt{9+16}=5$.",
    N(sp.Abs(3 + 4 * I)))

B.q("m-cpx-04", "complex-numbers", 2,
    r"$\dfrac{2+i}{1-i}=$",
    [r"$\dfrac12+\dfrac32i$", r"$\dfrac32+\dfrac12i$", r"$\dfrac12-\dfrac32i$", r"$1+3i$"],
    r"Multiply top and bottom by the conjugate $1+i$: $\dfrac{(2+i)(1+i)}{(1-i)(1+i)}=\dfrac{2+3i+i^2}{2}=\dfrac{1+3i}{2}=\dfrac12+\dfrac32i$.",
    N(sp.simplify((2 + I) / (1 - I)), complex_i=True))

B.q("m-cpx-05", "complex-numbers", 1,
    r"The conjugate of $z=2-3i$ is",
    [r"$2+3i$", r"$-2+3i$", r"$-2-3i$", r"$3-2i$"],
    r"The conjugate keeps the real part and changes the sign of the imaginary part: $\bar z=2+3i$.",
    N(sp.conjugate(2 - 3 * I), complex_i=True))

_z6 = sp.simplify(2 / (1 + I))
B.q("m-cpx-06", "complex-numbers", 2,
    r"If $z(1+i)=2$, then $|z|=$",
    [r"$\sqrt2$", r"$2$", r"$1$", r"$2\sqrt2$"],
    r"$z=\dfrac2{1+i}=\dfrac{2(1-i)}{2}=1-i$, so $|z|=\sqrt2$. (Or directly: $|z|=\dfrac{|2|}{|1+i|}=\dfrac2{\sqrt2}=\sqrt2$.)",
    N(sp.Abs(_z6)))

_z7 = sp.simplify((1 + 2 * I) / I)
B.q("m-cpx-07", "complex-numbers", 2,
    r"In the complex plane, the point representing $z=\dfrac{1+2i}{i}$ lies in the",
    [r"Fourth quadrant", r"First quadrant", r"Second quadrant", r"Third quadrant"],
    r"$\dfrac{1+2i}{i}=\dfrac{(1+2i)(-i)}{i(-i)}=\dfrac{-i-2i^2}{1}=2-i$. The point $(2,-1)$ is in the fourth quadrant.",
    T(quadrant(_z7)))

B.q("m-cpx-08", "complex-numbers", 2,
    r"If $(a+i)(1+i)$ is a purely imaginary number ($a\in\mathbb{R}$), then $a=$",
    [r"$1$", r"$-1$", r"$0$", r"$2$"],
    r"$(a+i)(1+i)=a+ai+i+i^2=(a-1)+(a+1)i$. Purely imaginary: real part $a-1=0$ and imaginary part $a+1\ne0$. So $a=1$.",
    N([v for v in sp.solve(sp.re(sp.expand((a + I) * (1 + I))).subs(a, sp.Symbol("r", real=True)), sp.Symbol("r", real=True)) if v + 1 != 0][0]))

B.q("m-cpx-09", "complex-numbers", 1,
    r"$i^{2026}=$",
    [r"$-1$", r"$1$", r"$i$", r"$-i$"],
    r"Powers of $i$ repeat every $4$. $2026=4\times506+2$, so $i^{2026}=i^2=-1$.",
    N(I ** 2026, complex_i=True))

_xr, _yr = sp.symbols("xr yr", real=True)
_loc10 = sp.expand(((_xr - 1) ** 2 + _yr ** 2) - (_xr ** 2 + (_yr + 1) ** 2)).subs({_xr: x, _yr: y})
B.q("m-cpx-10", "complex-numbers", 3,
    r"The complex number $z=x+yi$ satisfies $|z-1|=|z+i|$. The locus of the point $(x,y)$ is the line",
    [r"$y=-x$", r"$y=x$", r"$x=1$", r"$y=-1$"],
    r"""$|z-1|$ is the distance to $(1,0)$ and $|z+i|$ the distance to $(0,-1)$, so the locus is the perpendicular bisector of these two points.

Algebraically: $(x-1)^2+y^2=x^2+(y+1)^2\Rightarrow-2x=2y$, i.e. $y=-x$.""",
    Eqn(_loc10))

B.q("m-cpx-11", "complex-numbers", 2,
    r"The real part of $\dfrac{(1+i)^2}{1-i}$ is",
    [r"$-1$", r"$1$", r"$0$", r"$2$"],
    r"$(1+i)^2=2i$, and $\dfrac{2i}{1-i}=\dfrac{2i(1+i)}{2}=i+i^2=-1+i$. Real part: $-1$.",
    N(sp.re(sp.simplify((1 + I) ** 2 / (1 - I)))))

B.q("m-cpx-12", "complex-numbers", 2,
    r"If $z=1+i$, then $z^2-2z=$",
    [r"$-2$", r"$2$", r"$-2+4i$", r"$4i$"],
    r"$z^2=(1+i)^2=2i$ and $2z=2+2i$, so $z^2-2z=2i-2-2i=-2$.",
    N(sp.expand((1 + I) ** 2 - 2 * (1 + I)), complex_i=True))

# ------------------------------------------------------------ solid geometry
B.q("m-sol-01", "solid-geometry", 1,
    r"In a space rectangular coordinate system, the distance between $A(1,2,3)$ and $B(4,6,3)$ is",
    [r"$5$", r"$7$", r"$25$", r"$\sqrt{7}$"],
    r"$|AB|=\sqrt{(4-1)^2+(6-2)^2+(3-3)^2}=\sqrt{9+16}=5$.",
    N(sp.sqrt(3 ** 2 + 4 ** 2 + 0)))

B.q("m-sol-02", "solid-geometry", 1,
    r"The midpoint of $A(2,-1,4)$ and $B(0,3,-2)$ is",
    [r"$(1,1,1)$", r"$(2,2,2)$", r"$(1,-2,3)$", r"$(-1,2,-3)$"],
    r"Average each coordinate: $\left(\dfrac{2+0}2,\dfrac{-1+3}2,\dfrac{4-2}2\right)=(1,1,1)$.",
    Pt(sp.Rational(2, 2), sp.Rational(2, 2), sp.Rational(2, 2)))

B.q("m-sol-03", "solid-geometry", 1,
    r"The surface area of a sphere of radius $2$ is",
    [r"$16\pi$", r"$\dfrac{32\pi}{3}$", r"$8\pi$", r"$4\pi$"],
    r"$S=4\pi r^2=4\pi\cdot4=16\pi$. ($\tfrac{32\pi}3$ is the volume $\tfrac43\pi r^3$.)",
    N(4 * sp.pi * 2 ** 2))

B.q("m-sol-04", "solid-geometry", 2,
    r"The volume of a cone with base radius $3$ and height $4$ is",
    [r"$12\pi$", r"$36\pi$", r"$15\pi$", r"$24\pi$"],
    r"$V=\dfrac13\pi r^2h=\dfrac13\pi\cdot9\cdot4=12\pi$. Forgetting the $\tfrac13$ gives the cylinder's volume $36\pi$.",
    N(sp.Rational(1, 3) * sp.pi * 3 ** 2 * 4))

B.q("m-sol-05", "solid-geometry", 2,
    r"The length of a space diagonal of a cube with edge $2$ is",
    [r"$2\sqrt3$", r"$2\sqrt2$", r"$4$", r"$\sqrt3$"],
    r"Space diagonal $=\sqrt{a^2+a^2+a^2}=a\sqrt3=2\sqrt3$. ($2\sqrt2$ is a face diagonal.)",
    N(sp.sqrt(3 * 2 ** 2)))

B.q("m-sol-06", "solid-geometry", 3,
    r"All eight vertices of a cube with edge $2$ lie on a sphere. The surface area of the sphere is",
    [r"$12\pi$", r"$4\sqrt3\pi$", r"$16\pi$", r"$8\pi$"],
    r"The diameter of the circumscribed sphere is the space diagonal $2\sqrt3$, so $R=\sqrt3$ and $S=4\pi R^2=12\pi$.",
    N(4 * sp.pi * (sp.sqrt(3 * 2 ** 2) / 2) ** 2))

B.q("m-sol-07", "solid-geometry", 2,
    r"The total surface area of a cylinder with base radius $1$ and height $2$ is",
    [r"$6\pi$", r"$4\pi$", r"$2\pi$", r"$5\pi$"],
    r"Two bases $2\pi r^2=2\pi$ plus the lateral surface $2\pi rh=4\pi$: total $6\pi$.",
    N(2 * sp.pi * 1 ** 2 + 2 * sp.pi * 1 * 2))

_edge = 2
_h8 = sp.sqrt(_edge ** 2 - (_edge / sp.sqrt(3)) ** 2)
B.q("m-sol-08", "solid-geometry", 3,
    r"The volume of a regular tetrahedron with edge length $2$ is",
    [r"$\dfrac{2\sqrt2}{3}$", r"$\dfrac{\sqrt2}{3}$", r"$\dfrac{8}{3}$", r"$2\sqrt3$"],
    r"""Base: equilateral triangle, area $\dfrac{\sqrt3}4\cdot4=\sqrt3$. The foot of the height is the centroid, at distance $\dfrac{2}{\sqrt3}$ from each vertex, so $h=\sqrt{4-\dfrac43}=\dfrac{2\sqrt6}3$.
$$V=\frac13\cdot\sqrt3\cdot\frac{2\sqrt6}3=\frac{2\sqrt{18}}9=\frac{2\sqrt2}3.$$""",
    N(sp.Rational(1, 3) * sp.sqrt(3) / 4 * _edge ** 2 * _h8))

B.q("m-sol-09", "solid-geometry", 2,
    r"A cone has slant height $5$ and base radius $3$. Its lateral surface area is",
    [r"$15\pi$", r"$24\pi$", r"$12\pi$", r"$30\pi$"],
    r"Lateral area $=\pi rl=\pi\cdot3\cdot5=15\pi$. (Adding the base, $9\pi$, gives the total $24\pi$.)",
    N(sp.pi * 3 * 5))

B.q("m-sol-10", "solid-geometry", 2,
    r"The point symmetric to $P(1,2,3)$ with respect to the plane $xOy$ is",
    [r"$(1,2,-3)$", r"$(-1,-2,3)$", r"$(-1,-2,-3)$", r"$(-1,2,3)$"],
    r"Reflection in the $xOy$ plane keeps $x$ and $y$ and changes the sign of $z$: $(1,2,-3)$.",
    Pt(1, 2, -3))

B.q("m-sol-11", "solid-geometry", 2,
    r"The distance from the point $(2,-3,1)$ to the $z$-axis is",
    [r"$\sqrt{13}$", r"$\sqrt{14}$", r"$1$", r"$\sqrt{5}$"],
    r"The nearest point on the $z$-axis is $(0,0,1)$, so the distance is $\sqrt{2^2+(-3)^2}=\sqrt{13}$. Only $x$ and $y$ matter.",
    N(sp.sqrt(2 ** 2 + 3 ** 2)))

B.q("m-sol-12", "solid-geometry", 1,
    r"A rectangular box measures $3\times4\times12$. The length of its diagonal is",
    [r"$13$", r"$19$", r"$5$", r"$\sqrt{153}$"],
    r"$d=\sqrt{3^2+4^2+12^2}=\sqrt{169}=13$.",
    N(sp.sqrt(9 + 16 + 144)))

B.q("m-sol-13", "solid-geometry", 1,
    r"Which statement is correct ($a,b$ are lines, $\alpha$ is a plane)?",
    [r"If $a\perp\alpha$ and $b\perp\alpha$, then $a\parallel b$", r"If $a\parallel\alpha$ and $b\parallel\alpha$, then $a\parallel b$", r"If $a\perp b$ and $b\perp\alpha$, then $a\perp\alpha$", r"If $a\parallel\alpha$ and $b\subset\alpha$, then $a\parallel b$"],
    r"""Two lines perpendicular to the same plane are parallel — a basic theorem.

The others fail: two lines parallel to a plane can intersect or be skew; if $a\perp b$ and $b\perp\alpha$ then $a$ is parallel to (or lies in) $\alpha$; a line parallel to a plane can be skew to a line in the plane.""")

_diag14 = sp.sqrt(1 + 1 + 2)
B.q("m-sol-14", "solid-geometry", 3,
    r"All vertices of a rectangular box with edges $1$, $1$ and $\sqrt2$ lie on a sphere. The volume of the sphere is",
    [r"$\dfrac{4\pi}{3}$", r"$4\pi$", r"$\dfrac{32\pi}{3}$", r"$\dfrac{\sqrt2\pi}{3}$"],
    r"The sphere's diameter is the box diagonal $\sqrt{1+1+2}=2$, so $R=1$ and $V=\dfrac43\pi R^3=\dfrac{4\pi}3$.",
    N(sp.Rational(4, 3) * sp.pi * (_diag14 / 2) ** 3))
