## Key ideas

A **set** is a well-defined collection of distinct objects, called its **elements**. We write $a\in A$ ("$a$ belongs to $A$") or $a\notin A$.

- Elements are **distinct** (no repeats) and their order does not matter: $\{1,2\}=\{2,1\}$.
- **Representations:** listing $\{1,3,5\}$; description (set-builder) $\{x\mid x^2<4\}$; intervals $(-2,2)$; Venn diagrams.
- Read the letter before the bar: $\{x\mid y=\sqrt{x}\}$ is a set of $x$-values (a domain), while $\{y\mid y=\sqrt x\}$ is a set of $y$-values (a range).
- Standard sets: $\mathbb N$ (natural numbers, **including $0$**), $\mathbb N^*$ or $\mathbb N_+$ (positive integers), $\mathbb Z$, $\mathbb Q$, $\mathbb R$, and the empty set $\varnothing$.

## Relations and operations

| Name | Notation | Meaning |
|---|---|---|
| Subset | $A\subseteq B$ | every element of $A$ is in $B$ |
| Proper subset | $A\subsetneqq B$ | $A\subseteq B$ and $A\ne B$ |
| Intersection | $A\cap B$ | in $A$ **and** in $B$ |
| Union | $A\cup B$ | in $A$ **or** in $B$ (or both) |
| Complement | $\complement_U A$ | in the universal set $U$ but not in $A$ |

Useful facts:

- $\varnothing\subseteq A$ for every set $A$.
- A set with $n$ elements has $2^n$ subsets and $2^n-1$ proper subsets.
- $A\cap B=A\iff A\subseteq B$, and $A\cup B=B\iff A\subseteq B$.
- Counting: $|A\cup B|=|A|+|B|-|A\cap B|$.

## Worked examples

**Example 1.** $A=\{x\mid -1\le x<3\}$, $B=\{x\mid x>1\}$. Find $A\cap B$, $A\cup B$ and $A\cap\complement_{\mathbb R}B$.

*Solution.* Draw both on a number line. $A\cap B=(1,3)$; $A\cup B=[-1,+\infty)$. Since $\complement_{\mathbb R}B=(-\infty,1]$, we get $A\cap\complement_{\mathbb R}B=[-1,1]$. Note how the endpoint $1$ switches from open to closed in the complement.

**Example 2.** $A=\{1,2\}$ and $B=\{x\mid ax=1\}$ with $B\subseteq A$. Find all $a$.

*Solution.* If $a=0$, $B=\varnothing\subseteq A$ ✔. Otherwise $B=\{\tfrac1a\}$, so $\tfrac1a=1$ or $\tfrac1a=2$, giving $a=1$ or $a=\tfrac12$. Answer: $a\in\{0,1,\tfrac12\}$.

**Example 3.** How many subsets $M$ satisfy $\{1\}\subseteq M\subseteq\{1,2,3,4\}$?

*Solution.* $M$ must contain $1$; each of $2,3,4$ may be in or out: $2^3=8$ sets.

## Common traps

- Forgetting the **empty-set case** when a set depends on a parameter ($B\subseteq A$ allows $B=\varnothing$).
- Forgetting that elements must be **distinct** — check answers like $a=1$ in $\{1,a\}$.
- Treating $0\in\mathbb N$ as false: in CSCA/Chinese textbooks $\mathbb N$ contains $0$.
- Confusing $\in$ (element) with $\subseteq$ (subset): $\{0\}\subseteq\{0,1\}$ but $\{0\}\notin\{0,1\}$.
