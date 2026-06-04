# ex03_clip_outliers

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def clip_outliers(
    x: list[float],
    low_pct: float = 5.0,
    high_pct: float = 95.0,
) -> list[float]:
    ...
```

Behavior:

- `x` is a 1-D list of floats. `low_pct` and `high_pct` are in `[0, 100]`
  with `low_pct <= high_pct`.
- Compute the `low_pct`-th and `high_pct`-th percentiles of `x`.
  Return a new list where every value `<` the low percentile is
  replaced with the low percentile, and every value `>` the high
  percentile is replaced with the high percentile. Values strictly
  inside the range are unchanged.
- Values exactly equal to a percentile are kept as-is (the comparison
  is strict: `<` and `>`).
- If `len(x) == 0`, raise `ValueError`.
- If `low_pct > high_pct`, raise `ValueError`.

## Examples

- `clip_outliers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])` with defaults
  `low_pct=5, high_pct=95` -> the 5th and 95th percentiles are
  approximately `1.45` and `9.55`. The output is unchanged in the
  interior; the only values that would be clipped are values below
  `1.45` (none here) or above `9.55` (none here). The list is returned
  unchanged.
- `clip_outliers([1, 2, 3, 100, 5, 6])` with defaults -> the 95th
  percentile is ~`39.5`. The `100` is clipped to ~`39.5`.
- `clip_outliers([-100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 100])` ->
  the 5th and 95th percentiles clip `-100` and `100` to the boundary
  values.

## Complexity requirement

- O(n) time (one pass to compute the percentile; one pass to apply the
  clip). No Python loops.

## Constraints (for practice)

- Use `numpy`. Use `np.percentile` (or `np.quantile`) for the
  percentile computation.
- Use **boolean masking** to apply the clip in one vectorised
  operation: `arr = np.where(arr < low, low, np.where(arr > high, high, arr))`,
  or equivalently `arr = arr.clip(low, high)` (note: `clip` is
  inclusive; the prompt wants strict `<` and `>`, so the `np.where`
  form is the safer match).
- No Python `for` / `while` loops.

## Disallowed examples

```python
import numpy as np
arr = np.asarray(x)
low = np.percentile(arr, low_pct)
high = np.percentile(arr, high_pct)
out = []
for v in arr:                                # WRONG: Python loop
    if v < low:
        out.append(float(low))
    elif v > high:
        out.append(float(high))
    else:
        out.append(float(v))
return out
```

```python
# WRONG: arr.clip uses inclusive boundaries, but the prompt is strict.
return np.asarray(x).clip(np.percentile(...), np.percentile(...)).tolist()
```

## Hints

- `np.percentile(arr, q)` accepts `q` as a scalar (`0 <= q <= 100`).
  For the `low_pct` and `high_pct` arguments, call it twice (once each)
  rather than once with an array (the array form is a different
  operation: it returns a single array of both percentiles).
- `np.where(cond, a, b)` returns `a` where `cond` is true, else `b`.
  The nested form `np.where(cond1, a, np.where(cond2, b, c))` handles
  three-valued logic in one expression.
