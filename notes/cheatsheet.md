# Cheatsheet (Coach-Owned)

This file stays short.
It records patterns you repeatedly use (in your own style), not a dump of APIs.

## Patterns

- Single-pass stats: initialize from first element, then update min/max/sum/count in one loop.
- Dict counting: use `if key in d:` (not `key in d.keys()`), and normalize once (e.g., lowercase) before counting.
- Line parsing: `for i, raw in enumerate(text.splitlines(), start=1): line = raw.strip();` then skip empty/comment, then parse.
- Debug hygiene: remove `print(...)` from solution code before final run; prefer raising helpful errors.
- Stack parsing: push opening tokens; on closing token, check top-of-stack matches then pop; fail on mismatch/empty; end requires empty stack.
- Grouping into dict-of-lists: create a list for a new key, otherwise append.
- Pytest stdout: prints are captured by default; use `pytest -s` (or `--capture=no`) when debugging with `print(...)`.
- Sorting with tie-breakers: use `sorted(..., key=...)` to encode primary + secondary ordering in one place.
- Dedupe + sort: `sorted(set(xs))` gives deterministic order.
- Preserve first-seen unique items: keep `seen = set()` for membership and append to a result list only on first sight.
- Avoid mutating input dicts: start with `out = start.copy()` (or `{**start}`) and modify `out`.
- Best-per-key update: for each key, replace stored value only when candidate is better (handle tie-break explicitly).
- Adjacent-pairs counting: loop `i` from `0..len(xs)-2` and count `key = (xs[i], xs[i+1])` in a dict.
- Reverse a dict safely: iterate `for k, v in d.items()`, check collision (`if v in out: raise ValueError`), otherwise assign `out[v] = k`.
- First nonrepeating: build counts in one pass, then scan original order to return first item with count 1.
- Two-sum exists: scan numbers, keep `seen` set; for each `x`, check if `target - x` is already seen.
- Merge two sorted lists: two pointers `i/j`, append smaller, then append the remaining tail.
- Canonical key grouping: compute a per-item signature (e.g., `"".join(sorted(word))`) and group by that key.
- Ordered membership filter: build `second_set = set(second)` once; keep `out` list + `added` set to preserve order while deduping.
- First duplicate: scan left-to-right with `seen` set; first item already in `seen` is the answer.
- Longest run: track `current_item/current_len` plus `best_len`, and update `best_len` as you scan.
- Merge intervals: sort by start, then sweep; merge when `next_start <= end + 1`, otherwise emit current range and start a new one.
- Range intersection: two pointers over sorted disjoint ranges; overlap is `lo = max(starts)`, `hi = min(ends)`; advance the one with smaller end.
- Total covered by ranges: sort, sweep merging overlaps/touches, and sum inclusive lengths: `end - start + 1`.
- Insert interval: single pass over sorted disjoint ranges; emit before, merge overlaps/touches with `new`, then emit after (O(n), no full sort).
- Subtract interval: for each range, emit left remainder `(s, remove_start-1)` if needed and right remainder `(remove_end+1, e)` if needed.

## Algorithmic Foundations track (started 2026-06-02)

- Binary search: pick a loop form (`while lo <= hi:` inclusive) and a `mid` rule; state the invariant in your head before writing the loop. For "first/last" position, do *not* return on match — keep shrinking `hi` (or `lo`) past it.
- Kadane's: a single pass; the running sum is "what's the best sum *ending* at this position?". If dropping the prefix is better, reset to the current value. All-negative inputs need `max(nums)` as the base.
- Sliding window, variable: the rule is "the left pointer only moves forward, never backward", and you need a `last_seen` (or similar) to know *where* to jump to. The same shape builds attention masks.
- Tree BFS: queue of upcoming nodes; record "current level size" before the inner loop, drain exactly that many, push children, advance. Don't try to do it recursively.
- Tree DFS recursion: the function's return value is "what I computed for this subtree"; the call site decides how to combine. Inorder of a BST returns sorted output — that's the same invariant `bisect` relies on.

## Patterns practiced (auto-derived from `progress.json`)

Counts are approximate; they assume one exercise per strategy and may double-count an exercise that practices multiple patterns. The point is coverage, not exact accounting.

### Done (26 exercises, 01_basics + 02_collections)

- Dicts and counting: ~10 exercises (`dict_counting`, `frequency_analysis`, `dict_grouping`, `dict_inversion`, `adjacent_pairs`, `dict_update`, `merge_logic`, `canonical_key`).
- Set membership and dedup: ~6 (`set_membership`, `set_intersection`, `order_preservation`, `two_pass_counting`).
- Single-pass accumulation: ~6 (`single_pass`, `single_pass_stats`, `min_max`, `run_length`).
- Sorting with custom keys / tie-breaks: ~4 (`sorting`, `sort_with_key`, `tie_break`).
- Intervals and ranges: ~5 (`interval_compaction`, `interval_merge`, `sweep`, `interval_ops`, `split_logic`).
- Two-pointer on arrays/lists: ~2 (`two_pointer`, `merge_algorithm`).
- Stack parsing: ~1 (`stack_parsing`).
- String and line processing: ~4 (`line_parsing`, `split_with_limit`, `split_tokenize`, `string_traversal`).
- Exception handling and input validation: ~4 (`exception_handling`, `input_validation`, `validation`, `merge_logic`).
- Not yet done (will start in 03_algorithmic_foundations): **binary search, Kadane, sliding window, recursion on trees, tree BFS/DFS, backtracking, DP 1-D / 2-D, heap / top-k, recursion on list-of-lists**.

### Coming (16 scaffolded in 03_algorithmic_foundations)

- Binary search and boundary-shrink: 2 (ex01, ex02).
- Two-pointer on sorted: 1 (ex03).
- Kadane / single-pass DP warmup: 1 (ex04).
- In-place partition and swap: 2 (ex05, ex08).
- Sliding window (fixed + variable): 2 (ex06, ex07).
- Tree BFS / DFS: 2 (ex09, ex10).
- Recursion on tree-like data: 2 (ex10, ex11).
- Backtracking (combinatorics): 1 (ex12).
- DP 1-D: 2 (ex13, ex14).
- DP 2-D: 1 (ex15).
- Heap / top-k streaming: 1 (ex16).

If a row above grows stale, the source of truth is `progress.json`: `completed[*].strategies` for done, `scaffolding[*].strategies` for coming. A 5-line Python query against that file gives exact counts.
