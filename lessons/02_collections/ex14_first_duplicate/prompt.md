# ex14_first_duplicate

Practice using a set to detect repeats in one pass.

## Task

In `solution.py`, implement:

```python
def first_duplicate(items: list[str]) -> str | None:
    ...
```

Return the first item whose **second occurrence** appears earliest when scanning left-to-right.

Rules:

- If there is no duplicate, return `None`.
- Treat strings exactly as given (case-sensitive).
- Empty strings are allowed.

## Examples

- `first_duplicate(["a", "b", "a", "b"])` -> `"a"` (the second `"a"` occurs at index 2, earlier than the second `"b"` at index 3)
- `first_duplicate(["x", "y", "z"])` -> `None`

## Constraints (for practice)

- Do not use `items.count(x)` inside a loop.

Disallowed example:

```python
for x in items:
    if items.count(x) > 1:
        return x
```

- Do not track "seen" as a list.

Disallowed example:

```python
seen = []
for x in items:
    if x in seen:
        return x
    seen.append(x)
```
