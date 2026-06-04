# ex05_softmax_rows

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def softmax_rows(x: list[list[float]]) -> list[list[float]]:
    ...
```

Behavior:

- `x` is a 2-D list of shape `(n_rows, n_cols)`. All rows have the same
  length. `n_rows >= 1` and `n_cols >= 1`.
- For each row, apply the **stable softmax** along the column axis:
  `softmax(row)_j = exp(row_j - max(row)) / sum(exp(row_k - max(row)) for k in cols)`.
- The result is a 2-D list of the same shape; each row sums to `1.0`
  (within float epsilon) and contains only finite, non-negative values.
- For an empty outer list, raise `ValueError`.

## Examples

- `softmax_rows([[1.0, 2.0, 3.0]])` ->
  `[[exp(-2)/(exp(-2)+exp(-1)+exp(0)), exp(-1)/(...), exp(0)/(...))]`
  ~ `[[0.0900, 0.2447, 0.6652]]`.
- `softmax_rows([[1.0, 2.0, 3.0], [4.0, 4.0, 4.0]])` ->
  `[[0.0900, 0.2447, 0.6652], [1/3, 1/3, 1/3]]`
  (row 1 is uniform because all entries are equal).
- `softmax_rows([[1000.0, 1000.0, 1000.0]])` -> `[[1/3, 1/3, 1/3]]`
  (the unstable form `exp(1000)` would overflow).

## Complexity requirement

- O(n_rows * n_cols). One reduction to find the max per row, one
  elementwise exp, one reduction to sum per row, one elementwise
  divide. All vectorised.

## Constraints (for practice)

- Use `numpy`.
- Subtract the row max before exponentiating. The shape dance is the
  same as in `ex02_subtract_row_mean`:
  `arr - arr.max(axis=1, keepdims=True)`.
- Do **not** use `scipy.special.softmax`. Implement it from
  `numpy.exp` and the max-subtraction trick.
- No Python loops.

## Disallowed examples

```python
import scipy.special                             # WRONG: the prompt bans scipy
return scipy.special.softmax(x, axis=1).tolist()
```

```python
import numpy as np
arr = np.asarray(x)                              # WRONG: unstable
return (np.exp(arr) / np.exp(arr).sum(axis=1, keepdims=True)).tolist()
```

```python
# WRONG: no max-subtraction, overflows for large positive entries
out = np.exp(arr) / np.exp(arr).sum(axis=1, keepdims=True)
```

## Hints

- The full expression:
  `exp(arr - arr.max(axis=1, keepdims=True)) / exp(...).sum(axis=1, keepdims=True)`.
- Save the numerator as a variable so you do not call `np.exp` twice.
- `arr.max(axis=1, keepdims=True)` has shape `(n_rows, 1)`. The
  broadcast over the column axis is what makes this work for
  rectangular inputs (n_rows != n_cols).
