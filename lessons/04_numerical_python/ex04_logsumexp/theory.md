# Log-Sum-Exp (Numerical Stability)

## What problem this solves

Compute `log(sum(exp(x_i)))` for a list `x` of floats. The naive
formulation `log(sum(exp(x_i)))` is **numerically unstable**: if any
`x_i` is large (say `1000`), `exp(1000)` overflows IEEE 754 double
to `inf`, and once the sum is `inf` no amount of `log` will bring it
back. The standard fix is to factor out the max first.

The log-sum-exp function is the workhorse of every softmax /
log-softmax computation, every cross-entropy loss that takes
logits (not probabilities) as input, and a number of
sequence-decoding tricks (e.g. the "log-sum-exp over beam scores"
step inside beam search).

## Mental model

The key identity:

```
log(sum(exp(x_i)))            =  log(sum(exp(x_i) * 1))
                              =  log(sum(exp(x_i) * exp(m) * exp(-m)))
                              =  log(exp(m) * sum(exp(x_i - m)))
                              =  m + log(sum(exp(x_i - m)))
```

for any scalar `m`. Picking `m = max(x)` makes `x_i - m <= 0` for all
`i`, so `exp(x_i - m) in (0, 1]`. The sum is at most `n`. `log(sum)`
is bounded. The final answer is `m + log(sum)`, where `m` is the
original max.

The whole point: we never compute `exp(big_number)` directly. Every
exponent is of a non-positive number.

## Why it matters in real projects

- **Log-softmax**: `log_softmax(x_i) = x_i - logsumexp(x)`. Computing
  `log_softmax` naively (`log(softmax(x))`) underflows for very
  negative logits. The stable form is `x - logsumexp(x)`.
- **Cross-entropy with logits**: `cross_entropy(logits, labels) =
  -sum(labels * log_softmax(logits))`. This is computed with a
  log-sum-exp inside, not a `softmax` + `log` + `cross_entropy`
  pipeline.
- **Beam search**: combining log-probabilities from different beam
  paths, then normalising across beams, requires log-sum-exp.

## Common pitfalls

### Forgetting the `+ m` at the end

- `log(sum(exp(x - max(x))))` is **not** `log(sum(exp(x)))`. It is
  off by exactly `max(x)`. The test will catch this with a small
  example (e.g. `[0, 0, 0]` -> answer is `log(3)`, but the broken
  form gives `log(1) = 0`).

### The unstable form for large positive `x`

- `log(sum(exp([1000, 1000, 1000])))` mathematically equals
  `1000 + log(3)`, but in floating point:
  - `exp(1000) = inf`
  - `sum([inf, inf, inf]) = inf`
  - `log(inf) = inf`
- The stable form: `m = 1000`, `arr - m = [0, 0, 0]`, `exp(...) = 1`,
  `sum = 3`, `log(3) ~ 1.0986`, result `1000 + 1.0986 = 1001.0986`.

### All-negative `x` (or all-very-negative)

- Subtract the max (least-negative) and add it back. Same math, same
  stability. The principle is "factor out the largest, every other
  exponent is in `(-inf, 0]`.

### Returning a numpy scalar

- The return type is `float`. Use `float(...)` on the final numpy
  scalar. `np.float64` and `float` are not the same type to pytest's
  `is` checks; the test will use `pytest.approx`, which does not
  care, but `type(out) is float` will fail if you forget.

## Edge cases

- Single element: `logsumexp([x])` = `x`.
- All equal: `logsumexp([c, c, c, c])` = `c + log(n)`.
- Empty list: `ValueError`.
- All zeros: `log(n)`.
- Mix of very large and very small: still works (e.g. `[-1000, 1000]`
  -> `1000 + log(1 + exp(-2000))` ~ `1000`).

## Quick check

`x = [1.0, 2.0, 3.0]`.

- `m = 3.0`.
- `arr - m = [-2, -1, 0]`.
- `exp(arr - m) = [exp(-2), exp(-1), 1]` ~ `[0.1353, 0.3679, 1.0]`.
- `sum = 1.5032`.
- `log(1.5032) = 0.4076`.
- Result: `3.0 + 0.4076 = 3.4076`.

That matches the expected `log(e + e^2 + e^3)`.

## ML/research connection

The exact `m + np.log(np.sum(np.exp(x - m)))` is the formula inside `scipy.special.logsumexp`, the core of `torch.nn.functional.log_softmax(x)` and `torch.nn.functional.cross_entropy(x, y)` (the latter is implemented as `-log_softmax(x)[y]`, which is just `-(x[y] - logsumexp(x)) = logsumexp(x) - x[y]`). It is also the step that turns raw language-model logits into a normalised log-probability distribution at every decoding step.
