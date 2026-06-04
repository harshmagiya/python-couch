# 1-D Dynamic Programming: Climbing Stairs

## What problem this solves

Count the number of distinct ways to climb a staircase of `n` steps where each move is 1 or 2 steps. The result is the Fibonacci sequence shifted by one position. This is the cleanest introduction to bottom-up 1-D dynamic programming: the subproblem structure, the recurrence, the base cases, and the space optimisation all appear in the simplest possible form.

## Mental model

Let `ways(i)` be the number of ways to reach step `i`. To step on `i`, you must have come from `i - 1` (taking a 1-step) or from `i - 2` (taking a 2-step). So:

```
ways(i) = ways(i - 1) + ways(i - 2)
```

Base cases: `ways(0) = 1` (you are already at step 0; the empty sequence of moves is one way to "be at the top when n = 0"), `ways(1) = 1` (only the `1` move is possible).

The recurrence is the Fibonacci recurrence. Closed form: `ways(n) = F(n + 1)`, where `F` is the standard Fibonacci sequence with `F(0) = 0, F(1) = 1`.

## Why bottom-up

Two equivalent ways to compute:

1. **Bottom-up**: iterate `i` from 2 to `n`, building up `ways(i)` from smaller values. O(n) time, O(1) space if you keep only the last two values.
2. **Top-down with memoisation**: recurse, but cache each `ways(i)` the first time it is computed. O(n) time, O(n) space for the cache.

The bottom-up form with two scalars is what the prompt asks for.

## Why it matters in real projects

- The Fibonacci-style recurrence shows up in: combinatorics (counting binary strings with no two adjacent 0s, etc.), the analysis of divide-and-conquer algorithms (the Master Theorem's recurrence), the "Tribonacci" generalisation in some financial forecasting libraries, and the dynamic-programming warmup section of every algorithms textbook.
- The 1-D DP shape generalises to a huge family of problems: longest increasing subsequence, edit distance (but 2-D), 0/1 knapsack, unbounded knapsack, longest common subsequence (2-D), and many more.
- The "keep only the last two values" trick — the space optimisation — is a foundational DP idea. It generalises to rolling-row DP for 2-D problems (e.g. edit distance, which is in the next extension).

## Common pitfalls

### Forgetting the base case `ways(0) = 1`

If you use `ways(0) = 0` (the more "natural" answer to "how many ways to be at step 0"), `climb_stairs(2)` returns `0` (wrong) instead of `2`. The convention is: an empty sequence of moves counts as one way to "be at the top" when `n = 0`.

### Off-by-one in the iteration range

`for i in range(2, n + 1)` is the correct range. `range(2, n)` is off by one and would miss the last value.

### O(n) space when O(1) is required

The full DP table is correct and easier to read, but the prompt explicitly bans it. Keep only `prev` and `curr` and shift them as you iterate.

### Recursion without memo

Works for tiny `n` (say, `n < 30`), but is exponentially slow beyond that. The prompt bans it.

## Edge cases

- `n = 0` -> `1` (by convention).
- `n = 1` -> `1`.
- `n = 2` -> `2`.
- `n < 0` -> raise `ValueError`.
- `n` very large (e.g. 10⁶): should still complete in O(n) time with O(1) memory.

## Quick check

`n = 4`:

- ways(0) = 1
- ways(1) = 1
- ways(2) = 1 + 1 = 2
- ways(3) = 2 + 1 = 3
- ways(4) = 3 + 2 = 5

Return 5. ✓

The five sequences are: `1+1+1+1`, `1+1+2`, `1+2+1`, `2+1+1`, `2+2`.

## ML/research connection

The Fibonacci recurrence is the simplest 1-D DP warmup, and the "keep only the last two values" trick is the prototype for the rolling-row optimisation in 2-D DP (next exercises: edit distance, then the O(min(m, n)) space variant). The recurrence itself shows up in combinatorics of binary strings and in the analysis of divide-and-conquer algorithms via the Master Theorem.
