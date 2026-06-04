# Binary Search: Index of Target

## What problem this solves

Given a sorted array and a target value, find the target's position (or report it's missing) in logarithmic time. This is the workhorse for dictionary lookups, database indexes, version-control bisects, and "first timestamp after t" queries.

## Mental model

You maintain a search range `[lo, hi]` over the sorted array. Each iteration:

1. Look at the middle element `arr[mid]`.
2. If it equals `target`, you found it -> return `mid`.
3. If it's less than `target`, the target (if present) is in the right half: `lo = mid + 1`.
4. If it's greater, the target is in the left half: `hi = mid - 1`.

The range strictly shrinks each iteration, so you reach an answer (or exhaust the array) in O(log n) steps.

## Why it matters in real projects

- Sorted arrays are everywhere: log files, time series, sorted index keys, calendar slots.
- A linear scan in a sorted context is almost always a missed optimization.
- Binary search trains the **loop invariant** mindset: know what is true *before*, *during*, and *after* each iteration.

## Common pitfalls

### Off-by-one in the loop condition

- `while lo <= hi:` (inclusive range) and `while lo < hi:` (left-closed, right-open) both work, but they have different exit conditions and different `mid` math. Pick one and be consistent.
- `mid = (lo + hi) // 2` is correct for normal input sizes in Python. In C/Java you would use `lo + (hi - lo) // 2` to avoid overflow.

### Returning as soon as you find the target is fine ONLY for "any index"

- The next exercise (`first_and_last`) is the one that needs an *exact* index even with duplicates. This exercise accepts any valid index.

### The empty-array case

- `lo = 0, hi = -1` must exit the loop and return `-1`. The `while lo <= hi` form handles this naturally: `0 <= -1` is false, so the loop body never runs.

### Confusing "move the right pointer" with "move the left pointer"

- When `arr[mid] < target`: shrink the left side OUT -> `lo = mid + 1`.
- When `arr[mid] > target`: shrink the right side OUT -> `hi = mid - 1`.
- Drawing a 5-element array and tracing on paper cements this faster than reading.

## Edge cases

- Empty array.
- Single-element array, target present and absent.
- Target at the very start or very end.
- Target smaller than all elements, larger than all elements.
- Negative numbers.

## Quick check

For `arr = [1, 3, 5, 7, 9]`, `target = 7`:

- Step 1: `lo=0, hi=4, mid=2, arr[2]=5`. `5 < 7` -> `lo = 3`.
- Step 2: `lo=3, hi=4, mid=3, arr[3]=7`. Match! Return `3`.

Two steps for a 5-element array. log2(5) ~= 2.3. ✓

## ML/research connection

Used inside sklearn's `DecisionTreeClassifier.best_split` to find the best feature threshold in O(log n) per node — a sorted array of candidate thresholds is binary-searched at every node, so the algorithm is the difference between an interactive tree-training run and a slow one.
