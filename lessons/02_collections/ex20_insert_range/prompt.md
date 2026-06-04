# ex20_insert_range

Practice inserting a new interval into an existing sorted, disjoint set of
intervals.

## Task

In `solution.py`, implement:

```python
def insert_range(
    ranges: list[tuple[int, int]],
    new_range: tuple[int, int],
) -> list[tuple[int, int]]:
    ...
```

You are given:

- `ranges`: a list of inclusive integer ranges `(start, end)` sorted by `start`.
- `ranges` contains no overlaps and no touching ranges.
  (So for consecutive ranges `(a, b)` then `(c, d)`, you have `c > b + 1`.)
- `new_range`: one additional valid inclusive range `(start, end)`.

Return a new sorted list of ranges that is the union of `ranges` and
`new_range`, merging any overlaps OR touching ranges.

## Examples

- `insert_range([(1, 2), (6, 7)], (3, 5))` -> `[(1, 7)]` (touches both)
- `insert_range([], (4, 4))` -> `[(4, 4)]`

## Constraints (for practice)

- Do not sort the entire list.
- Do not expand ranges into lists of numbers.
- Do not use a `set`.

Disallowed examples:

```python
# Don't do this.
all_ranges = sorted(ranges + [new_range])
```

```python
# Don't do this.
nums = []
for s, e in ranges:
    nums.extend(range(s, e + 1))
```
