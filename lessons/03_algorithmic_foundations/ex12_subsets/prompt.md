# ex12_subsets

Read: `theory.md` (2-3 minutes) before coding. Backtracking
(choose / don't-choose) is the workhorse of combinatorial generation.

## Task

In `solution.py`, implement:

```python
def subsets(nums: list[int]) -> list[list[int]]:
    ...
```

Behavior:

- `nums` contains *distinct* integers (the tests guarantee this).
- Return the **power set** of `nums`: the list of all subsets, including
  the empty set and `nums` itself.
- Result must be in **deterministic order**:
  1. Subsets are sorted by **length** (empty set first, full set last).
  2. Within each length, subsets are sorted **lexicographically**.
- The internal lists in the result are independent copies; mutating one
  must not affect the others.

## Examples

- `subsets([]) == [[]]`
- `subsets([1]) == [[], [1]]`
- `subsets([1, 2]) == [[], [1], [2], [1, 2]]`
- `subsets([3, 1, 2]) == [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]`
  (input is sorted internally first, then grouped by length)
- `subsets([-1, 0, 1]) == [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]`

## Complexity requirement

- The result has `2 ** len(nums)` subsets. Each subset must be built
  with O(k) work (where k is its size) so the total is O(n * 2^n).
- This is optimal — the output itself is already that size.

## Constraints (for practice)

- Use a backtracking / recursive "choose or don't-choose" pattern.
- No `itertools.combinations` (which is a one-liner that hides the
  recursion).
- No `functools` / stdlib "powerset" trick.
- Sort the input internally so output is deterministic regardless of
  input order.

## Disallowed examples

```python
from itertools import combinations
def subsets(nums):                          # WRONG: hides the recursion
    nums = sorted(nums)
    return [list(c) for k in range(len(nums) + 1) for c in combinations(nums, k)]
```

```python
def subsets(nums):                          # WRONG: bit-mask trick is fine in concept
    nums = sorted(nums)                     # but the prompt asks for backtracking
    n = len(nums)
    out = []
    for mask in range(1 << n):
        out.append([nums[i] for i in range(n) if mask & (1 << i)])
    return out
```
