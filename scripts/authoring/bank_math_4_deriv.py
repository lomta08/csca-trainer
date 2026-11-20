from qb import *  # noqa: F403

B = Bank("math", "functions")
R_ = sp.S.Reals


def tangent(f, x0):
    k_ = sp.diff(f, x).subs(x, x0)
    return y - (k_ * (x - x0) + f.subs(x, x0))


def increasing_set(f):
    return sp.solveset(sp.diff(f, x) > 0, x, R_)


B.q("m-der-01", "derivatives", 1,
    r"If $f(x)=x^3$, then $f'(2)=$",
    [r"$12$", r"$8$", r"$6$", r"$4$"],
    r"$f'(x)=3x^2$, so $f'(2)=3\cdot4=12$. ($8=f(2)$ is the function value, not the derivative.)",
    N(sp.diff(x ** 3, x).subs(x, 2)))

B.q("m-der-02", "derivatives", 1,
    r"The derivative of $y=x^2+\sin x$ is",
    [r"$y'=2x+\cos x$", r"$y'=2x-\cos x$", r"$y'=x+\cos x$", r"$y'=2x+\sin x$"],
    r"$(x^2)'=2x$ and $(\sin x)'=\cos x$, so $y'=2x+\cos x$.",
    Expr(sp.diff(x ** 2 + sp.sin(x), x)))

B.q("m-der-03", "derivatives", 2,
    r"If $f(x)=xe^x$, then $f'(0)=$",
    [r"$1$", r"$0$", r"$e$", r"$2$"],
    r"Product rule: $f'(x)=e^x+xe^x=(x+1)e^x$, so $f'(0)=1$.",
    N(sp.diff(x * sp.exp(x), x).subs(x, 0)))

B.q("m-der-04", "derivatives", 1,
    r"If $y=\ln x$, then the value of $y'$ at $x=2$ is",
    [r"$\dfrac12$", r"$\ln2$", r"$2$", r"$-\dfrac12$"],
    r"$(\ln x)'=\dfrac1x$, so at $x=2$ the derivative is $\dfrac12$.",
    N(sp.diff(sp.log(x), x).subs(x, 2)))

B.q("m-der-05", "derivatives", 2,
    r"The tangent line to $y=x^2$ at the point $(1,1)$ is",
    [r"$y=2x-1$", r"$y=2x+1$", r"$y=x$", r"$y=2x$"],
    r"Slope $k=y'(1)=2\cdot1=2$. Point-slope: $y-1=2(x-1)$, i.e. $y=2x-1$.",
    Eqn(tangent(x ** 2, 1)))

B.q("m-der-06", "derivatives", 2,
    r"The tangent line to $y=e^x$ at $x=0$ is",
    [r"$y=x+1$", r"$y=x$", r"$y=ex$", r"$y=x-1$"],
    r"At $x=0$: $y=e^0=1$ and slope $y'=e^0=1$. So $y-1=1\cdot(x-0)$, i.e. $y=x+1$.",
    Eqn(tangent(sp.exp(x), 0)))

B.q("m-der-07", "derivatives", 2,
    r"The increasing intervals of $f(x)=x^3-3x$ are",
    [r"$(-\infty,-1)$ and $(1,+\infty)$", r"$(-1,1)$", r"$(-\infty,-1)$ only", r"$(1,+\infty)$ only"],
    r"$f'(x)=3x^2-3=3(x+1)(x-1)>0\iff x<-1$ or $x>1$. So $f$ increases on $(-\infty,-1)$ and on $(1,+\infty)$ (and decreases on $(-1,1)$).",
    S(increasing_set(x ** 3 - 3 * x)))

_c8 = [r for r in sp.solve(sp.diff(x ** 3 - 3 * x, x), x) if sp.diff(x ** 3 - 3 * x, x, 2).subs(x, r) < 0][0]
B.q("m-der-08", "derivatives", 2,
    r"The local maximum value of $f(x)=x^3-3x$ is",
    [r"$2$", r"$-2$", r"$-1$", r"$0$"],
    r"$f'(x)=3(x+1)(x-1)$: $f'$ changes from $+$ to $-$ at $x=-1$, so there is a local maximum there, with value $f(-1)=-1+3=2$. ($x=-1$ is where it happens, not the value.)",
    N((x ** 3 - 3 * x).subs(x, _c8)))

_f9 = x ** 3 - 3 * x
_cands9 = [v for v in sp.solve(sp.diff(_f9, x), x) if 0 <= v <= 2] + [0, 2]
B.q("m-der-09", "derivatives", 3,
    r"The maximum value of $f(x)=x^3-3x$ on $[0,2]$ is",
    [r"$2$", r"$0$", r"$-2$", r"$14$"],
    r"Critical point in $[0,2]$: $x=1$, with $f(1)=-2$ (a minimum). Endpoints: $f(0)=0$, $f(2)=8-6=2$. The largest is $2$. On a closed interval always compare critical values **and** endpoints.",
    N(max(_f9.subs(x, v) for v in _cands9)))

_h = sp.Symbol("h")
B.q("m-der-10", "derivatives", 2,
    r"For $f(x)=x^2+x$, $\displaystyle\lim_{\Delta x\to0}\frac{f(1+\Delta x)-f(1)}{\Delta x}=$",
    [r"$3$", r"$2$", r"$1$", r"$0$"],
    r"By definition this limit is $f'(1)$. $f'(x)=2x+1$, so $f'(1)=3$.",
    N(sp.limit(((1 + _h) ** 2 + (1 + _h) - 2) / _h, _h, 0)))

B.q("m-der-11", "derivatives", 3,
    r"If $f'(2)=3$, then $\displaystyle\lim_{h\to0}\frac{f(2+2h)-f(2)}{h}=$",
    [r"$6$", r"$3$", r"$\dfrac32$", r"$12$"],
    r"$$\lim_{h\to0}\frac{f(2+2h)-f(2)}{h}=2\lim_{h\to0}\frac{f(2+2h)-f(2)}{2h}=2f'(2)=6.$$ The increment in $x$ is $2h$, so we must divide by $2h$ to get the derivative.",
    N(sp.limit((3 * (2 * _h) + 7 * (2 * _h) ** 2) / _h, _h, 0)))

B.q("m-der-12", "derivatives", 2,
    r"The derivative of $y=x\ln x$ is",
    [r"$y'=\ln x+1$", r"$y'=\ln x$", r"$y'=\dfrac1x$", r"$y'=x+\ln x$"],
    r"Product rule: $(x)'\ln x+x(\ln x)'=\ln x+x\cdot\dfrac1x=\ln x+1$.",
    Expr(sp.diff(x * sp.log(x), x)))

B.q("m-der-13", "derivatives", 2,
    r"The derivative of $y=\sin2x$ is",
    [r"$y'=2\cos(2x)$", r"$y'=\cos(2x)$", r"$y'=-2\cos(2x)$", r"$y'=2\sin(2x)$"],
    r"Chain rule: $(\sin u)'=\cos u\cdot u'$ with $u=2x$, $u'=2$. So $y'=2\cos2x$.",
    Expr(sp.diff(sp.sin(2 * x), x)))

B.q("m-der-14", "derivatives", 3,
    r"$f(x)=x^3+ax^2+3x-9$ has an extremum at $x=-3$. Then $a=$",
    [r"$5$", r"$-5$", r"$3$", r"$4$"],
    r"""An extremum of a differentiable function requires $f'(-3)=0$: $f'(x)=3x^2+2ax+3$, so $27-6a+3=0$, $a=5$.

Check: $f'(x)=3x^2+10x+3=(3x+1)(x+3)$ really changes sign at $x=-3$ ✔.""",
    N(sp.solve(sp.diff(x ** 3 + a * x ** 2 + 3 * x - 9, x).subs(x, -3), a)[0]))

B.q("m-der-15", "derivatives", 3,
    r"The number of zeros of $f(x)=x^3-3x+1$ is",
    [r"$3$", r"$1$", r"$2$", r"$0$"],
    r"$f'(x)=3(x^2-1)$. Local maximum $f(-1)=3>0$, local minimum $f(1)=-1<0$. With $f\to-\infty$ on the left and $+\infty$ on the right, the graph crosses the $x$-axis once in each of $(-\infty,-1)$, $(-1,1)$ and $(1,+\infty)$: $3$ zeros.",
    N(len(sp.real_roots(sp.Poly(x ** 3 - 3 * x + 1, x)))))

B.q("m-der-16", "derivatives", 2,
    r"The minimum value of $f(x)=x-\ln x$ is",
    [r"$1$", r"$0$", r"$e-1$", r"$-1$"],
    r"Domain $x>0$. $f'(x)=1-\dfrac1x$: negative on $(0,1)$, positive on $(1,+\infty)$. So the minimum is $f(1)=1-0=1$.",
    N((x - sp.log(x)).subs(x, sp.solve(sp.diff(x - sp.log(x), x), x)[0])))

B.q("m-der-17", "derivatives", 1,
    r"$\displaystyle\int_0^1x^2\,dx=$",
    [r"$\dfrac13$", r"$\dfrac12$", r"$1$", r"$2$"],
    r"An antiderivative of $x^2$ is $\dfrac{x^3}3$, so the integral is $\dfrac13-0=\dfrac13$.",
    N(sp.integrate(x ** 2, (x, 0, 1))))

B.q("m-der-18", "derivatives", 2,
    r"$\displaystyle\int_0^{\pi}\sin x\,dx=$",
    [r"$2$", r"$0$", r"$1$", r"$-2$"],
    r"$\displaystyle\int_0^\pi\sin x\,dx=[-\cos x]_0^\pi=-\cos\pi+\cos0=1+1=2$.",
    N(sp.integrate(sp.sin(x), (x, 0, sp.pi))))

B.q("m-der-19", "derivatives", 2,
    r"The area of the region enclosed by $y=x^2$ and $y=x$ is",
    [r"$\dfrac16$", r"$\dfrac13$", r"$\dfrac12$", r"$\dfrac56$"],
    r"The curves meet at $x=0$ and $x=1$; on $(0,1)$ the line is above the parabola. Area $=\displaystyle\int_0^1(x-x^2)\,dx=\frac12-\frac13=\frac16$.",
    N(sp.integrate(x - x ** 2, (x, 0, 1))))

B.q("m-der-20", "derivatives", 3,
    r"$f(x)=e^x-ax$ is increasing on $\mathbb{R}$. The range of $a$ is",
    [r"$(-\infty,0]$", r"$(-\infty,1]$", r"$(0,+\infty)$", r"$(-\infty,0)$"],
    r"""We need $f'(x)=e^x-a\ge0$ for all $x$, i.e. $a\le e^x$ for every $x$.

$e^x$ takes every positive value but never $0$ (its infimum is $0$), so $a\le0$. For $a=0$, $f'=e^x>0$ ✔. Answer: $(-\infty,0]$.""",
    S(sp.Interval(-sp.oo, sp.limit(sp.exp(x), x, -sp.oo))))

B.q("m-der-21", "derivatives", 2,
    r"An object moves so that its displacement is $s(t)=t^3-2t$ (metres, $t$ in seconds). Its instantaneous velocity at $t=2$ s is",
    [r"$10$ m/s", r"$4$ m/s", r"$12$ m/s", r"$8$ m/s"],
    r"Velocity is the derivative of displacement: $v(t)=s'(t)=3t^2-2$, so $v(2)=12-2=10$ m/s.",
    N(sp.diff(t ** 3 - 2 * t, t).subs(t, 2)))

B.q("m-der-22", "derivatives", 1,
    r"The slope of the tangent to $y=\dfrac1x$ at $x=2$ is",
    [r"$-\dfrac14$", r"$\dfrac14$", r"$-\dfrac12$", r"$\dfrac12$"],
    r"$y'=-\dfrac1{x^2}$, so the slope at $x=2$ is $-\dfrac14$.",
    N(sp.diff(1 / x, x).subs(x, 2)))
