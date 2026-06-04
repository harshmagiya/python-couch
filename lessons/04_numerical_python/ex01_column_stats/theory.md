# Column-wise Mean and Standard Deviation

## What problem this solves

Given a 2-D dataset (rows of observations, columns of features), compute
the per-column mean and per-column population standard deviation in one
shot. This is the first thing any tabular-data exploration script does
(`pandas.DataFrame.describe` is the user-friendly wrapper around it),
and the same shape shows up in batched normalisation passes inside
training loops.

## Mental model

A 2-D numpy array has two **axes**:

- `axis=0` runs **along rows** (per-column reductions drop the row axis).
- `axis=1` runs **along columns** (per-row reductions drop the column axis).

For `arr` of shape `(n_rows, n_cols)`:

- `arr.mean(axis=0)` returns shape `(n_cols,)` — one mean per column.
- `arr.std(axis=0, ddof=0)` returns shape `(n_cols,)` — one population
  std per column.

The default `ddof=0` is **population** standard deviation (divide by
`N`). `ddof=1` is **sample** standard deviation (divide by `N - 1`,
Bessel-corrected). NumPy and `pandas` differ: pandas defaults to
sample, numpy defaults to population. This exercise asks for
population, matching numpy's default.

## Why it matters in real projects

- `pandas.DataFrame.describe()` is `df.mean()`, `df.std()`, `df.min()`,
  etc. — all the same one-axis reduction under the hood.
- Batch normalisation: `(x - mean) / std` is computed per feature axis
  every forward pass, with `keepdims=True` to preserve the rank for
  broadcasting. The mental model is the same.
- Standardisation before PCA, k-NN, k-means, linear regression: every
  one starts with column-wise mean/std.

## Common pitfalls

### Forgetting `ddof=0`

- `arr.std(axis=0)` and `pandas.Series.std()` differ by exactly 1 in
  the denominator. Tests pin the population variant. If you switch
  between numpy and pandas in the same project, write a one-line
  helper that always returns the population std so the difference does
  not silently sneak in.

### `arr.std(axis=1)` (row-wise) by accident

- `axis=0` collapses rows -> column-wise.
- `axis=1` collapses columns -> row-wise.
- A common bug is to swap the axis because "the test data feels like
  it should be a row". Trace one small example to lock the convention
  in your head.

### Converting back to plain Python lists

- The function's return type is `tuple[list[float], list[float]]`. You
  cannot return a numpy array. Use `arr.tolist()` (one call) or
  `[float(x) for x in arr]` (still a loop; not necessary).

### `np.asarray` vs `np.array`

- `np.asarray` reuses the input buffer if it is already a compatible
  array. `np.array` always copies. For tests that pass a list, both
  work; for production code that may pass a numpy array, prefer
  `np.asarray` to avoid an unnecessary copy.

## Edge cases

- 1 row, 1 col -> mean is the only value, std is `0.0`.
- 1 row, many cols -> mean is the row, std is all zeros.
- All-equal column -> std is `0.0` (not a small floating-point
  residual; `np.std` returns exactly `0.0` when all values are equal).
- Empty outer list -> `ValueError` (no rows, no columns to reduce over).

## Quick check

`data = [[1, 2], [3, 4], [5, 6]]` (shape `(3, 2)`).

- `arr = np.asarray(data)` -> shape `(3, 2)`.
- `arr.mean(axis=0)` = `[3.0, 4.0]`.
- `arr.std(axis=0, ddof=0)` = `[(2/3)**0.5, (2/3)**0.5]` ≈ `[1.633, 1.633]`.

## ML/research connection

`column_stats` is the per-feature `mean` and `std` step that goes into `StandardScaler.fit` inside scikit-learn: `StandardScaler` calls `mean = X.mean(axis=0)` and `scale = X.std(axis=0)` (population std, with optional `with_mean` and `with_std` toggles), then applies `(X - mean) / scale` on `transform`. The same exact pair is the first thing a batch-normalisation layer computes per training batch.
