# Subtract Row Mean (Broadcasting)

## What problem this solves

For each row of a 2-D matrix, subtract the mean of that row from every
element. The result is a "row-centred" matrix where each row sums to
~zero. This is the row-wise analogue of mean-centring a dataset per
feature, and it shows up in PCA whitening, batch normalisation
(scale-only variant), and a number of covariance stabilisation tricks.

## Mental model

Two numpy arrays of different shapes can be combined element-wise by
**broadcasting** if their shapes are compatible. The rule is:

> Numpy aligns shapes from the **right**. Dimensions match if they are
> equal, or if one of them is `1`.

For "subtract row mean from each row":

- `arr` has shape `(n_rows, n_cols)`.
- `arr.mean(axis=1)` has shape `(n_rows,)`. Numpy tries to align this
  with `(n_rows, n_cols)` from the right: it lines up `(n_rows,)` with
  the column axis, which **fails** unless `n_rows == n_cols`. Wrong
  axis.
- `arr.mean(axis=1, keepdims=True)` has shape `(n_rows, 1)`. Numpy
  aligns it with `(n_rows, n_cols)`: the column axis of size 1 broadcasts
  to size `n_cols`. Right axis. The subtraction works.

`keepdims=True` is the lever that makes broadcasting behave the way you
want.

## Why it matters in real projects

- Per-row normalisation in audio / image feature pipelines (e.g.
  "subtract DC offset per spectrogram frame").
- The math of standardisation: `(x - mean) / std` per row is row-mean
  subtraction followed by row-std division. Both are broadcasts over
  `axis=1` with `keepdims=True`.
- In neural-network batch norm: `(x - E[x]) / sqrt(Var[x])` uses
  the same shape arithmetic, just with `axis` parameterised.

## Common pitfalls

### Forgetting `keepdims=True`

- The single most common broadcasting bug. The operation runs without
  raising, but on non-square matrices it raises a `ValueError` like
  "operands could not be broadcast together with shapes (n_rows,n_cols)
  (n_rows,)". When you see that, you forgot `keepdims=True`.

### Using `np.tile` or `np.repeat` to "fix" the shape

- It works but defeats the point. Broadcasting is the lightweight
  version; tiling allocates an O(n_rows * n_cols) intermediate and
  hides the axis. The constraint enforces this.

### Confusing `axis=0` (column-wise) and `axis=1` (row-wise)

- The prompt explicitly says "mean of that row". `axis=1` is the
  reduction that walks **across** columns and produces one number
  per row. If you have a `(samples, features)` matrix, the rows
  are samples and `axis=1` is the features axis, which is what
  per-sample mean-centring reduces over.

### Returning numpy floats instead of plain Python floats

- The return type is `list[list[float]]`. `arr.tolist()` returns
  Python floats, so use that on the result.

## Edge cases

- Single-column matrix: each row's mean is its only element; result
  is all zeros.
- All-equal rows: the row mean equals the only value, result is all
  zeros.
- Single row, many columns: subtracts the only mean from each
  element.
- Empty outer list: `ValueError`.

## Quick check

`x = [[1, 2, 3], [4, 4, 4]]`.

- `arr = np.asarray(x)` (shape `(2, 3)`).
- `arr.mean(axis=1, keepdims=True)` = `[[2.0], [4.0]]` (shape `(2, 1)`).
- `arr - row_means` = `[[-1, 0, 1], [0, 0, 0]]` (shape `(2, 3)`,
  broadcasts the `(2, 1)` over the column axis).

## ML/research connection

The exact `arr - arr.mean(axis=1, keepdims=True)` pattern is the per-row centre step in scikit-learn's `Normalizer(norm='l1'/'l2')` and in the row-wise mean-centring step of PCA whitening (after which you also divide by the row std). In PyTorch batch norm, the running mean is `x.mean(dim=0, keepdim=True)` and the same `keepdim=True` shape discipline applies to keep the `(N, C, H, W)` tensor shape intact.
