# ex01_bsearch_index

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def bsearch_index(arr: list[int], target: int) -> int:
    ...
```

Behavior:

- `arr` is sorted in non-decreasing order.
- Return an index `i` such that `arr[i] == target`.
- If `target` is not present, return `-1`.
- When `target` appears multiple times, returning *any* valid index is acceptable in this exercise.
  (The next exercise sharpens this to first / last position.)

## Examples

- `bsearch_index([1, 3, 5, 7, 9], 7) == 3`
- `bsearch_index([1, 3, 5, 7, 9], 4) == -1`
- `bsearch_index([], 5) == -1`
- `bsearch_index([5], 5) == 0`
- `bsearch_index([1, 1, 1, 1], 1)` -> some valid index in `[0, 1, 2, 3]`

## Complexity requirement

Your solution **must run in O(log n)**. A linear scan is wrong even if it happens to pass the value tests.

## Constraints (for practice)

- Do not import or use the `bisect` module.
- The loop must halve the search range each iteration.

## Disallowed examples

```python
import bisect
return bisect.bisect_left(arr, target)  # WRONG: bypasses the algorithm
```

```python
for i, x in enumerate(arr):              # WRONG: O(n) linear scan
    if x == target:
        return i
return -1
```
