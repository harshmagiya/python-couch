# ex03_pair_sum_sorted

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def pair_sum_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    ...
```

Behavior:

- `nums` is sorted in non-decreasing order.
- Return `(i, j)` with `i < j` and `nums[i] + nums[j] == target`.
- If no such pair exists, return `None`.
- If multiple pairs exist, return any one of them (the test pins the simplest).

## Examples

- `pair_sum_sorted([1, 2, 3, 4, 6], 7) == (1, 4)` (2 + 5? no: 3 + 4 = 7 -> (2, 3) also valid)
- `pair_sum_sorted([1, 2, 3, 4, 6], 10) == (3, 4)` (4 + 6 = 10)
- `pair_sum_sorted([1, 2, 3], 100) is None`
- `pair_sum_sorted([], 0) is None`
- `pair_sum_sorted([3, 3], 6) == (0, 1)`

## Complexity requirement

Your solution **must run in O(n)**. Two pointers from both ends, converging.

## Constraints (for practice)

- No `dict` or `set` lookup of "have I seen a complement?". The whole point of this exercise is the two-pointer technique on a *sorted* input.
- Each index pair should be considered at most once.

## Disallowed examples

```python
seen = set()
for i, x in enumerate(nums):                          # WRONG: dict/set lookup
    if target - x in seen:
        return (some_i, i)   # this is the two-sum-with-hash pattern
    seen.add(x)
```

```python
for i in range(len(nums)):                              # WRONG: O(n^2) brute force
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return (i, j)
return None
```
