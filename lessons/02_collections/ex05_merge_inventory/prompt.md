# ex05_merge_inventory

Practice updating a dictionary from a stream of events.

## Task

In `solution.py`, implement:

```python
def merge_inventory(start: dict[str, int], changes: list[tuple[str, int]]) -> dict[str, int]:
    ...
```

You are given:

- `start`: current inventory counts (item -> count)
- `changes`: a list of `(item, delta)` adjustments, in order

Return a new dictionary representing the final inventory after applying all deltas.

Rules:

- Do not mutate `start`.
- Applying a change means: `count = previous_count + delta`.
- Items not present in `start` start at `0`.
- If a final count is `0`, omit that item from the returned dict.
- Negative counts are allowed (this is intentional).

## Examples

- `merge_inventory({"a": 2}, [("a", 3), ("b", 1)])` -> `{ "a": 5, "b": 1 }`
- `merge_inventory({"a": 2}, [("a", -2)])` -> `{}`

## Constraints (for practice)

- Do not use `collections.Counter`.

Disallowed example:

```python
from collections import Counter

out = Counter(start)
out.update(dict(changes))
```

- Do not use `dict.get`.

Disallowed example:

```python
out[item] = out.get(item, 0) + delta
```
