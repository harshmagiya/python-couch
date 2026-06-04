# 1-D Dynamic Programming: Longest Increasing Subsequence (LIS)

## What problem this solves

Given a sequence of numbers, find the length of the longest subsequence (not necessarily contiguous) that is strictly increasing. The O(n²) DP form is the natural 2-D iteration over a 1-D state; the O(n log n) "patience sorting" form is the optimal version that uses binary search to maintain a sorted array of "smallest tail" values. The O(n²) form is what this exercise asks for; the O(n log n) form is in `theory.md` for context.

## Mental model (O(n²) DP)

`dp[i]` = the length of the longest strictly increasing subsequence that **ends at index `i`** (i.e. `nums[i]` is the last element of that subsequence).

Base: `dp[i] = 1` for every `i` (a single element is a strictly increasing subsequence of length 1).

Recurrence: for every `i`, look at every `j < i`. If `nums[j] < nums[i]`, you can extend the LIS ending at `j` by `nums[i]`, giving a candidate of `dp[j] + 1`. Take the max over all such `j`:

```
dp[i] = 1
for j in range(i):
    if nums[j] < nums[i]:
        dp[i] = max(dp[i], dp[j] + 1)
```

Answer: `max(dp)` (not `dp[-1]`, which is only correct if the LIS happens to end at the last element).

## The O(n log n) upgrade (for context, not required here)

Maintain a sorted array `tails` where `tails[k]` is the smallest possible tail value of an increasing subsequence of length `k + 1`. For each `nums[i]`, binary-search for the smallest `k` such that `tails[k] >= nums[i]`, and either replace `tails[k]` (extending) or append (new longest). The length of `tails` at the end is the LIS length. This is O(n log n) because the binary search is O(log n) and you do it `n` times.

The O(n²) DP form is what the prompt asks for. The O(n log n) form is mentioned for completeness and is a useful later exercise.

## Why it matters in real projects

- LIS is the workhorse of "longest monotone subsequence" queries, which show up in time-series analysis (longest stretch of monotonically increasing values, useful as a feature or a regime detector).
- The patience-sorting variant is also how some `k-NN`-style data structures work, and the same "smallest tail" trick appears in patience sorting for the patience-diff algorithm used in version control bisects.
- The O(n²) DP shape generalises to "longest common subsequence" (next extension exercise), "longest path in DAG" (where you do a topological sort and run the same DP), and many production scheduling problems.

## Common pitfalls

### Returning `dp[-1]` instead of `max(dp)`

This is the most common bug. The LIS does not necessarily end at the last element. For example, in `[10, 9, 2, 5, 3, 7, 101, 18]`, the LIS is `[2, 3, 7, 18]`, which ends at index 7 (the last element, OK). But in `[1, 3, 2, 4]`, the LIS is `[1, 2, 4]`, length 3, which ends at index 3. If you had `[1, 3, 2]`, the LIS is `[1, 2]` or `[1, 3]`, length 2, ending at index 2. In general, return `max(dp)`.

### Using `nums[j] <= nums[i]` (non-strict) instead of `<` (strict)

The prompt says "strictly increasing". `nums[j] < nums[i]` enforces that. A common off-by-one in the comparison.

### Off-by-one in the `dp` initialisation

`dp[i] = 1` (the subsequence consisting of just `nums[i]`). If you start with `dp[i] = 0`, every value will be one too small.

### Exponential recursion

The recursive shape "extend any earlier element that is smaller, recurse" is correct but exponential. The DP form computes each `dp[i]` once.

### Forgetting the empty-list case

`lis([]) == 0`. With `nums = []`, the inner loop doesn't run, `dp` is empty, `max(dp)` would crash. The empty-list case must be handled before the DP.

## Edge cases

- Empty list -> `0`.
- Single element -> `1`.
- All-same (`[2, 2, 2]`) -> `1` (no two elements are strictly increasing).
- Already strictly increasing -> `len(nums)`.
- Strictly decreasing -> `1` (every element is its own subsequence).
- Mix of positive, negative, and zero.
- A list with one "anomaly" inside an otherwise increasing sequence.

## Quick check

`nums = [10, 9, 2, 5, 3, 7, 101, 18]`.

- dp[0] = 1
- dp[1]: j=0, 10 < 9? no. dp[1] = 1.
- dp[2]: j=0, 10 < 2? no. j=1, 9 < 2? no. dp[2] = 1.
- dp[3]: j=0, 10 < 5? no. j=1, 9 < 5? no. j=2, 2 < 5? yes -> dp[3] = max(1, 1 + 1) = 2.
- dp[4]: j=0..1, no. j=2, 2 < 3? yes -> dp[4] = 2. j=3, 5 < 3? no. dp[4] = 2.
- dp[5]: j=0..1, no. j=2, 2 < 7? yes -> 2. j=3, 5 < 7? yes -> dp[3] + 1 = 3. j=4, 3 < 7? yes -> 3. dp[5] = 3.
- dp[6]: j=0..1, no. j=2, 2 < 101? yes -> 2. j=3, 5 < 101? yes -> 3. j=4, 3 < 101? yes -> 3. j=5, 7 < 101? yes -> dp[5] + 1 = 4. dp[6] = 4.
- dp[7]: j=0..1, no. j=2, 2 < 18? yes -> 2. j=3, 5 < 18? yes -> 3. j=4, 3 < 18? yes -> 3. j=5, 7 < 18? yes -> 4. j=6, 101 < 18? no. dp[7] = 4.

`max(dp) = 4`. ✓ (e.g. `[2, 5, 7, 18]` or `[2, 3, 7, 18]` or `[2, 3, 7, 101]`.)

## ML/research connection

LIS is the workhorse of "longest monotone subsequence" queries, which show up in time-series analysis (longest stretch of monotonically increasing values, useful as a feature or a regime detector) and in some chain-finding algorithms. The DP recurrence `dp[i] = max(dp[j] + 1)` over `j < i` is the same shape as longest-path-in-a-DAG, which appears in the inner loop of some planning and reinforcement-learning algorithms.
