# Train/Test Split + Stratification

This exercise builds a reliable split function: the foundation of honest evaluation.

## Why splitting matters

You use a held-out test set to estimate how a model will perform on unseen data.
If you accidentally let test information influence training, your metrics become overly optimistic.

## Deterministic shuffling (reproducibility)

Splits should be reproducible:

- Same input + same `seed` => same output.
- Use Python's `random.Random(seed)` (local RNG) instead of global `random` state.

Reproducibility is not "nice to have" in ML; it is how you debug and compare experiments.

## Plain shuffle split (no stratification)

The simplest approach:

- Create a list of indices `0..n-1`
- Shuffle indices deterministically
- Put the first `n_test = round(n * test_size)` into test, the rest into train
- Build `x_train/x_test/y_train/y_test` by indexing

## Stratified split (label proportions)

When classes are imbalanced, a plain random split can create a test set with too few (or zero) minority examples.
That makes metrics unstable and misleading.

Stratification aims to keep class proportions in the test set close to the full dataset.

Conceptually:

- Group indices by class label (from `ys`)
- Shuffle indices *within each class* deterministically
- Decide how many test items each class should contribute
- Take that many indices per class for test; the remaining go to train

## The rounding problem

Let `n_test = round(n * test_size)`.

If a class has `count_c` items, its ideal test allocation is:

- `ideal_c = count_c * test_size`

But `ideal_c` is usually fractional, and allocations must be integers. Any reasonable method must ensure:

- `sum(test_count_c) == n_test` (exact total)
- Each `test_count_c` is between `0` and `count_c`
- Results are deterministic

Common approaches:

- Round each `ideal_c` and then adjust up/down until totals match.
- Floor each `ideal_c`, then distribute the remaining slots to classes with the largest fractional parts.

In production, you'd often lean on `sklearn.model_selection.train_test_split(..., stratify=ys)`, but implementing it once teaches you what it guarantees and what it doesn't.

## Pitfalls

- Shuffling `xs` and `ys` separately (breaks alignment): always shuffle indices or paired tuples.
- Using global RNG (non-reproducible across other code that uses `random`).
- Forgetting the exact test size requirement (`round(n * test_size)` in this course).
- Stratifying but not shuffling inside class (can introduce ordering bias).
