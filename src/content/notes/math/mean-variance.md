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
