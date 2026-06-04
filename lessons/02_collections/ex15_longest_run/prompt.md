# ex15_longest_run

Practice single-pass tracking of a run length.

## Task

In `solution.py`, implement:

```python
def longest_run(items: list[str]) -> int:
    ...
```

Return the length of the longest consecutive run of the same string.

Rules:

- If `items` is empty, return `0`.
- Treat strings exactly as given (case-sensitive).
- Empty strings are allowed.

## Examples

- `longest_run(["a", "a", "b", "b", "b", "a"])` -> `3`
- `longest_run([])` -> `0`

## Constraints (for practice)

- Do not use `itertools.groupby`.

Disallowed example:

```python
from itertools import groupby

return max(len(list(g)) for _, g in groupby(items))
```
