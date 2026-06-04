# Binary Search: First and Last Position

## What problem this solves

Given a sorted array and a target, return the *smallest* index and the *largest* index where the target occurs, or `(-1, -1)` if it doesn't. This is the natural follow-up to "any index": you usually want the *range* of equal values, not just one of them.

## Mental model

You can solve this with **two separate binary searches**, one tuned for "first" and one for "last". The key idea is to *not* return on the first match; instead, *keep searching* in a specific direction even when you find the target.

### Variant A: lower-bound (first position)

Find the smallest index `i` such that `arr[i] >= target`. After the search:

- If `i == len(arr)` or `arr[i] != target`, the target is absent.
- Otherwise `i` is the first position.

In the loop, when `arr[mid] == target`, **keep going left** by setting `hi = mid - 1` instead of returning.

### Variant B: upper-bound (last position)

Find the smallest index `i` such that `arr[i] > target`. Then `last = i - 1`. Equivalently: when `arr[mid] == target`, keep going right by setting `lo = mid + 1`.

The two variants differ in **only one line** of the binary search. That is the point of this exercise.

## Why it matters in real projects

- "Range of equal values" is the basic query behind SQL `BETWEEN`, group-by, histogram bin lookups, and time-range queries.
- The `bisect` module exposes these two as `bisect_left` and `bisect_right`. Knowing how to write them by hand means you can apply the idea in any language, including ones without a standard library equivalent.

## Common pitfalls

### Returning on the first match (not what you want here)

- The most common bug is `if arr[mid] == target: return mid` followed by normal halving. That gives a *valid* index but not the *first* one. To get the first, you must keep moving `hi = mid - 1` past the match.

### Off-by-one when the target is at the boundary

- If `target` is smaller than every element, the lower-bound search returns `0` immediately. You must still check `arr[0] == target` to decide "absent vs. present at the start".
- If `target` is larger than every element, the lower-bound search returns `len(arr)`. That's the "absent" signal.

### Mixing up the two variants

- "First" uses `hi = mid - 1` on match.
- "Last"  uses `lo = mid + 1` on match.
- Drawing the two side by side and writing the loop out is faster than guessing.

## Edge cases

- Empty array -> `(-1, -1)`.
- Single element, present and absent.
- Target appears once -> `(i, i)`.
- Target fills the array -> `(0, len(arr) - 1)`.
- Target is smaller than all, larger than all.
- Negative numbers.

## Quick check

`arr = [1, 2, 2, 2, 3, 4]`, `target = 2`.

- First: lower-bound search for `>= 2` -> `i = 1`. Check `arr[1] == 2`. Yes -> first = 1.
- Last: upper-bound search for `> 2` -> `i = 4`. last = `4 - 1 = 3`.
- Return `(1, 3)`. ✓

## ML/research connection

The two boundary-shrink variants are exactly what `numpy.searchsorted(arr, v, side='left' | 'right')` computes, and they are the inner step of `pandas.merge_asof` for nearest-match joins on sorted timestamps (e.g. joining a stream of irregular measurements onto a regular grid).
