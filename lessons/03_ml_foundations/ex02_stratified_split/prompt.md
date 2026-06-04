# ex02_stratified_split

ML fundamentals: train/test split with optional stratification.

Read: `theory.md` (3-5 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def train_test_split(
    xs: list[object],
    ys: list[int],
    *,
    test_size: float,
    seed: int = 0,
    stratify: bool = False,
) -> tuple[list[object], list[object], list[int], list[int]]:
    ...
```

Rules:

- `xs` and `ys` have the same length.
- `test_size` is a float in `(0, 1)`.
- Shuffle deterministically using `seed`.
- Return `(x_train, x_test, y_train, y_test)`.
- If `stratify=False`, do a simple shuffle and split.
- If `stratify=True`, split so class proportions in test roughly match the full set.
  (Use per-class shuffling; compute per-class test counts with rounding, but ensure the
  total test size equals `round(n * test_size)`.)

Clarifications:

- Always shuffle in a deterministic way using `seed` (your output should be identical across runs).
- If `stratify=True`, you are doing a label-aware split: shuffle within each class, then take a per-class slice for test.

## Constraints (for practice)

- Do not import sklearn.
