# ex07_bigram_frequencies

Practice using tuples as dictionary keys.

## Task

In `solution.py`, implement:

```python
def bigram_frequencies(words: list[str]) -> dict[tuple[str, str], int]:
    ...
```

Return a dictionary mapping each consecutive word pair (bigram) to its count.

A bigram is formed from adjacent items:

- `(words[0], words[1])`, `(words[1], words[2])`, ...

Rules:

- If `words` has fewer than 2 items, return `{}`.
- Treat strings exactly as given (case-sensitive).

## Examples

- `bigram_frequencies(["a", "b", "a"])` -> `{("a", "b"): 1, ("b", "a"): 1}`
- `bigram_frequencies(["x", "x", "x"])` -> `{("x", "x"): 2}`

## Constraints (for practice)

- Do not use `collections.Counter`.

Disallowed example:

```python
from collections import Counter

return dict(Counter(zip(words, words[1:])))
```

- Do not use `itertools.pairwise`.

Disallowed example:

```python
from itertools import pairwise

for a, b in pairwise(words):
    ...
```
