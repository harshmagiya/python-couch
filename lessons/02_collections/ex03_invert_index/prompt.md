# ex03_invert_index

Practice building a dictionary where each key maps to a collection you later sort.

## Recall (no code)

- How do you check whether a key exists in a dict?
- What does `sorted(...)` return?

## Task

In `solution.py`, implement:

```python
def invert_index(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    ...
```

Given a list of `(user, tag)` pairs, return a dictionary mapping each `tag` to a list of users who have that tag.

Rules:

- Each tag's user list must contain each user at most once (deduplicate duplicates in the input).
- Each tag's user list must be sorted in ascending lexicographic order.
- Treat strings exactly as given (case-sensitive).
- Empty strings are allowed for both `user` and `tag`.
- If `pairs` is empty, return `{}`.

## Examples

- `invert_index([("alice", "p1"), ("bob", "p1"), ("alice", "p2")])` -> `{ "p1": ["alice", "bob"], "p2": ["alice"] }`
- `invert_index([("a", "x"), ("a", "x"), ("b", "x")])` -> `{ "x": ["a", "b"] }`

## Constraints (for practice)

- Do not use `collections.defaultdict`.

Disallowed example:

```python
from collections import defaultdict

d = defaultdict(set)
for user, tag in pairs:
    d[tag].add(user)
```

- Do not use `dict.setdefault`.

Disallowed example:

```python
d = {}
for user, tag in pairs:
    d.setdefault(tag, set()).add(user)
```
