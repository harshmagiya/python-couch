# Mistakes (Coach-Owned)

Only record recurring or high-impact mistakes.
Each entry should include a concrete fix.

## Recurring

- Variable-name typos can silently break updates; rely on tests early and keep names consistent.

## Recurring (Quality)

- Leaving debug `print(...)` in final code; remove once you understand the bug.

## Watchlist (Not Yet Recurring)

- Unused imports add noise and hide intent; delete them as soon as you notice.
- Avoid `s += chunk` in a loop for large strings; build a list and `"".join(...)`.
- Be careful with "cleanup" transforms (e.g., removing all spaces) that can change meaning; prefer targeted `strip()` around tokens.
- Using bare `except:`; catch the specific exception (often `ValueError`) so real bugs aren't hidden.
- Avoid `k in d.keys()`; use `k in d`.
- Function returns `None` when you forget an explicit `return`; if a test says you returned `None`, verify every code path returns a value.
- `set` has no stable order; never return `list(set(xs))` when an ordered output is required (sort or preserve first-seen order explicitly).
- Repeated `x in some_list` checks inside a loop can go quadratic; switch to a `set`/`dict` for membership/counting.
