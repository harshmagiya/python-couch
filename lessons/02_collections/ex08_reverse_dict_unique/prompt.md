# ex08_reverse_dict_unique

Practice iterating dict items and handling collisions.

## Task

In `solution.py`, implement:

```python
def reverse_dict_unique(d: dict[str, str]) -> dict[str, str]:
    ...
```

Return a new dictionary where keys and values are swapped.

Rules:

- Do not mutate `d`.
- If two different keys in `d` map to the same value, raise `ValueError`.
- Treat strings exactly as given (case-sensitive).
- Empty strings are allowed.
- If `d` is empty, return `{}`.

## Examples

- `reverse_dict_unique({"a": "x", "b": "y"})` -> `{ "x": "a", "y": "b" }`
- `reverse_dict_unique({"a": "x", "b": "x"})` -> raises `ValueError`

## Constraints (for practice)

- Do not use a dict comprehension.

Disallowed example:

```python
return {v: k for k, v in d.items()}
```
