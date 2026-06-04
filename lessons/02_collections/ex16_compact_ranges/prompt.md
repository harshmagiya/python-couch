# ex16_compact_ranges

Practice scanning a sorted list and emitting grouped ranges.

## Task

In `solution.py`, implement:

```python
def compact_ranges(nums: list[int]) -> list[tuple[int, int]]:
    ...
```

Given a sorted list of **unique** integers, return a list of inclusive ranges
that compact consecutive runs.

Rules:

- If `nums` is empty, return `[]`.
- A run is consecutive when each next number is exactly `prev + 1`.
- Each output tuple is `(start, end)`.
- A single number becomes `(n, n)`.

## Examples

- `compact_ranges([1, 2, 3, 5, 6, 9])` -> `[(1, 3), (5, 6), (9, 9)]`
- `compact_ranges([])` -> `[]`

## Constraints (for practice)

- Do not sort the input.
- Do not use `itertools.groupby`.

Disallowed examples:

```python
nums = sorted(nums)
```

```python
from itertools import groupby

# (Don't do this.)
return [(g[0], g[-1]) for _, g in groupby(nums, key=...)]
```
