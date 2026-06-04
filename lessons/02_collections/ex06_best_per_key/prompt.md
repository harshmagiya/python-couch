# ex06_best_per_key

Practice maintaining a “current best” per key in a single pass.

## Task

In `solution.py`, implement:

```python
def best_per_category(records: list[tuple[str, str, int]]) -> dict[str, tuple[str, int]]:
    ...
```

Each record is `(category, item, score)`.

Return a dictionary mapping each `category` to the best `(item, score)` according to:

- Primary: higher `score` wins
- Tie-breaker: smaller `item` in ascending lexicographic order wins

Rules:

- If `records` is empty, return `{}`.
- Treat strings exactly as given (case-sensitive).

## Examples

- `best_per_category([("fruit", "apple", 5), ("fruit", "banana", 7)])` -> `{ "fruit": ("banana", 7) }`
- `best_per_category([("x", "b", 2), ("x", "a", 2)])` -> `{ "x": ("a", 2) }`

## Constraints (for practice)

- Do not sort the full `records` list.

Disallowed example:

```python
records = sorted(records, key=lambda r: (r[0], -r[2], r[1]))
```
