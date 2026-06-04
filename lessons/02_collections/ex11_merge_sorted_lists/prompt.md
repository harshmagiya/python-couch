# ex11_merge_sorted_lists

Practice two-pointer iteration.

## Task

In `solution.py`, implement:

```python
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    ...
```

Both `a` and `b` are already sorted in non-decreasing order.
Return a new sorted list containing all elements from `a` and `b`.

Rules:

- Do not mutate `a` or `b`.
- Preserve duplicates.
- Either input can be empty.

## Examples

- `merge_sorted([1, 3, 5], [2, 4])` -> `[1, 2, 3, 4, 5]`
- `merge_sorted([1, 1], [1])` -> `[1, 1, 1]`

## Constraints (for practice)

- Do not call `sorted(...)` on the concatenation.

Disallowed example:

```python
return sorted(a + b)
```
