# Fixed-Size Sliding Window: Max Sum of Length-k Subarray

## What problem this solves

Find the contiguous subarray of length exactly `k` with the largest sum. A naive solution recomputes the sum of every length-`k` window from scratch, costing O(n*k). The sliding-window trick reuses the previous sum: a window slide is one subtraction and one addition, so the whole pass is O(n).

## Mental model

A "window" is a contiguous range `[i, i + k)`. To move from window `[i, i + k)` to `[i + 1, i + k + 1)`:

- Subtract the value leaving: `nums[i]`.
- Add the value entering: `nums[i + k]`.

So `new_sum = old_sum - nums[i] + nums[i + k]`.

You compute the sum of the first window directly (`sum(nums[:k])`), then iterate `i` from `0` to `len(nums) - k - 1`, updating the sum and tracking the maximum.

## Why it matters in real projects

- Fixed sliding windows show up in: rolling averages in monitoring, throughput over the last N seconds, top-N leaderboards refreshed on each event, and "average over the last 5 minutes" charts.
- Once you can do "fixed-size" sliding windows, the variable-size variant (next exercise) becomes a natural extension.

## Common pitfalls

### Recomputing the sum from scratch

- `sum(nums[i:i+k])` inside a loop is O(k) per window and O(n*k) total. The point of the exercise is the O(1) update.

### Initialising the running sum to 0 with all-negative input

- If you keep `best = 0`, an all-negative array will report `0` as the "max sum" — wrong. Initialise to `float("-inf")` or to the first window's sum.

### Off-by-one at the boundaries

- The number of windows is `len(nums) - k + 1`. If `k > len(nums)`, this is non-positive and you should raise.

### Forgetting the k = 0 case

- A window of size 0 has sum 0. This is degenerate but well-defined; the spec says it returns 0.

## Edge cases

- `k == 0` -> `0`.
- `k == 1` -> `max(nums)`.
- `k == len(nums)` -> `sum(nums)`.
- `k > len(nums)` -> raise `ValueError`.
- `len(nums) == 0` with `k > 0` -> raise `ValueError`.
- All-negative `nums`.
- Mix of positive and negative.

## Quick check

`nums = [1, 4, 2, 10]`, `k = 2`.

- Initial window `[0:2]` = `[1, 4]`. `cur = 5`, `best = 5`.
- Slide to `[1:3]` = `[4, 2]`. `cur = 5 - 1 + 2 = 6`. `best = 6`.
- Slide to `[2:4]` = `[2, 10]`. `cur = 6 - 4 + 10 = 12`. `best = 12`.
- Return `12`. ✓

## ML/research connection

The "subtract leaving, add entering" update is the same pattern as online streaming statistics (running mean, running variance, online quantiles via P² or t-digest) and the per-window aggregation in transformer attention — every step is one subtraction and one addition, not a full re-sum.
