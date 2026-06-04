# ex15_edit_distance

Read: `theory.md` (4-5 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def edit_distance(a: str, b: str) -> int:
    ...
```

Behavior:

- Return the **Levenshtein edit distance** between the two strings.
- The distance is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change `a` into `b`. Each edit has cost 1.
- If `a == b`, return `0`.
- If `a` is empty, return `len(b)` (insert each character of `b`).
- If `b` is empty, return `len(a)` (delete each character of `a`).

## Examples

- `edit_distance("", "") == 0`
- `edit_distance("abc", "abc") == 0`
- `edit_distance("", "abc") == 3`
- `edit_distance("abc", "") == 3`
- `edit_distance("kitten", "sitting") == 3` (k→s, e→i, insert g)
- `edit_distance("flaw", "lawn") == 2` (delete f, insert n — or substitute w↔n and rearrange)
- `edit_distance("intention", "execution") == 5`
- `edit_distance("a", "b") == 1`
- `edit_distance("ab", "ba") == 2` (delete+insert; you cannot swap in a single edit)

## Complexity requirement

- O(m * n) time, where m = len(a) and n = len(b).
- O(min(m, n)) extra space, using the **two-row rolling** trick. A full m*n matrix is *not* required.

## Constraints (for practice)

- Use the Wagner-Fischer 2-D DP. State: `dp[i][j]` = edit distance between `a[:i]` and `b[:j]`. Recurrence:

  ```
  if a[i-1] == b[j-1]:
      dp[i][j] = dp[i-1][j-1]                # no edit needed
  else:
      dp[i][j] = 1 + min(
          dp[i-1][j],     # delete a[i-1]
          dp[i][j-1],     # insert b[j-1]
          dp[i-1][j-1],   # substitute a[i-1] -> b[j-1]
      )
  ```

  Base row `dp[0][j] = j` and base column `dp[i][0] = i`.

- For the rolling-row form, keep only the previous row. The current cell `dp[i][j]` only depends on `dp[i-1][j-1]` (the diagonal) and `dp[i-1][j]` / `dp[i][j-1]` (the previous row's `j` and the current row's `j-1`).

- If you choose the "swap so the shorter string is the row" form, the space becomes O(min(m, n)).

## Disallowed examples

```python
def edit_distance(a, b):                            # WRONG: full m*n matrix
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
```

This is correct and O(m*n) time, but uses O(m*n) space. The prompt asks for the two-row rolling form, O(min(m, n)) space.

```python
def edit_distance(a, b):                            # WRONG: BFS / A* over edit graph
    from collections import deque
    if a == b:
        return 0
    q = deque([(a, 0)])
    seen = {a}
    while q:
        s, d = q.popleft()
        for nxt in _neighbors(s, b):
            if nxt == b:
                return d + 1
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, d + 1))
    return -1
```

BFS over the implicit edit graph is correct in principle but exponential in
practice (each string of length k has roughly 3k+1 single-character edits,
and the graph blows up). For non-trivial strings this will not finish
in time. Use the DP form.

## Hints

- The diagonal `dp[i-1][j-1]` becomes the "previous" diagonal as you iterate row by row. In the rolling form, you keep one extra scalar for the "previous diagonal" (called `prev_diag` in the code) and shift it as you move to the next column.
- Equivalently: keep two rows, `prev_row` and `curr_row`, and after each row, `prev_row = curr_row` and `curr_row = [0] * (n + 1)`.
- For O(min(m, n)) space, decide which string is the row and which is the column based on length. Pick the shorter string as the column so the rolling row is shorter.
