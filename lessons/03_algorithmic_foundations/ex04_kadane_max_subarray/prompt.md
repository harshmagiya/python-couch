# ex04_kadane_max_subarray

Read: `theory.md` (3-4 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def max_subarray_sum(nums: list[int]) -> int:
    ...
```

Behavior:

- Return the maximum sum of any non-empty contiguous subarray of `nums`.
- A "contiguous subarray" means a slice `nums[i:j]` for some `0 <= i < j <= len(nums)`. The subarray must be non-empty, so the result is always a real number (never "no subarray").
- For an all-negative input, the answer is the *largest* (least-negative) single element.
- If `nums` is empty, raise `ValueError`.

## Examples

- `max_subarray_sum([1, -3, 2, 1, -1]) == 3` (subarray `[2, 1]`, or `[1, -3, 2, 1]`)
- `max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6` (subarray `[4, -1, 2, 1]`)
- `max_subarray_sum([5]) == 5`
- `max_subarray_sum([-3, -1, -2]) == -1` (largest single element)
- `max_subarray_sum([1, 2, 3, 4, 5]) == 15` (the whole array)
- `max_subarray_sum([-1, 2, -1, 3, -2]) == 4` (subarray `[2, -1, 3]`)

## Complexity requirement

- O(n) time, single pass.
- O(1) extra space (a few scalar variables; no full DP table).

## Constraints (for practice)

- Single pass. You may keep two running scalars: the best sum *ending* at the current position, and the best sum seen so far. Update both in one loop.
- No `sum(nums[i:j])` inside a loop.
- No full DP table of length `n`.

## Disallowed examples

```python
best = 0
for i in range(len(nums)):                              # WRONG: O(n^2) brute force
    for j in range(i + 1, len(nums) + 1):
        best = max(best, sum(nums[i:j]))
return best
```

```python
# WRONG: full DP table
dp = [0] * len(nums)                                    # unnecessary O(n) space
dp[0] = nums[0]
for i in range(1, len(nums)):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])
return max(dp)
```

```python
import itertools
return max(sum(s) for s in itertools.chain(             # WRONG: O(n^3) over all subarrays
    (nums[i:j] for i in range(len(nums))
              for j in range(i + 1, len(nums) + 1))
))
```

## Hints

- The key insight: at each position, you only need to know "the best sum of a subarray *ending here*". Either extend the previous best-ending-here by adding the current element, or start fresh from the current element (if the previous sum was negative and dragging you down).
- Initialise carefully: the running `best_ending_here` should be `nums[0]`, not `0` (because all-negative inputs would otherwise return 0 instead of the largest element).
