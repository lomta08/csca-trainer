from fractions import Fraction
from itertools import combinations, permutations, product
from statistics import NormalDist, mean, pstdev, pvariance, median

from qb import *  # noqa: F403

B = Bank("math", "probability-statistics")


def _pv(vals):
    mu = sum(vals) / len(vals)
    return sp.simplify(sum((v - mu) ** 2 for v in vals) / len(vals))


def P(fav, total):
    return sp.Rational(fav, total)


def count(it, pred):
    items = list(it)
    return sum(1 for v in items if pred(v)), len(items)


# ------------------------------------------------------- classical probability
B.q("m-prob-01", "classical-probability", 1,
    r"A fair die is rolled once. The probability that the number shown is greater than $4$ is",
    [r"$\dfrac13$", r"$\dfrac12$", r"$\dfrac23$", r"$\dfrac16$"],
    r"Favourable outcomes: $5,6$ — two of the six equally likely outcomes. $P=\dfrac26=\dfrac13$.",
    N(P(*count(range(1, 7), lambda v: v > 4))))

B.q("m-prob-02", "classical-probability", 1,
    r"A fair coin is tossed twice. The probability of getting at least one head is",
    [r"$\dfrac34$", r"$\dfrac12$", r"$\dfrac14$", r"$\dfrac23$"],
    r"Outcomes: HH, HT, TH, TT (equally likely). Only TT has no head, so $P=1-\dfrac14=\dfrac34$. (Listing only “0, 1 or 2 heads” as three outcomes is wrong: they are not equally likely.)",
    N(P(*count(product("HT", repeat=2), lambda v: "H" in v))))

B.q("m-prob-03", "classical-probability", 2,
    r"Two different numbers are chosen at random from $\{1,2,3,4\}$. The probability that their sum is even is",
    [r"$\dfrac13$", r"$\dfrac12$", r"$\dfrac23$", r"$\dfrac14$"],
    r"There are $C_4^2=6$ pairs. An even sum needs two odds or two evens: $\{1,3\}$ and $\{2,4\}$. $P=\dfrac26=\dfrac13$.",
    N(P(*count(combinations([1, 2, 3, 4], 2), lambda v: sum(v) % 2 == 0))))

B.q("m-prob-04", "classical-probability", 2,
    r"From $3$ boys and $2$ girls, $2$ people are chosen at random. The probability that exactly one girl is chosen is",
    [r"$\dfrac35$", r"$\dfrac25$", r"$\dfrac{3}{10}$", r"$\dfrac{1}{10}$"],
    r"Total: $C_5^2=10$. Exactly one girl: $C_2^1C_3^1=6$. $P=\dfrac6{10}=\dfrac35$.",
    N(P(*count(combinations("BBBGG", 2), lambda v: v.count("G") == 1))))

B.q("m-prob-05", "classical-probability", 1,
    r"Two fair dice are rolled. The probability that the sum of the numbers is $7$ is",
    [r"$\dfrac16$", r"$\dfrac{7}{36}$", r"$\dfrac{1}{12}$", r"$\dfrac{1}{11}$"],
    r"$36$ ordered outcomes. Sum $7$: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$ — six of them. $P=\dfrac6{36}=\dfrac16$.",
    N(P(*count(product(range(1, 7), repeat=2), lambda v: sum(v) == 7))))

B.q("m-prob-06", "classical-probability", 2,
    r"Events $A$ and $B$ are independent with $P(A)=0.5$ and $P(B)=0.4$. Then $P(A\cup B)=$",
    [r"$0.7$", r"$0.9$", r"$0.2$", r"$0.8$"],
    r"Independent: $P(AB)=0.5\times0.4=0.2$. Then $P(A\cup B)=P(A)+P(B)-P(AB)=0.9-0.2=0.7$. (Adding to get $0.9$ only works for mutually exclusive events.)",
    N(sp.Rational(1, 2) + sp.Rational(2, 5) - sp.Rational(1, 2) * sp.Rational(2, 5)))

B.q("m-prob-07", "classical-probability", 2,
    r"A fair coin is tossed $3$ times. The probability of exactly $2$ heads is",
    [r"$\dfrac38$", r"$\dfrac14$", r"$\dfrac12$", r"$\dfrac23$"],
    r"$2^3=8$ equally likely sequences. Exactly two heads: HHT, HTH, THH. $P=\dfrac38$ (or $C_3^2\left(\tfrac12\right)^3$).",
    N(P(*count(product("HT", repeat=3), lambda v: v.count("H") == 2))))

B.q("m-prob-08", "classical-probability", 3,
    r"$A$, $B$, $C$, $D$ stand in a row in random order. The probability that $A$ and $B$ are next to each other is",
    [r"$\dfrac12$", r"$\dfrac13$", r"$\dfrac14$", r"$\dfrac16$"],
    r"Total $4!=24$. Treat $AB$ as one block: $3!$ arrangements, times $2$ for the order inside the block: $12$. $P=\dfrac{12}{24}=\dfrac12$.",
    N(P(*count(permutations("ABCD"), lambda v: abs(v.index("A") - v.index("B")) == 1))))

B.q("m-prob-09", "classical-probability", 3,
    r"Three different numbers are chosen at random from $1,2,3,4,5$. The probability that they can be the side lengths of a triangle is",
    [r"$\dfrac{3}{10}$", r"$\dfrac{2}{5}$", r"$\dfrac{1}{5}$", r"$\dfrac{1}{2}$"],
    r"""$C_5^3=10$ choices. A triangle needs the two shorter sides to sum to more than the longest:
$\{2,3,4\}$, $\{2,4,5\}$, $\{3,4,5\}$ work ($\{1,\cdot,\cdot\}$ never works, and $\{2,3,5\}$ fails since $2+3=5$).

$P=\dfrac3{10}$.""",
    N(P(*count(combinations(range(1, 6), 3), lambda v: v[0] + v[1] > v[2]))))

B.q("m-prob-10", "classical-probability", 2,
    r"A shooter hits the target with probability $0.8$ on each shot, independently. In two shots, the probability of hitting at least once is",
    [r"$0.96$", r"$0.64$", r"$0.8$", r"$0.16$"],
    r"Complement: missing both times has probability $0.2\times0.2=0.04$. So $P(\text{at least one hit})=1-0.04=0.96$.",
    N(1 - sp.Rational(1, 5) ** 2))

_deck = list(product(range(13), "SHDC"))
B.q("m-prob-11", "classical-probability", 2,
    r"One card is drawn from a standard $52$-card deck. The probability that it is a heart or a king is",
    [r"$\dfrac{4}{13}$", r"$\dfrac{17}{52}$", r"$\dfrac14$", r"$\dfrac{1}{52}$"],
    r"$13$ hearts $+\ 4$ kings $-\ 1$ (the king of hearts is counted twice) $=16$. $P=\dfrac{16}{52}=\dfrac4{13}$.",
    N(P(*count(_deck, lambda c: c[1] == "H" or c[0] == 12))))

B.q("m-prob-12", "classical-probability", 2,
    r"A bag has $2$ red and $2$ white balls. Balls are drawn one at a time without replacement. The probability that the **second** ball is red is",
    [r"$\dfrac12$", r"$\dfrac13$", r"$\dfrac23$", r"$\dfrac14$"],
    r"By symmetry every position is equally likely to hold any particular ball, so $P=\dfrac24=\dfrac12$. (Directly: $\tfrac24\cdot\tfrac13+\tfrac24\cdot\tfrac23=\tfrac16+\tfrac13=\tfrac12$.)",
    N(P(*count(permutations(["R1", "R2", "W1", "W2"]), lambda v: v[1].startswith("R")))))

B.q("m-prob-13", "classical-probability", 2,
    r"Two people are chosen at random from $A,B,C,D,E$. The probability that $A$ is chosen is",
    [r"$\dfrac25$", r"$\dfrac15$", r"$\dfrac12$", r"$\dfrac{1}{10}$"],
    r"$C_5^2=10$ pairs; pairs containing $A$: $4$. $P=\dfrac4{10}=\dfrac25$.",
    N(P(*count(combinations("ABCDE", 2), lambda v: "A" in v))))

B.q("m-prob-14", "classical-probability", 3,
    r"A four-digit number is formed from the digits $1,2,3,4$, each used exactly once. The probability that it is even **and** greater than $2000$ is",
    [r"$\dfrac13$", r"$\dfrac12$", r"$\dfrac14$", r"$\dfrac38$"],
    r"""$4!=24$ numbers. The last digit must be $2$ or $4$, and the first digit at least $2$.

- Last digit $2$: first digit $3$ or $4$ (2 ways), middle two digits $2!$ ways: $4$ numbers.
- Last digit $4$: first digit $2$ or $3$: $4$ numbers.

$P=\dfrac8{24}=\dfrac13$.""",
    N(P(*count(permutations("1234"), lambda v: int("".join(v)) % 2 == 0 and int("".join(v)) > 2000))))

# ------------------------------------------------------------ mean & variance
B.q("m-stat-01", "mean-variance", 1,
    r"The mean of the data $2,4,6,8,10$ is",
    [r"$6$", r"$5$", r"$30$", r"$8$"],
    r"$\bar x=\dfrac{2+4+6+8+10}{5}=\dfrac{30}5=6$.",
    N(Fraction(sum([2, 4, 6, 8, 10]), 5)))

B.q("m-stat-02", "mean-variance", 1,
    r"The variance of the data $1,2,3,4,5$ is",
    [r"$2$", r"$\dfrac52$", r"$\sqrt2$", r"$10$"],
    r"Mean $3$; squared deviations $4,1,0,1,4$, total $10$. $s^2=\dfrac{10}5=2$. ($\tfrac52$ divides by $n-1$; CSCA uses $n$.)",
    N(pvariance([1, 2, 3, 4, 5])))

B.q("m-stat-03", "mean-variance", 2,
    r"The median of $3,7,1,9,5,8$ is",
    [r"$6$", r"$5$", r"$7$", r"$5.5$"],
    r"Sort first: $1,3,5,7,8,9$. With an even number of values, the median is the mean of the two middle ones: $\dfrac{5+7}2=6$.",
    N(median([3, 7, 1, 9, 5, 8])))

B.q("m-stat-04", "mean-variance", 2,
    r"A data set $x_1,\dots,x_n$ has mean $5$ and variance $2$. The data $3x_1+1,\dots,3x_n+1$ have",
    [r"mean $16$, variance $18$", r"mean $16$, variance $6$", r"mean $15$, variance $18$", r"mean $16$, variance $19$"],
    r"Mean: $3\cdot5+1=16$. Variance: adding $1$ does not change spread, multiplying by $3$ multiplies the variance by $3^2$: $9\cdot2=18$.",
    Nums(3 * 5 + 1, _pv([3 * v + 1 for v in (5 - sp.sqrt(2), 5 + sp.sqrt(2))])))

_x5 = sp.solve((4 + 6 + x + 8) / 4 - 6, x)[0]
B.q("m-stat-05", "mean-variance", 3,
    r"The data $4,6,x,8$ have mean $6$. Their variance is",
    [r"$2$", r"$\dfrac83$", r"$4$", r"$8$"],
    r"$\dfrac{4+6+x+8}4=6\Rightarrow x=6$. Deviations: $-2,0,0,2$. $s^2=\dfrac{4+0+0+4}4=2$.",
    N(pvariance([4, 6, int(_x5), 8])))

B.q("m-stat-06", "mean-variance", 2,
    r"The standard deviation of $2,4,4,4,5,5,7,9$ is",
    [r"$2$", r"$4$", r"$5$", r"$\sqrt2$"],
    r"Mean $=\dfrac{40}8=5$. Squared deviations: $9,1,1,1,0,0,4,16$, total $32$. Variance $=\dfrac{32}8=4$, standard deviation $=\sqrt4=2$.",
    N(pstdev([2, 4, 4, 4, 5, 5, 7, 9])))

_d7 = [2, 3, 3, 5, 7, 7, 7, 9]
B.q("m-stat-07", "mean-variance", 1,
    r"The mode of $2,3,3,5,7,7,7,9$ is",
    [r"$7$", r"$3$", r"$5$", r"$6$"],
    r"The mode is the most frequent value: $7$ appears three times.",
    N(max(set(_d7), key=_d7.count)))

B.q("m-stat-08", "mean-variance", 1,
    r"Two machines fill bags with the same mean mass. The variance for machine A is $0.4$ and for machine B is $1.2$. Which conclusion is correct?",
    [r"Machine A is more consistent", r"Machine B is more consistent", r"Both are equally consistent", r"It cannot be decided without the means"],
    r"Variance measures spread. A smaller variance means the data cluster more tightly around the mean, so machine A is more consistent (stable).")

B.q("m-stat-09", "mean-variance", 3,
    r"Ten numbers have mean $3$ and variance $2$. The number $3$ is added to the data. The variance of the $11$ numbers is",
    [r"$\dfrac{20}{11}$", r"$2$", r"$\dfrac{22}{10}$", r"$\dfrac{20}{9}$"],
    r"The sum of squared deviations is $10\times2=20$. Adding the value $3$ keeps the mean at $3$ and adds a deviation of $0$. New variance: $\dfrac{20+0}{11}=\dfrac{20}{11}$.",
    N(sp.Rational(10 * 2 + (3 - 3) ** 2, 11)))

_vals10, _freq10 = [1, 2, 3], [2, 5, 3]
B.q("m-stat-10", "mean-variance", 2,
    r"A survey records the number of books read: $1$ book ($2$ people), $2$ books ($5$ people), $3$ books ($3$ people). The mean number of books is",
    [r"$2.1$", r"$2$", r"$3.3$", r"$6.3$"],
    r"Weighted mean: $\dfrac{1\cdot2+2\cdot5+3\cdot3}{2+5+3}=\dfrac{21}{10}=2.1$. (The plain mean of $1,2,3$ ignores the frequencies.)",
    N(sp.Rational(sum(v * f for v, f in zip(_vals10, _freq10)), sum(_freq10))))

_d11 = [12, 15, 9, 20, 17]
B.q("m-stat-11", "mean-variance", 1,
    r"The range of the data $12,15,9,20,17$ is",
    [r"$11$", r"$8$", r"$5$", r"$29$"],
    r"Range $=$ largest $-$ smallest $=20-9=11$.",
    N(max(_d11) - min(_d11)))

_X12 = [(0, sp.Rational(3, 10)), (1, sp.Rational(1, 2)), (2, sp.Rational(1, 5))]
_E12 = sum(v * p_ for v, p_ in _X12)
B.q("m-stat-12", "mean-variance", 3,
    r"A random variable $X$ takes the values $0,1,2$ with probabilities $0.3,\ 0.5,\ 0.2$. Its variance $D(X)$ is",
    [r"$0.49$", r"$0.9$", r"$1.3$", r"$0.7$"],
    r"""$E(X)=0\cdot0.3+1\cdot0.5+2\cdot0.2=0.9$, $E(X^2)=0+0.5+4\cdot0.2=1.3$.

$D(X)=E(X^2)-[E(X)]^2=1.3-0.81=0.49$.""",
    N(sum((v - _E12) ** 2 * p_ for v, p_ in _X12)))

# ----------------------------------------------------------- normal distribution
B.q("m-norm-01", "normal-distribution", 1,
    r"$X\sim N(2,\sigma^2)$. Then $P(X<2)=$",
    [r"$0.5$", r"$0.25$", r"$1$", r"It depends on $\sigma$"],
    r"The normal curve is symmetric about $x=\mu=2$, so exactly half of the probability lies below the mean: $P(X<2)=0.5$, whatever $\sigma$ is.",
    N(NormalDist(2, 1.7).cdf(2)))


def nd_with_tail(mu, point, upper_tail):
    """Normal distribution with mean mu such that P(X > point) = upper_tail."""
    z = NormalDist().inv_cdf(1 - upper_tail)
    return NormalDist(mu, (point - mu) / z)


_nd2 = nd_with_tail(1, 3, 0.2)
B.q("m-norm-02", "normal-distribution", 1,
    r"$X\sim N(1,\sigma^2)$ and $P(X>3)=0.2$. Then $P(X<-1)=$",
    [r"$0.2$", r"$0.8$", r"$0.3$", r"$0.4$"],
    r"$-1$ and $3$ are symmetric about $\mu=1$ (both are $2$ away). By symmetry $P(X<-1)=P(X>3)=0.2$.",
    N(round(_nd2.cdf(-1), 6), rel=1e-4))

_nd3 = nd_with_tail(3, 5, 0.2)
B.q("m-norm-03", "normal-distribution", 3,
    r"$X\sim N(3,\sigma^2)$ and $P(X<5)=0.8$. Then $P(1<X<3)=$",
    [r"$0.3$", r"$0.2$", r"$0.6$", r"$0.4$"],
    r"$P(3<X<5)=0.8-0.5=0.3$. The interval $(1,3)$ is the mirror image of $(3,5)$ in $\mu=3$, so $P(1<X<3)=0.3$.",
    N(round(_nd3.cdf(3) - _nd3.cdf(1), 6), rel=1e-4))

_std = NormalDist()
B.q("m-norm-04", "normal-distribution", 2,
    r"$X\sim N(\mu,\sigma^2)$ and $P(\mu-\sigma<X<\mu+\sigma)\approx0.6827$. Then $P(X>\mu+\sigma)\approx$",
    [r"$0.1587$", r"$0.3173$", r"$0.6827$", r"$0.3413$"],
    r"The two tails outside $(\mu-\sigma,\mu+\sigma)$ have total probability $1-0.6827=0.3173$ and are equal by symmetry, so each is $\dfrac{0.3173}2\approx0.1587$.",
    N(1 - _std.cdf(1), rel=1e-3))

B.q("m-norm-05", "normal-distribution", 1,
    r"Which statement about the normal density curve of $N(\mu,\sigma^2)$ is correct?",
    [r"It is symmetric about the line $x=\mu$", r"It is symmetric about the $y$-axis", r"Its maximum value does not depend on $\sigma$", r"The total area under it depends on $\mu$"],
    r"The bell curve is symmetric about $x=\mu$ (the $y$-axis only when $\mu=0$). Its peak height is $\dfrac1{\sigma\sqrt{2\pi}}$, which depends on $\sigma$, and the total area is always $1$.")

B.q("m-norm-06", "normal-distribution", 2,
    r"$X_1\sim N(0,1)$ and $X_2\sim N(0,4)$. Compared with the curve of $X_1$, the curve of $X_2$ is",
    [r"lower and more spread out", r"higher and narrower", r"shifted to the right", r"identical"],
    r"Both have mean $0$, so neither is shifted. $X_2$ has the larger standard deviation ($\sigma=2$), so its curve is flatter (lower peak) and more spread out.")

_nd7 = NormalDist(100, 10)
B.q("m-norm-07", "normal-distribution", 2,
    r"Exam scores follow $N(100,10^2)$. Using $P(\mu-2\sigma<X<\mu+2\sigma)\approx0.9545$, the proportion of students scoring above $120$ is about",
    [r"$2.3\%$", r"$4.6\%$", r"$95.4\%$", r"$15.9\%$"],
    r"$120=\mu+2\sigma$. The two tails beyond $\mu\pm2\sigma$ total $1-0.9545=0.0455$, so the upper tail is about $0.0228\approx2.3\%$.",
    N(100 * (1 - _nd7.cdf(120)), rel=0.02))

B.q("m-norm-08", "normal-distribution", 2,
    r"$X\sim N(0,1)$ and $P(X>1)=p$. Then $P(-1<X<0)=$",
    [r"$\dfrac12-p$", r"$1-p$", r"$1-2p$", r"$2p$"],
    r"$P(0<X<1)=0.5-p$, and by symmetry about $0$, $P(-1<X<0)=P(0<X<1)=\dfrac12-p$.",
    Expr(sp.Rational(1, 2) - p))

# P(0<X<4)=0.6 with mu=2 -> each side 0.3 -> P(X<0)=0.5-0.3
_z9 = NormalDist().inv_cdf(0.5 + 0.3)
_nd9 = NormalDist(2, 2 / _z9)
B.q("m-norm-09", "normal-distribution", 3,
    r"$X\sim N(2,\sigma^2)$ and $P(0<X<4)=0.6$. Then $P(X<0)=$",
    [r"$0.2$", r"$0.4$", r"$0.3$", r"$0.6$"],
    r"$(0,4)$ is symmetric about $\mu=2$, so the remaining probability $1-0.6=0.4$ is split equally between the two tails: $P(X<0)=0.2$.",
    N(round(_nd9.cdf(0), 6), rel=1e-4) if abs(_nd9.cdf(4) - _nd9.cdf(0) - 0.6) < 1e-9 else N(999))

B.q("m-norm-10", "normal-distribution", 2,
    r"$X\sim N(\mu,\sigma^2)$ and $P(X<1)=P(X>5)$. Then $\mu=$",
    [r"$3$", r"$2$", r"$4$", r"$6$"],
    r"Equal tail probabilities mean $1$ and $5$ are symmetric about the mean: $\mu=\dfrac{1+5}2=3$.",
    N([v for v in range(-10, 11) if abs(NormalDist(v, 1.3).cdf(1) - (1 - NormalDist(v, 1.3).cdf(5))) < 1e-12][0]))

B.q("m-norm-11", "normal-distribution", 1,
    r"$X\sim N(50,4^2)$. The standardised value $z=\dfrac{X-\mu}{\sigma}$ of $X=58$ is",
    [r"$2$", r"$8$", r"$0.5$", r"$\dfrac{29}{25}$"],
    r"$z=\dfrac{58-50}{4}=2$: the value $58$ lies two standard deviations above the mean.",
    N(sp.Rational(58 - 50, 4)))
