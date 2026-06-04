# ex19_total_covered

Compose previous patterns: merge ranges, then compute total coverage.

## Task

In `solution.py`, implement:

```python
def total_covered(ranges: list[tuple[int, int]]) -> int:
    ...
```

You are given a list of inclusive integer ranges `(start, end)`.

Return the total number of **distinct integers** covered by the union of these
ranges.

Rules:

- If the input is empty, return `0`.
- Input may be unsorted.
- Ranges may overlap or touch.
- All input ranges are valid: `start <= end`.

Examples:

- `total_covered([(1, 3), (5, 5)])` -> `4` (covers 1,2,3,5)
- `total_covered([(1, 3), (3, 6)])` -> `6` (covers 1..6)

## Constraints (for practice)

- Do not expand ranges into a list of numbers.
- Do not use a `set` to build the union.

Disallowed examples:

```python
# Don't do this.
nums = []
for a, b in ranges:
    nums.extend(range(a, b + 1))
return len(set(nums))
```
