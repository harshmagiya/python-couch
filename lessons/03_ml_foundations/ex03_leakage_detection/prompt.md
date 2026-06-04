# ex03_leakage_detection

ML fundamentals: detect obvious target leakage.

Read: `theory.md` (2-4 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def leakage_columns(rows: list[dict[str, object]], label: str) -> list[str]:
    ...
```

You are given `rows`, a list of dicts with the same keys, and `label`, the key name
of the target.

Return a sorted list of feature column names (keys excluding `label`) that are
**perfectly predictive** of the label in this dataset.

For this exercise, a feature column `k` is considered leakage if, for every row:

- `row[k] == row[label]`

Notes:

- Ignore missing keys (assume well-formed rows).
- Do not include `label` itself in the output.

Mental model:

- You're looking for columns that are a direct copy of the target (a trivial form of leakage).
- For each feature key `k != label`, check whether `row[k] == row[label]` holds for all rows.

## Constraints (for practice)

- Do not use pandas.
