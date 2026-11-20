## Key ideas

A sequence $\{a_n\}$ is a list $a_1,a_2,a_3,\dots$. $S_n=a_1+\dots+a_n$ and
$$a_n=\begin{cases}S_1,&n=1\\S_n-S_{n-1},&n\ge2\end{cases}\qquad\text{(always check } n=1\text{)}.$$

## Arithmetic and geometric sequences

| | Arithmetic (difference $d$) | Geometric (ratio $q\ne0$) |
|---|---|---|
| Definition | $a_{n+1}-a_n=d$ | $\dfrac{a_{n+1}}{a_n}=q$ |
| General term | $a_n=a_1+(n-1)d$ | $a_n=a_1q^{n-1}$ |
| Sum | $S_n=\dfrac{n(a_1+a_n)}2=na_1+\dfrac{n(n-1)}2d$ | $S_n=\dfrac{a_1(1-q^n)}{1-q}$ ($q\ne1$); $S_n=na_1$ ($q=1$) |
| Middle term | $2b=a+c$ | $b^2=ac$ |
| Index property | $m+n=p+q\Rightarrow a_m+a_n=a_p+a_q$ | $m+n=p+q\Rightarrow a_ma_n=a_pa_q$ |

Also: $a_n=a_m+(n-m)d$; in an arithmetic sequence $S_{2k-1}=(2k-1)a_k$.

## Useful techniques

- **Telescoping:** $\dfrac1{n(n+1)}=\dfrac1n-\dfrac1{n+1}$.
- **Subtract a shifted copy** for $\sum n\cdot q^n$ (arithmetic × geometric).
- **Recursions:** $a_{n+1}=pa_n+r$ — rewrite as $a_{n+1}+t=p(a_n+t)$ to get a geometric sequence.
- The max of $S_n$ for an arithmetic sequence with $d<0$: add up the terms while they are non-negative.

## Worked examples

**Example 1.** Arithmetic: $a_2=5$, $a_6=17$. Find $a_{10}$ and $S_{10}$.

*Solution.* $4d=12$, $d=3$, $a_1=2$. $a_{10}=2+27=29$; $S_{10}=\dfrac{10(2+29)}{2}=155$.

**Example 2.** Geometric with positive terms: $a_1=2$, $a_3=18$. Find $S_4$.

*Solution.* $q^2=9$, $q=3$. $S_4=\dfrac{2(3^4-1)}{3-1}=80$.

**Example 3.** $S_n=3n^2-n$. Find $a_n$.

*Solution.* For $n\ge2$: $a_n=3n^2-n-[3(n-1)^2-(n-1)]=6n-4$. $a_1=S_1=2=6\cdot1-4$ ✔. So $a_n=6n-4$.

## Common traps

- Using $q^n$ instead of $q^{n-1}$, or $nd$ instead of $(n-1)d$.
- Using the geometric sum formula when $q=1$.
- Forgetting that $a_n=S_n-S_{n-1}$ is only valid for $n\ge2$.
- $b^2=ac$ does not determine the sign of $b$: check whether terms must be positive.
