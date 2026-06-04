# ex04_read_int_lines

Practice file I/O + parsing + good errors.

## Task

In `solution.py`, implement:

```python
from pathlib import Path


def read_int_lines(path: Path) -> list[int]:
    ...
```

Read a UTF-8 text file and return a list of integers.

Rules:

- Ignore empty lines.
- Ignore comment lines whose first non-space character is `#`.
- For data lines:
  - strip leading/trailing whitespace
  - parse as a base-10 integer (allow leading `+`/`-`)

Errors:

- If a data line cannot be parsed as an int, raise `ValueError` with a helpful message that includes the 1-based line number.

## Examples

If the file contains:

```text
# counts
10
 -3

7
```

Then `read_int_lines(...)` returns `[10, -3, 7]`.

## Constraints (for practice)

- Do not use regex.
- Do not use `eval`.
