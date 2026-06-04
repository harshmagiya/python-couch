# ex13_climb_stairs

Read: `theory.md` (3-4 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def climb_stairs(n: int) -> int:
    ...
```

Behavior:

- You are at the bottom of a staircase with `n` steps. At each step you can take 1 or 2 stairs.
- Return the number of **distinct** ways to reach the top.
- The order of the moves matters. For example, with 2 steps, the ways are `1+1` and `2`, so the answer is 2.

## Examples

- `climb_stairs(0) == 1` (the empty sequence of moves: you are already at the top, by convention)
- `climb_stairs(1) == 1` (only `1`)
- `climb_stairs(2) == 2` (`1+1` and `2`)
- `climb_stairs(3) == 3` (`1+1+1`, `1+2`, `2+1`)
- `climb_stairs(4) == 5`
- `climb_stairs(10) == 89`

## Complexity requirement

- O(n) time.
- O(1) extra space (no full DP table).

## Constraints (for practice)

- Use the recurrence `ways(i) = ways(i - 1) + ways(i - 2)`, with base cases `ways(0) = 1`, `ways(1) = 1`.
- Keep only the last two values, not a full array.
- For `n < 0`, raise `ValueError`.

## Disallowed examples

```python
def climb_stairs(n):                                # WRONG: full DP table
    if n < 0:
        raise ValueError("n must be >= 0")
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

This is correct but uses O(n) extra memory. The prompt asks for O(1).

```python
def climb_stairs(n):                                # WRONG: recursion without memo
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)
```

Recursion without memoization recomputes the same subproblems exponentially
many times. For `n = 30` this is still fast, but for `n = 100` it is
catastrophically slow (more than 2^90 calls). Use bottom-up with O(1)
space, or top-down with `@functools.cache`.

## Hints

- This is the same recurrence as the Fibonacci sequence (just shifted: `F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, F(5) = 5, ...` and `climb_stairs(n) = F(n + 1)`).
- The O(1) space trick: keep only the last two values, `prev` and `curr`, and shift them as you iterate.
