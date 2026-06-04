# ex18_range_intersection

Practice two-pointer scanning over sorted ranges.

## Task

In `solution.py`, implement:

```python
def intersect_ranges(
    a: list[tuple[int, int]],
    b: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    ...
```

Each input is a list of inclusive integer ranges `(start, end)`.

Assumptions about inputs:

- Each list is sorted by `start`.
- Ranges within the same list do not overlap and do not touch.
- Every range is valid: `start <= end`.

Return the list of intersections between ranges from `a` and `b`, also as
inclusive ranges, sorted by `start`.

Rules:

- If there is no overlap, the intersection is empty (emit nothing).
- Touching at a point counts as an intersection of length 1.
  Example: `(1, 3)` intersect `(3, 5)` -> `(3, 3)`.

## Examples

- `intersect_ranges([(1, 5)], [(2, 3)])` -> `[(2, 3)]`
- `intersect_ranges([(1, 2), (5, 7)], [(3, 4), (6, 10)])` -> `[(6, 7)]`

## Constraints (for practice)

- Do not expand ranges into lists of numbers.
- Do not use `set` math.

Disallowed examples:

```python
# Don't do this.
nums = []
for s, e in a:
    nums.extend(range(s, e + 1))
```

```python
# Don't do this.
return sorted(set(nums_a) & set(nums_b))
```
