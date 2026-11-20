from qb import *  # noqa: F403

B = Bank("math", "functions")
rad = lambda d: sp.pi * d / 180  # noqa: E731


def seq_terms(a1, rule, count):
    out = [sp.nsimplify(a1)]
    for i in range(1, count):
        out.append(rule(out[-1], i))  # i = index of previous term (1-based)
    return out


# ------------------------------------------------------------ trigonometry
B.q("m-trig-01", "trigonometry", 1,
    r"$\sin 210^\circ=$",
    [r"$-\dfrac12$", r"$\dfrac12$", r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$"],
    r"$210^\circ=180^\circ+30^\circ$ lies in the third quadrant, where sine is negative: $\sin210^\circ=-\sin30^\circ=-\dfrac12$.",
    N(sp.sin(rad(210))))

B.q("m-trig-02", "trigonometry", 1,
    r"$\cos\dfrac{2\pi}{3}=$",
    [r"$-\dfrac12$", r"$\dfrac12$", r"$-\dfrac{\sqrt3}{2}$", r"$\dfrac{\sqrt3}{2}$"],
    r"$\dfrac{2\pi}3=\pi-\dfrac\pi3$ is in the second quadrant (cosine negative): $\cos\dfrac{2\pi}3=-\cos\dfrac\pi3=-\dfrac12$.",
    N(sp.cos(2 * sp.pi / 3)))

B.q("m-trig-03", "trigonometry", 1,
    r"$\tan\left(-\dfrac{\pi}{4}\right)=$",
    [r"$-1$", r"$1$", r"$-\dfrac{\sqrt2}{2}$", r"$\sqrt3$"],
    r"Tangent is odd: $\tan(-\theta)=-\tan\theta$, so $\tan\left(-\dfrac\pi4\right)=-1$.",
    N(sp.tan(-sp.pi / 4)))

B.q("m-trig-04", "trigonometry", 1,
    r"$150^\circ$ expressed in radians is",
    [r"$\dfrac{5\pi}{6}$", r"$\dfrac{3\pi}{4}$", r"$\dfrac{2\pi}{3}$", r"$\dfrac{5\pi}{3}$"],
    r"Multiply by $\dfrac{\pi}{180^\circ}$: $150\times\dfrac{\pi}{180}=\dfrac{5\pi}6$.",
    N(rad(150)))

_c5 = -sp.sqrt(1 - sp.Rational(3, 5) ** 2)
B.q("m-trig-05", "trigonometry", 2,
    r"If $\sin\alpha=\dfrac35$ and $\alpha\in\left(\dfrac\pi2,\pi\right)$, then $\cos\alpha=$",
    [r"$-\dfrac45$", r"$\dfrac45$", r"$-\dfrac34$", r"$\dfrac34$"],
    r"$\cos^2\alpha=1-\sin^2\alpha=\dfrac{16}{25}$, so $\cos\alpha=\pm\dfrac45$. In the second quadrant cosine is negative: $\cos\alpha=-\dfrac45$.",
    N(_c5))

_al6 = sp.atan(2)
B.q("m-trig-06", "trigonometry", 2,
    r"If $\tan\alpha=2$, then $\dfrac{\sin\alpha+\cos\alpha}{\sin\alpha-\cos\alpha}=$",
    [r"$3$", r"$-3$", r"$\dfrac13$", r"$1$"],
    r"Divide numerator and denominator by $\cos\alpha$: $\dfrac{\tan\alpha+1}{\tan\alpha-1}=\dfrac{2+1}{2-1}=3$.",
    N(sp.nsimplify(sp.N((sp.sin(_al6) + sp.cos(_al6)) / (sp.sin(_al6) - sp.cos(_al6)), 30))))

_al7 = sp.atan(3)
B.q("m-trig-07", "trigonometry", 3,
    r"If $\tan\alpha=3$, then $\sin\alpha\cos\alpha=$",
    [r"$\dfrac{3}{10}$", r"$\dfrac{3}{5}$", r"$\dfrac{1}{3}$", r"$\dfrac{3}{4}$"],
    r"""Divide by $1=\sin^2\alpha+\cos^2\alpha$:
$$\sin\alpha\cos\alpha=\frac{\sin\alpha\cos\alpha}{\sin^2\alpha+\cos^2\alpha}=\frac{\tan\alpha}{\tan^2\alpha+1}=\frac{3}{10}.$$""",
    N(sp.nsimplify(sp.N(sp.sin(_al7) * sp.cos(_al7), 30))))

B.q("m-trig-08", "trigonometry", 1,
    r"The smallest positive period of $y=\sin\left(2x+\dfrac\pi3\right)$ is",
    [r"$\pi$", r"$2\pi$", r"$\dfrac\pi2$", r"$\dfrac{\pi}{3}$"],
    r"For $y=A\sin(\omega x+\varphi)$ the period is $T=\dfrac{2\pi}{|\omega|}=\dfrac{2\pi}{2}=\pi$. The phase $\dfrac\pi3$ does not affect the period.",
    N(sp.periodicity(sp.sin(2 * x + sp.pi / 3), x)))

B.q("m-trig-09", "trigonometry", 2,
    r"The smallest positive period of $y=|\sin x|$ is",
    [r"$\pi$", r"$2\pi$", r"$\dfrac\pi2$", r"It is not periodic"],
    r"Taking the absolute value flips the negative half-waves up, so the graph repeats every $\pi$: $|\sin(x+\pi)|=|-\sin x|=|\sin x|$, and no smaller positive shift works.")

B.q("m-trig-10", "trigonometry", 2,
    r"The maximum value of $y=\sin x+\sqrt3\cos x$ is",
    [r"$2$", r"$1+\sqrt3$", r"$\sqrt3$", r"$4$"],
    r"$\sin x+\sqrt3\cos x=2\left(\tfrac12\sin x+\tfrac{\sqrt3}2\cos x\right)=2\sin\left(x+\dfrac\pi3\right)$, whose maximum is $2$. In general the maximum of $a\sin x+b\cos x$ is $\sqrt{a^2+b^2}$.",
    N(sp.sqrt(1 + 3)))

B.q("m-trig-11", "trigonometry", 2,
    r"The maximum value of $y=3\sin x+4\cos x$ is",
    [r"$5$", r"$7$", r"$4$", r"$1$"],
    r"$a\sin x+b\cos x=\sqrt{a^2+b^2}\,\sin(x+\varphi)$, so the maximum is $\sqrt{9+16}=5$. (Adding $3+4$ is wrong: $\sin x$ and $\cos x$ cannot both equal $1$.)",
    N(sp.sqrt(3 ** 2 + 4 ** 2)))

B.q("m-trig-12", "trigonometry", 2,
    r"$\sin15^\circ\cos15^\circ=$",
    [r"$\dfrac14$", r"$\dfrac12$", r"$\dfrac{\sqrt3}{4}$", r"$\dfrac{\sqrt3}{2}$"],
    r"Double-angle formula: $\sin15^\circ\cos15^\circ=\dfrac12\sin30^\circ=\dfrac12\cdot\dfrac12=\dfrac14$.",
    N(sp.nsimplify(sp.N(sp.sin(rad(15)) * sp.cos(rad(15)), 30))))

B.q("m-trig-13", "trigonometry", 2,
    r"$\cos^2\dfrac\pi8-\sin^2\dfrac\pi8=$",
    [r"$\dfrac{\sqrt2}{2}$", r"$1$", r"$\dfrac12$", r"$\dfrac{\sqrt3}{2}$"],
    r"$\cos^2\theta-\sin^2\theta=\cos2\theta$, so the value is $\cos\dfrac\pi4=\dfrac{\sqrt2}2$.",
    N(sp.cos(sp.pi / 8) ** 2 - sp.sin(sp.pi / 8) ** 2))

B.q("m-trig-14", "trigonometry", 2,
    r"$\sin75^\circ=$",
    [r"$\dfrac{\sqrt6+\sqrt2}{4}$", r"$\dfrac{\sqrt6-\sqrt2}{4}$", r"$\dfrac{\sqrt3+1}{2}$", r"$\dfrac{\sqrt2}{2}$"],
    r"""$\sin75^\circ=\sin(45^\circ+30^\circ)=\sin45^\circ\cos30^\circ+\cos45^\circ\sin30^\circ$
$$=\frac{\sqrt2}2\cdot\frac{\sqrt3}2+\frac{\sqrt2}2\cdot\frac12=\frac{\sqrt6+\sqrt2}{4}.$$""",
    N(sp.sin(rad(75))))

B.q("m-trig-15", "trigonometry", 2,
    r"If $\cos\alpha=\dfrac13$, then $\cos2\alpha=$",
    [r"$-\dfrac79$", r"$\dfrac79$", r"$\dfrac23$", r"$-\dfrac{2}{9}$"],
    r"$\cos2\alpha=2\cos^2\alpha-1=2\cdot\dfrac19-1=-\dfrac79$.",
    N(2 * sp.Rational(1, 3) ** 2 - 1))

_a16 = sp.acos(sp.Rational(4, 5))
_ab16 = sp.acos(sp.Rational(5, 13))
B.q("m-trig-16", "trigonometry", 3,
    r"$\alpha$ and $\beta$ are acute angles with $\cos\alpha=\dfrac45$ and $\cos(\alpha+\beta)=\dfrac5{13}$. Then $\sin\beta=$",
    [r"$\dfrac{33}{65}$", r"$\dfrac{63}{65}$", r"$\dfrac{16}{65}$", r"$\dfrac{56}{65}$"],
    r"""Write $\beta=(\alpha+\beta)-\alpha$. Both $\alpha$ and $\alpha+\beta$ lie in $(0,\pi)$, so their sines are positive: $\sin\alpha=\dfrac35$, $\sin(\alpha+\beta)=\dfrac{12}{13}$.
$$\sin\beta=\sin(\alpha+\beta)\cos\alpha-\cos(\alpha+\beta)\sin\alpha=\frac{12}{13}\cdot\frac45-\frac5{13}\cdot\frac35=\frac{48-15}{65}=\frac{33}{65}.$$""",
    N(sp.nsimplify(sp.N(sp.sin(_ab16 - _a16), 30))))

B.q("m-trig-17", "trigonometry", 3,
    r"To obtain the graph of $y=\sin\left(2x-\dfrac\pi3\right)$ from the graph of $y=\sin2x$, shift it",
    [r"right by $\dfrac\pi6$", r"right by $\dfrac\pi3$", r"left by $\dfrac\pi6$", r"left by $\dfrac\pi3$"],
    r"""Factor out the coefficient of $x$: $\sin\left(2x-\dfrac\pi3\right)=\sin\left[2\left(x-\dfrac\pi6\right)\right]$.

Replacing $x$ by $x-\dfrac\pi6$ shifts the graph **right** by $\dfrac\pi6$. (Shifting by $\dfrac\pi3$ forgets to divide by $\omega=2$.)""")

B.q("m-trig-18", "trigonometry", 2,
    r"In $\triangle ABC$, $a=3$, $b=4$ and $C=60^\circ$. Then $c=$",
    [r"$\sqrt{13}$", r"$5$", r"$\sqrt{37}$", r"$\sqrt{7}$"],
    r"Law of cosines: $c^2=a^2+b^2-2ab\cos C=9+16-2\cdot3\cdot4\cdot\dfrac12=13$, so $c=\sqrt{13}$.",
    N(sp.sqrt(3 ** 2 + 4 ** 2 - 2 * 3 * 4 * sp.cos(rad(60)))))

B.q("m-trig-19", "trigonometry", 3,
    r"In $\triangle ABC$, $A=30^\circ$, $a=2$ and $b=2\sqrt3$. Then $B=$",
    [r"$60^\circ$ or $120^\circ$", r"$60^\circ$", r"$120^\circ$", r"$30^\circ$"],
    r"""Law of sines: $\sin B=\dfrac{b\sin A}{a}=\dfrac{2\sqrt3\cdot\frac12}{2}=\dfrac{\sqrt3}2$, so $B=60^\circ$ or $120^\circ$.

Both are possible because $b>a$ means $B>A$, and both $60^\circ$ and $120^\circ$ exceed $30^\circ$ while leaving room for $C$ ($A+B<180^\circ$).""")

B.q("m-trig-20", "trigonometry", 2,
    r"In $\triangle ABC$, $a=2$, $b=3$ and $C=30^\circ$. The area of the triangle is",
    [r"$\dfrac32$", r"$3$", r"$\dfrac{3\sqrt3}{2}$", r"$6$"],
    r"$S=\dfrac12ab\sin C=\dfrac12\cdot2\cdot3\cdot\dfrac12=\dfrac32$.",
    N(sp.Rational(1, 2) * 2 * 3 * sp.sin(rad(30))))

# f = sin^2 x + sqrt3 sin x cos x = 1/2 - cos2x/2 + (sqrt3/2) sin 2x
_A21, _B21, _C21 = sp.sqrt(3) / 2, -sp.Rational(1, 2), sp.Rational(1, 2)
assert sp.simplify(sp.sin(x) ** 2 + sp.sqrt(3) * sp.sin(x) * sp.cos(x) - (_A21 * sp.sin(2 * x) + _B21 * sp.cos(2 * x) + _C21)) == 0
B.q("m-trig-21", "trigonometry", 3,
    r"The maximum value of $f(x)=\sin^2x+\sqrt3\sin x\cos x$ is",
    [r"$\dfrac32$", r"$1+\sqrt3$", r"$2$", r"$\dfrac{1+\sqrt3}{2}$"],
    r"""Use $\sin^2x=\dfrac{1-\cos2x}2$ and $\sin x\cos x=\dfrac{\sin2x}2$:
$$f(x)=\frac{\sqrt3}2\sin2x-\frac12\cos2x+\frac12=\sin\left(2x-\frac\pi6\right)+\frac12.$$
Maximum: $1+\dfrac12=\dfrac32$.""",
    N(sp.sqrt(_A21 ** 2 + _B21 ** 2) + _C21))

B.q("m-trig-22", "trigonometry", 2,
    r"If $\sin\alpha+\cos\alpha=\dfrac12$, then $\sin\alpha\cos\alpha=$",
    [r"$-\dfrac38$", r"$\dfrac38$", r"$-\dfrac34$", r"$\dfrac14$"],
    r"Square both sides: $1+2\sin\alpha\cos\alpha=\dfrac14$, so $\sin\alpha\cos\alpha=\dfrac{\frac14-1}{2}=-\dfrac38$.",
    N((sp.Rational(1, 4) - 1) / 2))

# ------------------------------------------------------------- sequences
B.q("m-seq-01", "sequences", 1,
    r"An arithmetic sequence has $a_1=2$ and common difference $d=3$. Then $a_{10}=$",
    [r"$29$", r"$32$", r"$30$", r"$27$"],
    r"$a_n=a_1+(n-1)d$, so $a_{10}=2+9\cdot3=29$. (Using $10d$ instead of $9d$ gives $32$.)",
    N(seq_terms(2, lambda p, i: p + 3, 10)[-1]))

B.q("m-seq-02", "sequences", 1,
    r"A geometric sequence has $a_1=3$ and common ratio $q=2$. Then $a_5=$",
    [r"$48$", r"$96$", r"$30$", r"$24$"],
    r"$a_n=a_1q^{n-1}$, so $a_5=3\cdot2^4=48$.",
    N(seq_terms(3, lambda p, i: p * 2, 5)[-1]))

_d3 = sp.Rational(13 - 5, 7 - 3)
_a13 = 5 - 2 * _d3
B.q("m-seq-03", "sequences", 2,
    r"In an arithmetic sequence, $a_3=5$ and $a_7=13$. The sum of the first $10$ terms, $S_{10}$, is",
    [r"$100$", r"$120$", r"$90$", r"$110$"],
    r"""$d=\dfrac{a_7-a_3}{7-3}=\dfrac84=2$, $a_1=a_3-2d=1$.

$S_{10}=10a_1+\dfrac{10\cdot9}{2}d=10+90=100$.""",
    N(sum(seq_terms(_a13, lambda p, i: p + _d3, 10))))

B.q("m-seq-04", "sequences", 2,
    r"In an arithmetic sequence, $a_2+a_8=10$. Then $S_9=$",
    [r"$45$", r"$90$", r"$50$", r"$40$"],
    r"Since $2+8=1+9$, $a_1+a_9=a_2+a_8=10$. So $S_9=\dfrac{9(a_1+a_9)}{2}=\dfrac{9\cdot10}{2}=45$.",
    N(sp.Rational(9, 2) * 10))

_q5 = [r for r in sp.solve(6 * t ** 2 - 24, t) if r > 0][0]
B.q("m-seq-05", "sequences", 2,
    r"In a geometric sequence with positive ratio, $a_2=6$ and $a_4=24$. The sum of the first $5$ terms is",
    [r"$93$", r"$96$", r"$186$", r"$45$"],
    r"$q^2=\dfrac{a_4}{a_2}=4$ and $q>0$, so $q=2$ and $a_1=3$. $S_5=\dfrac{3(2^5-1)}{2-1}=93$.",
    N(sum(seq_terms(6 / _q5, lambda p, i: p * _q5, 5))))

B.q("m-seq-06", "sequences", 1,
    r"If $a_n=2n-1$, then the sum of the first $n$ terms is $S_n=$",
    [r"$n^2$", r"$n^2+1$", r"$2n^2-n$", r"$n(n+1)$"],
    r"This is arithmetic with $a_1=1$, $d=2$: $S_n=\dfrac{n(a_1+a_n)}{2}=\dfrac{n(1+2n-1)}2=n^2$. (The sum of the first $n$ odd numbers is $n^2$.)",
    Expr(sp.summation(2 * k - 1, (k, 1, n))))

_S7 = n ** 2 + 2 * n
B.q("m-seq-07", "sequences", 3,
    r"The sum of the first $n$ terms of a sequence is $S_n=n^2+2n$. Then $a_n=$",
    [r"$2n+1$", r"$2n-1$", r"$2n+3$", r"$n^2+2n$"],
    r"""For $n\ge2$: $a_n=S_n-S_{n-1}=n^2+2n-[(n-1)^2+2(n-1)]=2n+1$.

Check $n=1$: $a_1=S_1=3=2\cdot1+1$ ✔, so $a_n=2n+1$ for all $n$.""",
    Expr(sp.expand(_S7 - _S7.subs(n, n - 1))) if sp.expand(_S7 - _S7.subs(n, n - 1)).subs(n, 1) == _S7.subs(n, 1) else Expr(0))

_S8 = 2 ** n - 1
B.q("m-seq-08", "sequences", 2,
    r"The sum of the first $n$ terms of a sequence is $S_n=2^n-1$. Then $a_n=$",
    [r"$2^{n-1}$", r"$2^n$", r"$2^n-1$", r"$2^{n+1}-1$"],
    r"For $n\ge2$: $a_n=S_n-S_{n-1}=2^n-2^{n-1}=2^{n-1}$. For $n=1$: $a_1=S_1=1=2^0$ ✔. So $a_n=2^{n-1}$.",
    Expr(sp.simplify(_S8 - _S8.subs(n, n - 1))))

B.q("m-seq-09", "sequences", 3,
    r"The sum of the first $n$ terms of a sequence is $S_n=n^2+n+1$. Then $a_n=$",
    [r"$a_n=\begin{cases}3,&n=1\\2n,&n\ge2\end{cases}$", r"$a_n=2n$", r"$a_n=2n+1$", r"$a_n=n^2+n+1$"],
    r"""For $n\ge2$: $a_n=S_n-S_{n-1}=(n^2+n+1)-[(n-1)^2+(n-1)+1]=2n$.

But $a_1=S_1=3\ne2\cdot1$. So the formula must be written in two pieces. **Always check $n=1$ separately.**""")

B.q("m-seq-10", "sequences", 2,
    r"A sequence has $a_1=1$ and $a_{n+1}=a_n+2n$. Then $a_5=$",
    [r"$21$", r"$31$", r"$11$", r"$25$"],
    r"$a_2=1+2=3$, $a_3=3+4=7$, $a_4=7+6=13$, $a_5=13+8=21$. (In general $a_n=1+2[1+2+\dots+(n-1)]=n^2-n+1$.)",
    N(seq_terms(1, lambda p, i: p + 2 * i, 5)[-1]))

B.q("m-seq-11", "sequences", 2,
    r"A sequence has $a_1=1$ and $a_{n+1}=2a_n+1$. Then $a_6=$",
    [r"$63$", r"$31$", r"$64$", r"$127$"],
    r"""$a_{n+1}+1=2(a_n+1)$, so $\{a_n+1\}$ is geometric with first term $2$ and ratio $2$: $a_n+1=2^n$, $a_n=2^n-1$.

$a_6=2^6-1=63$.""",
    N(seq_terms(1, lambda p, i: 2 * p + 1, 6)[-1]))

B.q("m-seq-12", "sequences", 2,
    r"In a geometric sequence of positive terms, $a_3a_7=16$. Then $a_5=$",
    [r"$4$", r"$8$", r"$\pm4$", r"$2$"],
    r"Since $3+7=5+5$, $a_3a_7=a_5^2=16$. The terms are positive, so $a_5=4$.",
    N(sp.sqrt(16)))

B.q("m-seq-13", "sequences", 2,
    r"In the arithmetic sequence $5,8,11,\dots$, the number $101$ is which term?",
    [r"$33$", r"$32$", r"$34$", r"$31$"],
    r"$a_n=5+3(n-1)=3n+2$. Solve $3n+2=101$: $n=33$.",
    N(sp.solve(5 + 3 * (n - 1) - 101, n)[0]))

_terms14 = seq_terms(20, lambda p, i: p - 3, 20)
B.q("m-seq-14", "sequences", 3,
    r"An arithmetic sequence has $a_1=20$ and $d=-3$. The maximum value of $S_n$ is",
    [r"$77$", r"$70$", r"$74$", r"$81$"],
    r"""$S_n$ is largest when we add all the positive terms and stop before the negative ones.

$a_n=23-3n>0\iff n<\tfrac{23}3$, so $a_7=2>0$ and $a_8=-1<0$. Maximum: $S_7=\dfrac{7(20+2)}{2}=77$.""",
    N(max(sum(_terms14[:j]) for j in range(1, 21))))

B.q("m-seq-15", "sequences", 3,
    r"$\dfrac1{1\times2}+\dfrac1{2\times3}+\dfrac1{3\times4}+\dots+\dfrac1{99\times100}=$",
    [r"$\dfrac{99}{100}$", r"$\dfrac{100}{101}$", r"$1$", r"$\dfrac{1}{100}$"],
    r"""Split each term (telescoping): $\dfrac1{k(k+1)}=\dfrac1k-\dfrac1{k+1}$. The sum becomes
$$\left(1-\tfrac12\right)+\left(\tfrac12-\tfrac13\right)+\dots+\left(\tfrac1{99}-\tfrac1{100}\right)=1-\frac1{100}=\frac{99}{100}.$$""",
    N(sum(sp.Rational(1, j * (j + 1)) for j in range(1, 100))))

B.q("m-seq-16", "sequences", 2,
    r"$1+3+3^2+3^3+3^4+3^5=$",
    [r"$364$", r"$1093$", r"$243$", r"$121$"],
    r"Geometric with $a_1=1$, $q=3$, $6$ terms: $S_6=\dfrac{3^6-1}{3-1}=\dfrac{728}2=364$.",
    N(sum(3 ** j for j in range(6))))

B.q("m-seq-17", "sequences", 2,
    r"If $2,\ x,\ 8$ form a geometric sequence and $x>0$, then $x=$",
    [r"$4$", r"$5$", r"$16$", r"$6$"],
    r"In a geometric sequence the middle term satisfies $x^2=2\cdot8=16$; with $x>0$, $x=4$. ($5$ would make it arithmetic.)",
    N([r for r in sp.solve(x ** 2 - 16, x) if r > 0][0]))

B.q("m-seq-18", "sequences", 1,
    r"Let $A$ be the arithmetic mean of $3$ and $7$, and $G$ the positive geometric mean of $4$ and $9$. Then $A+G=$",
    [r"$11$", r"$10$", r"$12$", r"$13$"],
    r"$A=\dfrac{3+7}2=5$ and $G=\sqrt{4\cdot9}=6$, so $A+G=11$.",
    N(sp.Rational(3 + 7, 2) + sp.sqrt(4 * 9)))

B.q("m-seq-19", "sequences", 3,
    r"Let $S_n=1\cdot2+2\cdot2^2+3\cdot2^3+\dots+n\cdot2^n$. Then $S_5=$",
    [r"$258$", r"$256$", r"$98$", r"$290$"],
    r"""Method (subtract a shifted copy): $S_n=(n-1)2^{n+1}+2$. Then $S_5=4\cdot64+2=258$.

Direct check: $2+8+24+64+160=258$.""",
    N(sum(j * 2 ** j for j in range(1, 6))))

B.q("m-seq-20", "sequences", 1,
    r"The 6th term of the geometric sequence $1,-2,4,\dots$ is",
    [r"$-32$", r"$32$", r"$-64$", r"$64$"],
    r"$q=-2$, so $a_6=1\cdot(-2)^5=-32$.",
    N(seq_terms(1, lambda p, i: p * -2, 6)[-1]))
