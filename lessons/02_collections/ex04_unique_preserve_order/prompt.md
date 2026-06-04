# ex04_unique_preserve_order

Practice using a set for membership while keeping a stable output order.

## Recall (no code)

- What property of a `set` makes it good for membership checks?
- Why is `list(set(items))` usually a bad idea when ordering matters?

## Task

In `solution.py`, implement:

```python
def unique_preserve_order(items: list[str]) -> list[str]:
    ...
```

Return a new list containing the first occurrence of each distinct item in `items`, preserving the original left-to-right order.

Rules:

- Treat strings exactly as given (case-sensitive).
- Empty strings are allowed.
- If `items` is empty, return `[]`.

## Examples

- `unique_preserve_order(["a", "b", "a", "c", "b"])` -> `["a", "b", "c"]`
- `unique_preserve_order(["", "", "x"])` -> `["", "x"]`

## Constraints (for practice)

- Do not use `dict.fromkeys`.

Disallowed example:

```python
return list(dict.fromkeys(items))
```

- Do not use `set(items)` (or similar) as your result.

Disallowed example:

```python
return list(set(items))
```
