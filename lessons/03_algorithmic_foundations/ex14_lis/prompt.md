# ex14_lis

Read: `theory.md` (3-5 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def lis(nums: list[int]) -> int:
    ...
```

Behavior:

- Return the **length** of the longest strictly increasing subsequence of `nums`.
- A subsequence is *not* required to be contiguous. It is a sequence obtained by deleting some (possibly zero) elements without changing the order of the remaining elements.
- "Strictly increasing" means each element is strictly greater than the previous.
- For an empty list, return `0` (no elements, no subsequence).

## Examples

- `lis([]) == 0`
- `lis([5]) == 1`
- `lis([1, 2, 3, 4, 5]) == 5` (the whole array)
- `lis([5, 4, 3, 2, 1]) == 1` (any single element)
- `lis([2, 2, 2]) == 1` (no two elements are strictly increasing)
- `lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4` (e.g. `[2, 3, 7, 18]` or `[2, 3, 7, 101]`)
- `lis([0, 1, 0, 3, 2, 3]) == 4` (e.g. `[0, 1, 2, 3]`)
- `lis([-1, 0, 1, 2, -1, -1]) == 4` (e.g. `[-1, 0, 1, 2]`)

## Complexity requirement

- O(n²) time and O(n) extra space (the standard DP formulation).
- The O(n log n) patience-sorting variant is mentioned in `theory.md` for context but is **not** required here; the prompt asks for the O(n²) DP.

## Constraints (for practice)

- Use the DP recurrence: `dp[i]` is the length of the longest increasing subsequence that *ends at index `i`* (i.e. `nums[i]` is the last element). The recurrence is `dp[i] = max(dp[j] + 1)` for all `j < i` with `nums[j] < nums[i]`. The answer is `max(dp)`.
- No recursive solution with no memoisation (would be exponential).
- No full n×n matrix; just a 1-D `dp` array of length `n`.

## Disallowed examples

```python
def lis(nums):                                  # WRONG: exponential recursion
    if not nums:
        return 0
    best = 1
    for i in range(len(nums)):
        tail = lis(nums[:i])
        if nums[i] > (nums[i - 1] if i > 0 else float("-inf")):
            best = max(best, 1 + ...)
    return best
```

The exact form varies, but the shape is "recurse on every prefix" without memoisation. Exponential time, disallowed.

```python
import itertools
def lis(nums):                                  # WRONG: enumerates all subsequences
    best = 0
    for k in range(1, len(nums) + 1):
        for combo in itertools.combinations(nums, k):
            if all(combo[i] < combo[i + 1] for i in range(len(combo) - 1)):
                best = max(best, k)
    return best
```

Enumerates all C(n, k) subsequences for every k, then checks each. At least
O(2^n). Forbidden by the prompt.

## Hints

- Initialise `dp[i] = 1` for every `i` (a single element is an increasing subsequence of length 1).
- For each `i`, look back at every `j < i`. If `nums[j] < nums[i]`, you can extend the LIS ending at `j` by `nums[i]`, so `dp[i] = max(dp[i], dp[j] + 1)`.
- The answer is `max(dp)`, **not** `dp[-1]`. A common bug is to return `dp[n - 1]`, which is only correct when the longest increasing subsequence happens to end at the last element.
