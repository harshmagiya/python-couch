# Row-wise Stable Softmax

## What problem this solves

Given a 2-D matrix of "logits" (raw scores, possibly unbounded),
return the same-shaped matrix where each row has been turned into a
probability distribution: `softmax(row)` sums to 1.0, all entries are
non-negative, and the largest logit gets the largest probability. The
result is computed in a numerically stable way: no overflow on large
logits, no underflow on very negative logits.

This is the output layer of a classification neural network. It is
also the step that converts language-model logits into a probability
distribution over the next token at every decoding step.

## Mental model

The per-row formula:

```
softmax(x)_j = exp(x_j) / sum_k(exp(x_k))
```

is mathematically correct, but for a row like `[1000, 1000, 1000]`
every `exp(1000)` overflows to `inf`, and `inf / inf = nan`. The
stable form factors out the row max:

```
softmax(x)_j = exp(x_j - m) / sum_k(exp(x_k - m)),     where m = max(x)
```

When `m = 1000` and `x_j = 1000`, `x_j - m = 0`, `exp(0) = 1`. None
of the exponents is bigger than 1. The denominator is finite. The
result is finite.

In code with numpy:

```python
arr = np.asarray(x)                                          # (n_rows, n_cols)
m = arr.max(axis=1, keepdims=True)                           # (n_rows, 1)
e = np.exp(arr - m)                                          # (n_rows, n_cols)
out = e / e.sum(axis=1, keepdims=True)                       # (n_rows, n_cols)
return out.tolist()
```

The `keepdims=True` is the broadcasting lever you saw in
`ex02_subtract_row_mean`.

## Why it matters in real projects

- Output layer of a classification neural network: logits -> softmax
  -> cross-entropy with the one-hot label.
- Language-model decoding: at every step, the model emits logits over
  the vocabulary; sampling or beam search takes a softmax of those
  logits.
- Reinforcement learning: the policy is a softmax over action
  preferences; the temperature parameter multiplies the logits
  before the softmax.
- Attention: scaled-dot-product attention uses a softmax over the
  scaled scores to produce attention weights.

## Common pitfalls

### Using `scipy.special.softmax`

- The prompt bans it. The point is the implementation: subtract the
  max, exp, normalise. Calling a one-liner from scipy bypasses the
  lesson entirely. (And in production, scipy's softmax is itself
  implemented as `exp(x - x.max(axis)) / exp(...).sum(axis)` — the
  same trick.)

### Forgetting the max-subtraction

- On small inputs (e.g. `[1, 2, 3]`) the unstable form works because
  `exp(3) ~ 20` is well within float range. The tests use large
  inputs (e.g. `[1000, 1000, 1000]`) to force the issue; the
  unstable form returns `nan` or `inf` and the test catches it.

### `arr.max(axis=1)` without `keepdims=True`

- Shape `(n_rows,)` does **not** broadcast with `(n_rows, n_cols)`.
  You'll get either a wrong result (on square matrices, by accident)
  or a `ValueError` (on non-square matrices). The test uses a
  non-square matrix.

### All-zero row

- `softmax([0, 0, 0])` = `[1/3, 1/3, 1/3]`. The max is 0, the
  subtraction leaves everything at 0, `exp(0) = 1`, divided by 3.
  Uniform. Correct.

### Negative logits

- Negative logits do not break anything; `exp` of a negative number
  is a positive fraction. The result is still a probability
  distribution.

## Edge cases

- Single row, many columns: standard 1-D softmax.
- Many rows, single column: each row's softmax is `[1.0]` (only one
  class to put probability on).
- All-equal row: uniform distribution `[1/n_cols, ..., 1/n_cols]`.
- Very large positive logits: stable form returns finite values.
- Very large negative logits: stable form returns finite values
  (e.g. `softmax([-1000, -1000])` = `[0.5, 0.5]`, not `nan`).
- Empty outer list: `ValueError`.

## Quick check

`x = [[1, 2, 3]]` (one row, three columns).

- `m = [3]` (shape `(1, 1)`).
- `arr - m = [[-2, -1, 0]]`.
- `e = [[exp(-2), exp(-1), exp(0)]]` ~ `[[0.1353, 0.3679, 1.0]]`.
- `e.sum(axis=1) = [1.5032]`.
- `out = e / 1.5032` ~ `[[0.0900, 0.2447, 0.6652]]`.
- Each row sums to 1.0. ✓

## ML/research connection

The exact `exp(x - x.max(axis=1, keepdims=True)) / exp(...).sum(axis=1, keepdims=True)` is the formula inside `torch.nn.functional.softmax`, `scipy.special.softmax`, and the manual softmax implementations in every deep-learning textbook. It is the output layer of a classification neural network (with `cross_entropy` as the loss) and the per-step decoder of every language model.
