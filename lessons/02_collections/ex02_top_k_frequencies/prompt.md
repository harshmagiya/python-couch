# ex02_top_k_frequencies

Practice frequency counting + sorting.

## Task

In `solution.py`, implement:

```python
def top_k_frequencies(items: list[str], k: int) -> list[tuple[str, int]]:
    ...
```

Return the `k` most frequent items as a list of `(item, count)` pairs.

Ordering rules:

- Primary: higher count first
- Tie-breaker: item in ascending lexicographic order

Rules:

- If `k <= 0`, return `[]`.
- If `k` is larger than the number of distinct items, return all distinct items.

## Examples

- `top_k_frequencies(["a", "b", "a"], 1)` -> `[("a", 2)]`
- `top_k_frequencies(["b", "a", "b", "a"], 2)` -> `[("a", 2), ("b", 2)]`  (tie broken by item)

## Constraints (for practice)

- Do not use `collections.Counter`.

Disallowed example:

```python
from collections import Counter

counts = Counter(items)
```
