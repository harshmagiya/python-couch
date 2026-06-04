# Kadane's Algorithm: Maximum Subarray Sum

## What problem this solves

Given a list of (possibly negative) integers, find the contiguous subarray with the largest sum. The naive O(n²) approach enumerates all `(i, j)` pairs and takes the max; Kadane's algorithm does it in one pass with O(1) extra space. The pattern is the simplest 1-D dynamic-programming warmup you'll ever meet, and it generalises directly to many "best window in a sequence" questions in signal processing, time-series, and online statistics.

## Mental model

Walk left to right. At each position `i`, you keep one scalar:

- `cur` — the best sum of a subarray that **ends at** position `i`.

The update rule is the heart of the algorithm:

```
cur = max(nums[i], cur + nums[i])
```

Two options at position `i`:

1. **Extend the previous subarray** by adding `nums[i]` to `cur`. This is good when `cur` is positive (extending helps).
2. **Start fresh** from `nums[i]`. This is good when `cur` is negative (extending drags you down; better to start over).

The best sum seen so far is tracked separately:

```
best = max(best, cur)
```

After the loop, `best` is the answer.

## Why O(1) space

You never need to look back more than one step. The "best sum ending at position i" only depends on the "best sum ending at position i-1" and `nums[i]`. So a single scalar `cur` suffices — no array, no DP table.

## Why it matters in real projects

- Streaming anomaly detection: given a time series of signed residuals (positive = above baseline, negative = below), the longest "above-baseline streak" is a Kadane-style question.
- Rolling signal analysis: the "max energy in any contiguous window" of a 1-D signal.
- The 1-D DP pattern generalises to "best subarray with a twist" — minimum-size subarray with sum >= K (sliding window variant), max-sum subarray with at most K distinct elements, etc.

## Common pitfalls

### Initialising `cur` to 0 with all-negative input

The most common bug. If you do `cur = 0; for x in nums: cur = max(x, cur + x)`, then on an all-negative input you will return `0` (or skip the loop entirely) instead of the largest element. The correct base is `cur = nums[0]`. After the first element, the recurrence takes over.

### Initialising `best` to 0 with all-negative input

Same trap. `best = 0` is wrong; use `best = nums[0]` and update from the first iteration onward.

### Returning `cur` instead of `best`

`cur` is the best sum *ending at the last position*. `best` is the best sum *anywhere*. They are equal only if the last position is also the best position, which is not always the case (e.g. `[-1, 2, -1]` has `cur = 1` at the end but `best = 2` from the middle). Return `best`.

### Forgetting the empty-list case

Empty input has no non-empty subarray, so the answer is undefined. Raise `ValueError` (matches the convention used in earlier exercises like `max_sum_subarray_k`).

### Reading the value of `cur` *before* the update

Order of operations matters. The recurrence is "look at the previous `cur`, then update". A mix-up here is subtle and only shows up on certain inputs.

## Edge cases

- Empty list -> `ValueError`.
- Single element -> that element.
- All positive -> the whole array.
- All negative -> the largest (least-negative) single element.
- Mix of positive and negative.
- A single positive in a sea of negatives.
- Zeros mixed in (zero neither helps nor hurts, but be careful not to "skip" it via the wrong update).

## Quick check

`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`.

- i=0: cur = max(-2, -2) = -2; best = -2.
- i=1: cur = max(1, -2 + 1) = 1; best = 1.
- i=2: cur = max(-3, 1 + -3) = -2; best = 1.
- i=3: cur = max(4, -2 + 4) = 4; best = 4.
- i=4: cur = max(-1, 4 + -1) = 3; best = 4.
- i=5: cur = max(2, 3 + 2) = 5; best = 5.
- i=6: cur = max(1, 5 + 1) = 6; best = 6.
- i=7: cur = max(-5, 6 + -5) = 1; best = 6.
- i=8: cur = max(4, 1 + 4) = 5; best = 6.

Return 6. ✓

## ML/research connection

Maximum subarray sum is the inner pattern in signal-processing anomaly detection (longest interval of positive cumulative signal vs noise) and in scoring windows over time-series features — the "best window in a sequence" question that comes up any time you have a 1-D stream and want to find the most "active" contiguous stretch.
