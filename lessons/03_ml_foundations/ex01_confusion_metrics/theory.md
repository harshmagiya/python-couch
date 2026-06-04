# Confusion Counts + Precision/Recall/F1 (Binary)

This exercise implements the core bookkeeping behind many classification metrics.

## What problem this solves

Given ground-truth labels (`y_true`) and model predictions (`y_pred`), you want to measure how good the model is at detecting a chosen "positive" class.

In real ML work, these numbers help you choose thresholds, compare models, and understand trade-offs (false alarms vs missed detections).

## Mental model (one-vs-rest)

Pick a `positive` label (default `1`). For metric purposes:

- True label is positive if `y_true[i] == positive`
- Predicted label is positive if `y_pred[i] == positive`
- Everything else is treated as negative (even if there are multiple other label values)

That turns the problem into a binary classification view for the chosen class.

## Confusion counts

For each example `i`, compute two booleans:

- `t = (y_true[i] == positive)`
- `p = (y_pred[i] == positive)`

Exactly one of these four cases applies:

- `tp` (true positive): `t` and `p`
- `fp` (false positive): not `t` and `p`
- `tn` (true negative): not `t` and not `p`
- `fn` (false negative): `t` and not `p`

Return order in this course: `(tp, fp, tn, fn)`.

## Metrics

- Precision: "when we predicted positive, how often were we right?"
  - `precision = tp / (tp + fp)`
- Recall: "of the actual positives, how many did we catch?"
  - `recall = tp / (tp + fn)`
- F1: single score balancing precision and recall (harmonic mean)
  - `f1 = 2 * precision * recall / (precision + recall)`

## Edge cases (important)

In small datasets or rare classes, denominators can be 0:

- If `tp + fp == 0`: there were no predicted positives. Define precision as `0.0`.
- If `tp + fn == 0`: there were no actual positives. Define recall as `0.0`.
- If `precision + recall == 0`: define f1 as `0.0`.

These conventions avoid division-by-zero and match common library behavior.

## Common pitfalls

- Mixing up `fp` vs `fn`:
  - `fp`: model said positive, truth is negative (false alarm)
  - `fn`: model said negative, truth is positive (miss)
- Treating label `0` as special: it isn't; only equality with `positive` matters.
- Forgetting that the exercise is one-vs-rest: if labels are `2/1/0`, "negative" means "not positive".
- Returning the counts in a different order.

## Quick sanity check example

`positive = 1`

- `y_true = [1, 1, 0, 0, 1]`
- `y_pred = [1, 0, 1, 0, 0]`

Counts:

- `tp = 1` (idx 0)
- `fp = 1` (idx 2)
- `tn = 1` (idx 3)
- `fn = 2` (idx 1, 4)

So precision = `1/(1+1)=0.5`, recall = `1/(1+2)=0.333...`.
