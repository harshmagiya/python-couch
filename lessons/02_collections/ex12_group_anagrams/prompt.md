# ex12_group_anagrams

Practice using a dictionary with a computed canonical key.

## Task

In `solution.py`, implement:

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    ...
```

Group words that are anagrams of each other.

Definitions:

- Two words are anagrams if sorting their characters gives the same sequence.
- Comparison is case-sensitive.

Output rules:

- Return a list of groups (each group is a list of strings).
- Order of groups: the group appears when its first member appears in the input.
- Order within a group: preserve the original left-to-right order from `words`.
- If `words` is empty, return `[]`.

## Examples

- `group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])` -> `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`
- `group_anagrams(["a", "A"])` -> `[["a"], ["A"]]`

## Constraints (for practice)

- Do not use `collections.defaultdict`.

Disallowed example:

```python
from collections import defaultdict

groups = defaultdict(list)
```

- Do not sort the full `words` list.

Disallowed example:

```python
words = sorted(words)
```
