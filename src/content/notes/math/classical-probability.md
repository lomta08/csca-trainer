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
