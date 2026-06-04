# ex11_flatten

Read: `theory.md` (2-3 minutes) before coding. Recursion on
tree-shaped data is one of the foundational patterns.

## Task

In `solution.py`, implement:

```python
def flatten(nested: list) -> list:
    ...
```

Behavior:

- `nested` is a list whose elements are either:
  - an `int` (or any non-list value, but the tests only use `int`), OR
  - another list, recursively with the same shape.
- Return a single flat list of all the `int` values, in the same order
  they appear during a depth-first traversal.

## Examples

- `flatten([]) == []`
- `flatten([1, 2, 3]) == [1, 2, 3]`
- `flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]`
- `flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]`
- `flatten([1, [2, 3], 4, [5, [6, 7]], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]`
- `flatten([[[1]], [[2]]]) == [1, 2]`

## Complexity requirement

- O(n) time where n is the total number of `int` values (and the
  number of list containers you traverse).
- The function is naturally recursive; no auxiliary data structure
  beyond the call stack is required.

## Constraints (for practice)

- Use recursion on the list-of-lists structure.
- No `itertools.chain.from_iterable` shortcut (which is a non-recursive
  one-liner for the *one-level* case and would still leave the deeper
  levels unhandled).

## Disallowed examples

```python
from itertools import chain
def flatten(nested):                          # WRONG: only handles one level
    return list(chain.from_iterable(
        item if isinstance(item, list) else [item]
        for item in nested
    ))
```

```python
def flatten(nested):                          # WRONG: non-recursive, loses inner levels
    out = []
    for item in nested:
        if isinstance(item, list):
            out += item
        else:
            out.append(item)
    return out
```
