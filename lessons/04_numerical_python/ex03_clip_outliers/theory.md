# Clip Outliers by Percentile (Boolean Masking)

## What problem this solves

Replace extreme values in a 1-D array with boundary values derived from
the data's own percentiles. This is a *lightweight* outlier-handling
step: a full 1-D array of length `n` comes in, and a clipped copy
comes out. No data is dropped, no model is fit; values outside the
`[low_pct, high_pct]` band are simply capped.

This shows up in every tabular data-cleaning pipeline (winsorisation),
in plotting helpers that need to draw the same axis range across
multiple plots, and in any preprocessing step where a few extreme
values would otherwise dominate a `mean` / `std` calculation.

## Mental model

Two numpy primitives do all the work:

1. **Percentile computation**: `np.percentile(arr, q)` for `q` in
   `[0, 100]` returns a single scalar. Linear interpolation between
   adjacent sorted values. `q=50` is the median.
2. **Boolean masking**: a numpy array of booleans (the result of
   `arr < low` or `arr > high`) can be used to drive `np.where`:
   `np.where(cond, a, b)` returns `a` where `cond` is true, else `b`.

The full pipeline is:

```python
arr = np.asarray(x)
low = np.percentile(arr, low_pct)
high = np.percentile(arr, high_pct)
clipped = np.where(arr < low, low, np.where(arr > high, high, arr))
return clipped.tolist()
```

The double `np.where` handles the three regions: below `low`, above
`high`, in between.

## Why it matters in real projects

- **Winsorisation** in stats: capping at the 5th and 95th percentiles
  is a standard step before computing correlation coefficients on
  data with heavy tails.
- Plotting: `plt.ylim(np.percentile(y, 1), np.percentile(y, 99))`
  sets axis limits to data percentiles, dodging extreme outliers.
- Preprocessing for downstream ML models: a few extreme values in a
  feature can blow up k-means cluster centres or distort a linear
  regression's loss; clipping at the 1st/99th percentiles is a
  common, cheap mitigation.

## Common pitfalls

### Forgetting the strict-vs-inclusive boundary

- The prompt says values **strictly** below the low percentile are
  clipped. A value *equal* to the low percentile is not clipped.
- `arr.clip(low, high)` is **inclusive** on both ends; it would clip
  values exactly equal to the percentile. The test pins the strict
  form, so use `np.where` (not `clip`).

### `np.percentile(arr, [low_pct, high_pct])` (array form)

- This returns **one** array of two percentiles. The prompt's
  signature uses two separate scalars, so calling `np.percentile`
  twice (once per scalar) is the cleaner form.

### Method-of-percentile differences

- `np.percentile` defaults to `"linear"` interpolation. That's what
  the test expects. If you pass `method="lower"` (older API) or
  `interpolation="lower"` (newer API), the answers will differ on
  inputs where the percentile falls between two sorted values.
  The exercise is about the *concept*, not the interpolation mode;
  tests pin "linear".

### Forgetting `tolist()` at the end

- The return type is `list[float]`. A numpy array is not a `list`
  (the assertion `type(out) is list` would fail). Use `.tolist()`.

## Edge cases

- Empty list -> `ValueError`.
- `low_pct == high_pct`: only values strictly less than or strictly
  greater than *the same* boundary are clipped. The middle values
  (including duplicates of the boundary) are kept.
- All values equal: percentile is that value; nothing is clipped
  (strict comparison, all values equal the boundary).
- Single element: same as above; nothing is clipped.
- `low_pct = 0, high_pct = 100`: percentiles are `min` and `max`;
  no value is strictly outside `[min, max]`, so nothing is clipped.

## Quick check

`x = [1, 2, 3, 100, 5, 6]` with `low_pct=5, high_pct=95`.

- `arr = np.asarray(x)`.
- `np.percentile(arr, 5)` ~ `1.25`.
- `np.percentile(arr, 95)` ~ `53.95`.
- After `np.where`: `[1, 2, 3, 53.95, 5, 6]`.

The `100` is clipped to the 95th percentile; the `1` is not (it
is above the 5th percentile). The interior values are unchanged.

## ML/research connection

Winsorisation by percentile is the cheap outlier-handling step that scikit-learn's `RobustScaler` and `QuantileTransformer` generalise: `RobustScaler` subtracts the median and scales by the IQR (which is `(q75 - q25)`), and `QuantileTransformer` maps every value to its rank-uniform percentile — both of which start with `np.percentile` under the hood.
