## Definition and meaning

$$f'(x_0)=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$$

- Geometric meaning: the **slope of the tangent** at $(x_0,f(x_0))$. Tangent line: $y-f(x_0)=f'(x_0)(x-x_0)$.
- Physical meaning: velocity $v(t)=s'(t)$, acceleration $a(t)=v'(t)$.

## Rules

| $f(x)$ | $f'(x)$ |
|---|---|
| $C$ | $0$ |
| $x^n$ | $nx^{n-1}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x\ln a$ |
| $\ln x$ | $\dfrac1x$ |
| $\log_ax$ | $\dfrac1{x\ln a}$ |

$$(u\pm v)'=u'\pm v',\quad (uv)'=u'v+uv',\quad \left(\frac uv\right)'=\frac{u'v-uv'}{v^2},\quad [f(g(x))]'=f'(g(x))\,g'(x).$$

## Applications

- $f'(x)>0$ on an interval ⇒ $f$ increasing there; $f'(x)<0$ ⇒ decreasing.
- **Local extremum** at $x_0$: $f'(x_0)=0$ **and** $f'$ changes sign ($+\to-$: maximum; $-\to+$: minimum).
- **Max/min on $[a,b]$:** compare $f$ at critical points inside $[a,b]$ and at the endpoints.
- Counting zeros: use the extreme values and the end behaviour.

## Basic integrals

$\displaystyle\int_a^bf(x)\,dx=F(b)-F(a)$ where $F'=f$. Area between curves on $[a,b]$: $\displaystyle\int_a^b(\text{upper}-\text{lower})\,dx$. Examples: $\int x^n dx=\dfrac{x^{n+1}}{n+1}$, $\int\cos x\,dx=\sin x$, $\int\dfrac1x dx=\ln|x|$.

## Worked examples

**Example 1.** Tangent to $y=x^3-2x$ at $x=1$.

*Solution.* $y(1)=-1$, $y'=3x^2-2$, $k=1$. Tangent: $y+1=x-1$, i.e. $y=x-2$.

**Example 2.** Find the extrema of $f(x)=x^3-3x^2+1$.

*Solution.* $f'(x)=3x(x-2)$: $+$ for $x<0$, $-$ on $(0,2)$, $+$ for $x>2$. Local max $f(0)=1$, local min $f(2)=-3$.

**Example 3.** $f(x)=x^2-a\ln x$ has an extremum at $x=1$. Find $a$.

*Solution.* $f'(x)=2x-\dfrac ax$, $f'(1)=2-a=0\Rightarrow a=2$. Check: $f'(x)=\dfrac{2(x^2-1)}x$ changes sign at $1$ ✔.

## Common traps

- $f'(x_0)=0$ alone does not guarantee an extremum ($f(x)=x^3$ at $0$).
- Tangent **at** a point vs tangent **through** a point (the point may not be on the curve).
- In $\lim\dfrac{f(x_0+2h)-f(x_0)}{h}$ the answer is $2f'(x_0)$.
- Forgetting the domain (e.g. $x>0$ for $\ln x$) when finding monotonic intervals.
