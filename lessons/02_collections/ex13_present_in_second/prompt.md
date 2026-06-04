# ex13_present_in_second

Practice using a set for membership while preserving order and deduplicating output.

## Task

In `solution.py`, implement:

```python
def present_in_second(first: list[str], second: list[str]) -> list[str]:
    ...
```

Return a list of distinct items from `first` that also appear in `second`.

Output rules:

- Preserve the order of first appearance from `first`.
- Include each item at most once in the result, even if it appears multiple times in `first`.
- Treat strings exactly as given (case-sensitive).
- Empty strings are allowed.

## Examples

- `present_in_second(["a", "b", "a", "c"], ["b", "c"])` -> `["b", "c"]`
- `present_in_second(["x", "x"], ["x"])` -> `["x"]`

## Constraints (for practice)

- Do not use nested loops.

Disallowed example:

```python
out = []
for x in first:
    for y in second:
        if x == y:
            out.append(x)
```

- Do not use set intersection as your final result (it loses order).

Disallowed example:

```python
return list(set(first) & set(second))
```
