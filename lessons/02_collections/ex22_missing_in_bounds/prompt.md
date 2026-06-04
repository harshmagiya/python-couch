# ex22_missing_in_bounds

Practice computing the complement of ranges within a bounding interval.

## Task

In `solution.py`, implement:

```python
def missing_in_bounds(
    ranges: list[tuple[int, int]],
    bounds: tuple[int, int],
) -> list[tuple[int, int]]:
    ...
```

You are given:

- `ranges`: a list of inclusive integer ranges `(start, end)` sorted by `start`.
- `ranges` contains no overlaps and no touching ranges.
- `bounds`: an inclusive bounding range `(lo, hi)` with `lo <= hi`.

Return a sorted list of inclusive ranges representing all integers in `bounds`
that are NOT covered by any range in `ranges`.

Notes:

- Ranges may extend outside `bounds`; treat them as clipped to `bounds`.
- Touching counts as continuous coverage.

## Examples

- `missing_in_bounds([(2, 3), (6, 7)], (1, 8))` -> `[(1, 1), (4, 5), (8, 8)]`
- `missing_in_bounds([], (5, 7))` -> `[(5, 7)]`

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
