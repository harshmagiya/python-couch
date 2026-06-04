# Backtracking: All Subsets (Power Set)

## What problem this solves

Generate every subset of a list of distinct integers, in deterministic order (by length, then lexicographically). The power set is the basic combinatorial generation problem. Backtracking — try a choice, recurse, undo the choice — is the standard pattern for problems where you build a solution incrementally and the partial work is reusable.

## Mental model

Imagine the elements laid out in a row. To build a subset, walk left to right: at each element, you either *include* it or *skip* it.

The recursion looks like this (for each index `i` from `start` to end of the array):

1. Include `nums[i]`: append, recurse on `i + 1`, then pop (undo).
2. Skip `nums[i]`: recurse on `i + 1` without appending.

The base case is "no more elements" — record the current subset.

A common way to enforce the **length-ascending, lex-ascending** output order is to drive the recursion by a target length `k`:

- For `k = 0, 1, 2, ..., n`:
  - Generate every subset of length exactly `k` by walking the sorted
    input and choosing one element at a time.
  - Within a single `k`, iterating `i` from `start` to `n` in order
    naturally produces lex-sorted output.

Sort the input first so "lex" is well-defined regardless of caller order.

## Why it matters in real projects

- The same backtracking pattern generates permutations, combinations, parenthesizations, valid Sudoku boards, and word-search solutions.
- "Sort the input, iterate in order" is the simplest way to make a combinatorial generator's output deterministic; deterministic output is essential for tests, snapshot files, and reproducible experiments.

## Common pitfalls

### Forgetting to copy before appending

- If you do `out.append(current)`, every subset ends up referring to the *same* list. Append `current[:]` (a copy).

### Output order

- The simplest reliable order: sort the input, then generate by length, then within each length by lex. A single-pass backtracking that does "include or skip" can produce subsets in *insertion* order, which is *not* length-sorted.

### Distinct-int assumption

- The prompt says `nums` is distinct. If you were to handle duplicates, you'd skip picking the same value at the same recursion depth (the "skip duplicates" trick in subset-with-dupes). Not needed here.

### Using `itertools.combinations`

- It works, but the prompt bans it for the same reason `bisect` is banned in earlier exercises: the point is to practise the pattern.

## Edge cases

- Empty input -> `[[]]` (one subset: the empty set).
- Single element -> `[[], [1]]`.
- Two elements.
- Three or more, with negative numbers and zero.

## Quick check

`nums = [1, 2, 3]` (already sorted).

- k=0: only `[]`.
- k=1: pick 1, pick 2, pick 3 -> `[[1], [2], [3]]`.
- k=2: pick 1+2, 1+3, 2+3 -> `[[1, 2], [1, 3], [2, 3]]`.
- k=3: pick 1+2+3 -> `[[1, 2, 3]]`.

Total: `[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]`. ✓

## ML/research connection

Power-set generation is the inner pattern of feature-subset selection in AutoML (Boruta-style feature ranking, recursive feature elimination) and of combinatorial hyperparameter search over discrete grids. The "sort the input, iterate in order" trick for deterministic output is also how you'd write any reproducible combinatorial generator used in tests or snapshot files.
