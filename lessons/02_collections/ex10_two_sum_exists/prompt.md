# ex10_two_sum_exists

Practice using a set for fast lookups while scanning once.

## Task

In `solution.py`, implement:

```python
def two_sum_exists(nums: list[int], target: int) -> bool:
    ...
```

Return `True` if there exist two different indices `i != j` such that `nums[i] + nums[j] == target`. Otherwise return `False`.

Rules:

- If `nums` has fewer than 2 items, return `False`.
- Duplicates count as separate indices (e.g., `[3, 3]` can satisfy target `6`).

## Examples

- `two_sum_exists([2, 7, 11, 15], 9)` -> `True`  (2 + 7)
- `two_sum_exists([1, 2, 3], 7)` -> `False`
- `two_sum_exists([3, 3], 6)` -> `True`

## Constraints (for practice)

- Do not use nested loops (avoid O(n^2)).

Disallowed example:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return True
```

- Do not sort `nums`.

Disallowed example:

```python
nums.sort()
```
