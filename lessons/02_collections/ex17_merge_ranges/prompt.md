# ex17_merge_ranges

Build on your `compact_ranges` thinking: merging intervals.

## Task

In `solution.py`, implement:

```python
def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ...
```

You are given a list of inclusive integer ranges `(start, end)`.

Return a new list of ranges where any overlapping **or touching** ranges are
merged, and the output is sorted by `start`.

Rules:

- If the input is empty, return `[]`.
- Input ranges may be unsorted.
- All input ranges are valid: `start <= end`.
- Two ranges should be merged if they overlap OR touch:
  - overlap: `next_start <= current_end`
  - touch: `next_start == current_end + 1`

## Examples

- `merge_ranges([(1, 3), (4, 4)])` -> `[(1, 4)]` (touching)
- `merge_ranges([(5, 7), (1, 3), (2, 6)])` -> `[(1, 7)]` (unsorted + overlap)

## Constraints (for practice)

- Do not "expand" ranges into a full list of numbers.
- Do not use a `set` to solve this.

Disallowed examples:

```python
# Don't do this.
nums = []
for a, b in ranges:
    nums.extend(range(a, b + 1))
```

```python
# Don't do this.
all_numbers = set(range(a, b + 1) for a, b in ranges)
```
