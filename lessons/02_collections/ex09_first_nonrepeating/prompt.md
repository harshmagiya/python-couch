# ex09_first_nonrepeating

Practice combining a count pass with an order-preserving scan.

## Task

In `solution.py`, implement:

```python
def first_nonrepeating(items: list[str]) -> str | None:
    ...
```

Return the first item (left-to-right) that appears exactly once in `items`.

Rules:

- If no such item exists, return `None`.
- Treat strings exactly as given (case-sensitive).
- Empty strings are allowed.
- If `items` is empty, return `None`.

## Examples

- `first_nonrepeating(["a", "b", "a", "c", "b", "d"])` -> `"c"`
- `first_nonrepeating(["x", "x"])` -> `None`

## Constraints (for practice)

- Do not use `collections.Counter`.

Disallowed example:

```python
from collections import Counter

counts = Counter(items)
```

- Do not use `items.count(x)` inside a loop (avoid quadratic scans).

Disallowed example:

```python
for x in items:
    if items.count(x) == 1:
        return x
```
