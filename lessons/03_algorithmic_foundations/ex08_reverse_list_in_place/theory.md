# In-Place Reversal: Two-Pointer Swap at the Ends

## What problem this solves

Reverse a list without allocating a new list. The list type already has `nums.reverse()` and the slice `nums[::-1]`, but the exercise is about *practising* the head/tail pointer swap. That swap is the building block for in-place linked-list reversal, palindrome checks, and many partitioning problems.

## Mental model

Two pointers: `l = 0` at the start, `r = len(nums) - 1` at the end. While `l < r`, swap `nums[l]` and `nums[r]`, then `l += 1` and `r -= 1`. When the pointers cross, the list is reversed.

```
[1, 2, 3, 4]
 l        r  swap  -> [4, 2, 3, 1]
    l  r     swap  -> [4, 3, 2, 1]
       lr            stop
```

## Why it matters in real projects

- Pointer-swap reversal is the prototype for: palindrome check, rotating a list by `k`, partitioning around a pivot (quicksort), and reversing a contiguous slice in place.
- The same loop, with one extra line (`if cond: nums[l], nums[r] = nums[r], nums[l]`), generalises to Dutch national flag and the "move zeros / move evens" partitions.

## Common pitfalls

### Returning a new list

- `nums[::-1]` or `list(reversed(nums))` return a new list. The function must *mutate* the input. The test asserts `result is nums`.

### Forgetting to update the pointers

- A `while True: swap` loop with no `l += 1 / r -= 1` would swap the same two elements forever. The pointers must move inward.

### Off-by-one on the loop condition

- `while l < r:` (strict) handles every case: empty, single, even, odd. When `l == r`, you're at the middle of an odd-length list and there's nothing to swap.

### Returning `None` (or the result of `nums.reverse()`)

- `list.reverse()` returns `None` and mutates in place. Writing `return nums.reverse()` is a bug. The prompt bans this for the deeper reason too: the exercise is the algorithm, not the one-liner.

## Edge cases

- Empty list.
- Single element.
- Two elements.
- Even length (4, 6).
- Odd length (3, 5).
- All-same (`[7, 7, 7, 7]`) — swap test still passes.
- Negative numbers.
- A list of length 1 with a single element of value 0.

## Quick check

`nums = [1, 2, 3, 4]`.

- l=0, r=3: swap -> [4, 2, 3, 1]; l=1, r=2.
- l=1, r=2: swap -> [4, 3, 2, 1]; l=2, r=1.
- Stop. Return `nums` (the same object, now `[4, 3, 2, 1]`). ✓

## ML/research connection

The head/tail swap is interview practice; production code uses `np.flip`/`tensor.flip` which hide the swap. The same loop, with an extra condition (`if cond: nums[l], nums[r] = nums[r], nums[l]`), generalises to Dutch national flag and to stable partitions (e.g. "move all padding tokens to the right" inside a batched sequence tensor).
