# ex05_balanced_brackets

Practice stack-based parsing.

## Task

In `solution.py`, implement:

```python
def is_balanced(s: str) -> bool:
    ...
```

Return `True` if all brackets in `s` are balanced and properly nested.

Supported brackets: `()`, `[]`, `{}`.

Rules:

- Ignore all non-bracket characters.
- `""` (empty string) is balanced.

Examples:

- `is_balanced("([])")` -> `True`
- `is_balanced("([)]")` -> `False`
- `is_balanced("a + (b * [c])")` -> `True`
- `is_balanced("]")` -> `False`

## Constraints (for practice)

- Use a single pass.
- Do not use recursion.

Disallowed examples:

- Recursion (do not do this):

```python
def is_balanced(s: str) -> bool:
    # calls itself -> recursion
    return is_balanced(s[1:-1])
```
