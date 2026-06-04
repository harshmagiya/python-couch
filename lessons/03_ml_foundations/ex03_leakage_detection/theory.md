# Target Leakage (Obvious Case)

This exercise introduces a high-impact failure mode in ML: target leakage.

## What is leakage?

Leakage happens when your features include information that would not be available at prediction time, or that is derived from the target.
It leads to unrealistically high validation/test scores and models that fail in production.

## The specific leakage in this exercise

Here we focus on the most obvious kind:

- A feature column is literally the same as the label column (a direct copy).

If a model can read the answer from a feature, it will look "perfect" but it learned nothing useful.

## Mental model

Given `rows` (list of dictionaries with consistent keys) and `label`:

- Consider each feature key `k` where `k != label`.
- `k` is leakage if `row[k] == row[label]` for every row.
- Return all such `k`, sorted.

## Why this matters in real projects

Direct copies are rare, but near-copies are common:

- A post-event field (e.g., "refund_issued") predicting "fraud".
- A feature engineered using the full dataset (including future) before splitting.
- IDs or timestamps that leak the split or the outcome.

Even small leakage can move your metrics enough to choose the wrong model.

## Pitfalls

- Accidentally including the label key in the output.
- Not handling empty input (`rows == []`): there are no columns to flag.
- Confusing "perfectly predictive" with "highly correlated": this exercise is exact equality only.
