## Laws of exponents and logarithms

For $a,b>0$ and real $m,n$:
$$a^m a^n=a^{m+n},\quad \frac{a^m}{a^n}=a^{m-n},\quad (a^m)^n=a^{mn},\quad a^{-n}=\frac1{a^n},\quad a^{\frac mn}=\sqrt[n]{a^m}.$$

$\log_a N=b\iff a^b=N$ (with $a>0$, $a\ne1$, $N>0$). Hence $\log_a1=0$, $\log_aa=1$, $a^{\log_aN}=N$.

$$\log_a(MN)=\log_aM+\log_aN,\quad \log_a\frac MN=\log_aM-\log_aN,\quad \log_aM^n=n\log_aM$$
$$\text{change of base: }\log_ab=\frac{\log_cb}{\log_ca},\qquad \log_ab\cdot\log_ba=1,\qquad \log_{a^m}b^n=\frac nm\log_ab.$$

$\lg x=\log_{10}x$ and $\ln x=\log_ex$ ($e\approx2.718$).

## Graphs and properties

| Function | Domain | Range | Monotonic | Fixed point |
|---|---|---|---|---|
| $y=a^x$ | $\mathbb R$ | $(0,+\infty)$ | increasing if $a>1$, decreasing if $0<a<1$ | $(0,1)$ |
| $y=\log_ax$ | $(0,+\infty)$ | $\mathbb R$ | increasing if $a>1$, decreasing if $0<a<1$ | $(1,0)$ |
| $y=x^\alpha$ | depends on $\alpha$ | | increasing on $(0,\infty)$ if $\alpha>0$ | $(1,1)$ |

$y=a^x$ and $y=\log_ax$ are inverse functions: their graphs are symmetric about $y=x$.

**Comparing values:** compare each number with benchmarks $0$ and $1$ ($a^0=1$, $\log_a1=0$, $\log_aa=1$), or use monotonicity with a common base.

## Worked examples

**Example 1.** Evaluate $\log_2 24-\log_2 3+8^{\frac23}$.

*Solution.* $\log_2\dfrac{24}{3}=\log_28=3$ and $8^{\frac23}=(2^3)^{\frac23}=4$. Total $7$.

**Example 2.** Compare $a=0.3^{0.2}$, $b=\log_{0.3}2$, $c=2^{0.3}$.

*Solution.* $0<a<1$ (base below 1, positive exponent), $b<0$ (base below 1, argument above 1), $c>1$. So $b<a<c$.

**Example 3.** Solve $\log_3(x+1)+\log_3(x-1)=1$.

*Solution.* Domain $x>1$. $\log_3(x^2-1)=1\Rightarrow x^2-1=3\Rightarrow x=\pm2$; only $x=2$ is in the domain.

## Common traps

- $\log_a(M+N)\ne\log_aM+\log_aN$.
- Forgetting the domain $x>0$ inside a logarithm, especially after combining logs.
- Rejecting nothing after a substitution $t=a^x$: remember $t>0$.
- A negative exponent means a reciprocal, not a negative number.
