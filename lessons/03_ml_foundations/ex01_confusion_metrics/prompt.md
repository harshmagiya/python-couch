# ex01_confusion_metrics

ML fundamentals: metrics from a confusion matrix.

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def confusion_counts(
    y_true: list[int],
    y_pred: list[int],
    *,
    positive: int = 1,
) -> tuple[int, int, int, int]:
    ...


def precision_recall_f1(
    y_true: list[int],
    y_pred: list[int],
    *,
    positive: int = 1,
) -> tuple[float, float, float]:
    ...
```

Definitions (for the `positive` class):

- `tp`: predicted positive AND actually positive
- `fp`: predicted positive BUT actually negative
- `tn`: predicted negative AND actually negative
- `fn`: predicted negative BUT actually positive

Mental model (binary one-vs-rest):

- Treat `positive` as the only positive label; every other label is "negative" for this exercise.
- For each index `i`, compare `y_true[i] == positive` and `y_pred[i] == positive`, then increment exactly one of `tp/fp/tn/fn`.

Metrics:

- `precision = tp / (tp + fp)` (if denominator is 0, return 0.0)
- `recall = tp / (tp + fn)` (if denominator is 0, return 0.0)
- `f1 = 2 * precision * recall / (precision + recall)` (if both 0, return 0.0)

## Constraints (for practice)

- Do not import sklearn.

Disallowed examples:

```python
from sklearn.metrics import precision_score
```
