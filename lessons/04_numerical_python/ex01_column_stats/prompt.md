# ex01_column_stats

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def column_stats(data: list[list[float]]) -> tuple[list[float], list[float]]:
    ...
```

Behavior:

- `data` is a 2-D list of numbers with shape `(n_rows, n_cols)`. All rows
  have the same length. `n_rows >= 1` and `n_cols >= 1`.
- Return `(means, stds)` where `means[j]` is the mean of column `j` and
  `stds[j]` is the **population** standard deviation of column `j` (i.e.
  divide by `n_rows`, not `n_rows - 1`).
- For a column where every value is the same, the standard deviation is
  `0.0`.
- For an empty outer list (zero rows), raise `ValueError`.

## Examples

- `column_stats([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])` →
  `([3.0, 4.0], [np.std([1,3,5], ddof=0), np.std([2,4,6], ddof=0)])`
  = `([3.0, 4.0], [1.632993161855452, 1.632993161855452])`
  (rounded, the population stds are `(4/3)**0.5 ≈ 1.633`).
- `column_stats([[7.0, 7.0], [7.0, 7.0]])` → `([7.0, 7.0], [0.0, 0.0])`.
- `column_stats([[1.0]])` → `([1.0], [0.0])`.
- `column_stats([])` raises `ValueError`.

## Complexity requirement

- O(n_rows * n_cols) work, achieved by one vectorised pass.
- No Python `for` / `while` loops in the implementation.

## Constraints (for practice)

- Use `numpy`. The function may convert the input to a `numpy.ndarray`
  internally; that's fine.
- The implementation must compute means and stds with **vectorised**
  operations (e.g. one call to `arr.mean(axis=0)`), not row-by-row Python
  loops.
- The standard deviation is **population** (`ddof=0`), not sample
  (`ddof=1`).

## Disallowed examples

```python
import numpy as np
arr = np.asarray(data)
n_cols = arr.shape[1]
means = []
stds = []
for j in range(n_cols):                                  # WRONG: column-by-column Python loop
    col = arr[:, j]
    means.append(float(col.mean()))
    stds.append(float(col.std(ddof=0)))
return means, stds
```

```python
# WRONG: ddof=1 (sample std, not population std)
return list(arr.mean(axis=0)), list(arr.std(axis=1))
```

```python
# WRONG: nothing to do with numpy
def column_stats(data):
    means = [sum(col) / len(col) for col in zip(*data)]
    stds = [...]
    return means, stds
```

## Hints

- `numpy.asarray(data)` accepts a list-of-lists and infers a 2-D array
  of shape `(n_rows, n_cols)`.
- `arr.mean(axis=0)` returns a 1-D array of column means. Same idea for
  `arr.std(axis=0, ddof=0)`.
- `float(x)` or `arr.tolist()` converts numpy scalars to Python
  `float`s. `tolist()` on a 1-D array gives a plain `list[float]`,
  which is what the return type promises.
