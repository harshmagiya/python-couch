# ex01_number_summary

Implement a function that summarizes a list of numbers.

## Task

In `solution.py`, implement:

```python
def number_summary(nums: list[float]) -> dict[str, float | int] | None:
    ...
```

Behavior:

- If `nums` is empty, return `None`.
- Otherwise return a dict with keys:
  - `count` (int)
  - `min` (float)
  - `max` (float)
  - `mean` (float)

Rules:

- Do not use third-party libraries.
- Accept ints and floats in the list.
- `mean` should be a float (normal Python division).

## Examples

- `number_summary([2, 4, 6])` returns `{"count": 3, "min": 2.0, "max": 6.0, "mean": 4.0}`
- `number_summary([])` returns `None`

## Constraints (for practice)

- Use a single pass through the data for min/max/sum (no `min(nums)`/`max(nums)`/`sum(nums)` in this exercise).
