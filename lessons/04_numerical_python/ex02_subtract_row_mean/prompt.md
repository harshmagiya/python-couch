# ex02_subtract_row_mean

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def subtract_row_mean(x: list[list[float]]) -> list[list[float]]:
    ...
```

Behavior:

- `x` is a 2-D list of shape `(n_rows, n_cols)`. All rows have the same
  length. `n_rows >= 1` and `n_cols >= 1`.
- For each row, subtract the **mean of that row** from every element
  in the row. The result is a 2-D list of the same shape where each
  row sums to ~`0.0` (within float epsilon).
- For an empty outer list, raise `ValueError`.

## Examples

- `subtract_row_mean([[1.0, 2.0, 3.0], [4.0, 4.0, 4.0]])` →
  `[[-1.0, 0.0, 1.0], [0.0, 0.0, 0.0]]`
  (row 0 mean is 2.0, row 1 mean is 4.0).
- `subtract_row_mean([[5.0, 5.0]])` → `[[0.0, 0.0]]`.
- `subtract_row_mean([[1.0], [2.0], [3.0]])` → `[[0.0], [0.0], [0.0]]`
  (each row has one element; mean equals that element; subtraction
  yields 0).
- `subtract_row_mean([])` raises `ValueError`.

## Complexity requirement

- O(n_rows * n_cols) work.
- Use **broadcasting**: a `(n_rows, 1)` row-mean vector minus a
  `(n_rows, n_cols)` matrix. No `np.tile`, no explicit row replication.

## Constraints (for practice)

- Use `numpy` and broadcasting (`arr - arr.mean(axis=1, keepdims=True)`
  is the canonical form).
- Do not use `np.tile`, `np.repeat`, or `np.broadcast_to` to manually
  expand the row-mean vector to full shape. That defeats the point of
  the exercise.
- No Python loops.

## Disallowed examples

```python
import numpy as np
arr = np.asarray(x)
row_means = arr.mean(axis=1, keepdims=True)
tiled = np.tile(row_means, (1, arr.shape[1]))    # WRONG: defeats broadcasting
return (arr - tiled).tolist()
```

```python
# WRONG: row-by-row Python loop
import numpy as np
arr = np.asarray(x)
out = []
for row in arr:
    out.append((row - row.mean()).tolist())
return out
```

## Hints

- The shape dance: `arr` is `(n_rows, n_cols)`. `arr.mean(axis=1)` is
  shape `(n_rows,)` — that **broadcasts** with `arr` only on the wrong
  axis (numpy aligns trailing axes). `arr.mean(axis=1, keepdims=True)`
  is shape `(n_rows, 1)` — that **broadcasts** correctly across the
  column axis.
- `keepdims=True` is the entire point. Forgetting it is the single
  most common bug in row-wise normalisation.
