# ex02_first_and_last

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def first_and_last(arr: list[int], target: int) -> tuple[int, int]:
    ...
```

Behavior:

- `arr` is sorted in non-decreasing order.
- Return `(first_index, last_index)` of `target` in `arr`.
- If `target` is not present, return `(-1, -1)`.
- When `target` appears exactly once, `first_index == last_index`.

## Examples

- `first_and_last([1, 3, 5, 7, 9], 7) == (3, 3)`
- `first_and_last([1, 3, 5, 7, 9], 4) == (-1, -1)`
- `first_and_last([1, 2, 2, 2, 3, 4], 2) == (1, 3)`
- `first_and_last([], 5) == (-1, -1)`
- `first_and_last([5, 5, 5, 5], 5) == (0, 3)`
- `first_and_last([1, 2, 3], 5) == (-1, -1)`

## Complexity requirement

Your solution **must run in O(log n)**. Each of the two indices is found with one binary search variant.

## Constraints (for practice)

- Do not import or use the `bisect` module.
- Do not do a linear scan to find duplicates; both `first` and `last` must come from a logarithmic search.

## Disallowed examples

```python
import bisect
lo = bisect.bisect_left(arr, target)
hi = bisect.bisect_right(arr, target) - 1
return (lo, hi) if lo < hi + 1 else (-1, -1)  # WRONG: bypasses the algorithm
```

```python
# WRONG: O(n) scan to find duplicates
indices = [i for i, x in enumerate(arr) if x == target]
if not indices:
    return (-1, -1)
return (indices[0], indices[-1])
```
