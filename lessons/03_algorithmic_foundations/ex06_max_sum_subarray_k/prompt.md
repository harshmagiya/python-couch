# ex06_max_sum_subarray_k

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def max_sum_subarray_k(nums: list[int], k: int) -> int:
    ...
```

Behavior:

- Return the maximum sum of any contiguous subarray of length exactly `k`.
- If `k > len(nums)` or `len(nums) == 0` (with `k > 0`), raise `ValueError`.
- The function must use a sliding window: compute the sum of the first
  `k` elements, then *slide* by subtracting the element leaving the
  window and adding the element entering it. Do not recompute the sum
  from scratch for each window.

## Examples

- `max_sum_subarray_k([1, 4, 2, 10], 2) == 12`  (window [2, 10])
- `max_sum_subarray_k([1, 4, 2, 10], 1) == 10`  (window [10])
- `max_sum_subarray_k([1, 4, 2, 10], 4) == 17`  (the whole array)
- `max_sum_subarray_k([-1, -2, -3], 1) == -1`   (least negative)
- `max_sum_subarray_k([-1, -2, -3], 3) == -6`
- `max_sum_subarray_k([5], 1) == 5`

Errors:

- `max_sum_subarray_k([1, 2, 3], 4)` raises `ValueError` (k > len(nums))
- `max_sum_subarray_k([], 1)` raises `ValueError` (empty nums with k > 0)
- `max_sum_subarray_k([1, 2], 0)` returns 0  (k = 0; one window of size 0 with sum 0)

## Complexity requirement

- O(n) time.
- O(1) extra space.

## Constraints (for practice)

- No `sum(nums[i:i+k])` inside a loop (that would be O(n*k) total).
- The first window's sum can be computed directly; every subsequent
  window must use the slide-by-one update.

## Disallowed examples

```python
best = float("-inf")
for i in range(len(nums) - k + 1):               # WRONG: O(n*k)
    best = max(best, sum(nums[i:i + k]))
return best
```

```python
return max(sum(nums[i:i + k]) for i in range(len(nums) - k + 1))  # WRONG: same issue
```
