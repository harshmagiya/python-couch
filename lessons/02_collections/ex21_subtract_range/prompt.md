# ex21_subtract_range

Practice subtracting an interval from a sorted set of disjoint intervals.

## Task

In `solution.py`, implement:

```python
def subtract_range(
    ranges: list[tuple[int, int]],
    remove: tuple[int, int],
) -> list[tuple[int, int]]:
    ...
```

You are given:

- `ranges`: a list of inclusive integer ranges `(start, end)` sorted by `start`.
- `ranges` contains no overlaps and no touching ranges.
- `remove`: one valid inclusive range `(start, end)`.

Return a new sorted list of ranges representing `ranges` with `remove` removed.

Rules:

- You may split a range into up to two ranges.
- If `remove` does not overlap anything, return the original ranges (as a new list).
- Touching counts as overlap at a point.
  Example: removing `(3, 3)` from `(1, 5)` yields `(1, 2)` and `(4, 5)`.

## Examples

- `subtract_range([(1, 10)], (3, 4))` -> `[(1, 2), (5, 10)]`
- `subtract_range([(1, 2), (6, 7)], (3, 5))` -> `[(1, 2), (6, 7)]`

## Constraints (for practice)

- Do not sort.
- Do not expand ranges into lists of numbers.
- Do not use `set`.

Disallowed examples:

```python
# Don't do this.
sorted(ranges)
```

```python
# Don't do this.
nums = []
for s, e in ranges:
    nums.extend(range(s, e + 1))
```
