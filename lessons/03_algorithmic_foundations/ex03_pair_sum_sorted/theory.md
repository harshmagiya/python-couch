# Two Pointers on a Sorted Array (Pair Sum)

## What problem this solves

Given a sorted array and a target, find two indices whose values sum to the target. Sorting buys you a property: a sum that's *too small* tells you which pointer to move, and so does a sum that's *too big*.

## Mental model

Maintain two pointers, one at each end: `l = 0`, `r = len(nums) - 1`. Compare the current sum to the target:

- If `nums[l] + nums[r] == target`: found it -> return `(l, r)`.
- If sum `< target`: the sum is too small. The only way to make it bigger is to move `l` right (toward larger values). `l += 1`.
- If sum `> target`: too big. Move `r` left (toward smaller values). `r -= 1`.
- If `l == r` and no match yet: no pair exists -> return `None`.

The two pointers converge, so the loop runs at most O(n) times. No extra memory.

## Why it matters in real projects

- Two-pointer on a sorted input is the workhorse of "find a pair / triple summing to X" problems, the merge step in merge sort, and many partitioning tasks.
- It contrasts directly with the hash-based "two-sum" pattern: that one works on *unsorted* input in O(n) time and O(n) space. The two-pointer version is O(n) time and O(1) space but requires sorted input. Knowing which to pick is the expert's call.

## Common pitfalls

### Wrong direction of movement

- "Sum too small" -> move `l` right (we need a bigger left value).
- "Sum too big"   -> move `r` left  (we need a smaller right value).
- Mixing these up produces wrong answers that may still pass simple tests.

### Allowing `i == j`

- The pair must use *two distinct* indices. The loop `while l < r:` (strict) enforces this naturally.

### Returning the first match by accident

- If the test expects a specific (i, j), check that the spec actually pins the order. In this exercise any valid pair is acceptable.

## Edge cases

- Empty input -> `None`.
- Single element -> `None` (no two distinct indices).
- Two elements summing to target.
- Two elements not summing to target.
- All-same array.
- Negative numbers (e.g., `target = 0` with `[-3, -1, 1, 3]` -> `(-3, 3)`).
- Target = 0 with `[0, 0]` -> `(0, 1)`.

## Quick check

`nums = [1, 2, 3, 4, 6]`, `target = 10`.

- l=0, r=4: 1+6 = 7 < 10 -> l=1.
- l=1, r=4: 2+6 = 8 < 10 -> l=2.
- l=2, r=4: 3+6 = 9 < 10 -> l=3.
- l=3, r=4: 4+6 = 10 == 10 -> return (3, 4). ✓

## ML/research connection

Underlies the inner loop of pair-scoring in re-ranking models (cross-encoders that score every candidate against a query), and the merge-style join step in dataframe libraries (pandas `merge_ordered`, polars `join_asof`) where the sorted-input property unlocks the O(n) variant.
