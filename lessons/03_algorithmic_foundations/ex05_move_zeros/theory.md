# In-Place Partition: Move Zeros to the End (Stable)

## What problem this solves

Rearrange a list so that all zeros are at the end, while the non-zero elements keep their original relative order. This is the "stable partition" operation: separating "keep" and "discard" groups in one linear pass, in place, with O(1) extra memory.

## Mental model

Two pointers walk the list from left to right:

- `read`  - scans every element.
- `write` - points to the position where the next non-zero element should be placed.

For each element:

- If `nums[read] != 0`: copy it to `nums[write]`, then `write += 1`.
- If `nums[read] == 0`: do nothing; it will be overwritten later.

After the scan, positions `[write, len(nums))` still hold the *original* values that were there. Fill them with zeros.

```
before: [0, 1, 0, 3, 12]
read=0 (0): skip
read=1 (1): write=0, copy 1. [1,1,0,3,12], write=1
read=2 (0): skip
read=3 (3): write=1, copy 3. [1,3,0,3,12], write=2
read=4 (12): write=2, copy 12. [1,3,12,3,12], write=3
fill [3..5] with 0: [1,3,12,0,0]
```

## Why it matters in real projects

- Stable partition is the core of in-place quicksort, Dutch national flag, and many layout/rendering passes (e.g. "move all hidden widgets to the bottom of the layout").
- The two-pointer pattern here is the same one used for removing duplicates in place, moving even/odd numbers, and "compact" operations in databases.

## Common pitfalls

### Building a new list

- A list comprehension or a second list is O(n) extra space, defeating the point. The algorithm above only uses two integer pointers.

### Confusing "in-place" with "return a new list"

- The function must *mutate* the input list. Tests check `result is nums`. A return like `return [x for x in nums if x != 0] + [0] * zeros_count` returns a *new* list and the assertion `result is nums` fails.

### Stability

- Relative order of non-zero elements must be preserved. A naive "swap-with-end" approach loses that. The two-pointer copy approach is naturally stable because it processes elements in original order.

### Forgetting the trailing-zero fill

- After the scan, positions `[write, len(nums))` may still hold non-zero values from before — for example, when zeros are interleaved, the leftover tail of the original list can still have non-zeros that got *bypassed* by `write`. Always finish with `for i in range(write, len(nums)): nums[i] = 0` (or equivalent).

## Edge cases

- Empty list -> `[]`.
- All zeros -> unchanged.
- No zeros  -> unchanged.
- Single zero at start, middle, end.
- Already arranged (zeros already at end).
- Negative numbers mixed with zeros.

## Quick check

`nums = [0, 1, 0, 3, 12]` -> `[1, 3, 12, 0, 0]`. Verified above.

## ML/research connection

The stable two-pointer partition is the core of in-place quicksort, and the same "read/write" pointer pattern is used in streaming aggregation buffers (e.g. shuffling in-place to compact active vs. evicted entries) and in some feature-engineering passes that need to reorder a tensor without allocating.
