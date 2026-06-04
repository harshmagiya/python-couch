# ex03_parse_kv_lines

Practice parsing structured text into a dictionary.

## Task

In `solution.py`, implement:

```python
def parse_kv_lines(text: str) -> dict[str, str]:
    ...
```

Parse `text` as a sequence of lines.

Rules:

- Ignore empty lines.
- Ignore comment lines whose first non-space character is `#`.
- For data lines, the format is: `key = value` (the `=` must exist).
- Strip whitespace around `key` and `value`.
- Keys are case-sensitive.
- If the same key appears multiple times, the *last* one wins.

Errors:

- If a non-empty, non-comment line does not contain `=`, raise `ValueError`.
- If the key is empty after stripping (e.g., `"   =x"`), raise `ValueError`.

## Examples

- `parse_kv_lines("a=1\nb=2\n")` -> `{"a": "1", "b": "2"}`
- `parse_kv_lines("# hi\na = 1\na=2")` -> `{"a": "2"}`

## Constraints (for practice)

- Do not use regex in this exercise.
- Use `split("=", 1)` so values may contain `=`.
