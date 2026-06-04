# ex01_group_by_length

Practice building dictionaries of lists.

## Task

In `solution.py`, implement:

```python
def group_by_length(words: list[str]) -> dict[int, list[str]]:
    ...
```

Return a dictionary mapping word length to the list of words with that length, preserving the original order within each length group.

Rules:

- Treat words exactly as given (case-sensitive).
- Include empty strings (length 0) if present.
- If `words` is empty, return `{}`.

## Examples

- `group_by_length(["a", "to", "b", "cat"])` -> `{1: ["a", "b"], 2: ["to"], 3: ["cat"]}`
- `group_by_length(["", "x", ""])` -> `{0: ["", ""], 1: ["x"]}`

## Constraints (for practice)

- Do not use `collections.defaultdict` in this exercise.

Disallowed example:

```python
from collections import defaultdict

d = defaultdict(list)
for w in words:
    d[len(w)].append(w)
```
