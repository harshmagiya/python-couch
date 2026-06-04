# ex04_logsumexp

Read: `theory.md` (3-4 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def logsumexp(x: list[float]) -> float:
    ...
```

Behavior:

- Return `log(sum(exp(x_i) for x_i in x))`.
- The implementation must be **numerically stable**: for large positive
  inputs the result must not overflow to `inf`, and for inputs that
  should evaluate to a large negative number the result must be
  representable as a finite float.
- For an empty `x`, raise `ValueError`.

## Examples

- `logsumexp([0.0, 0.0, 0.0])` ~ `log(3)` ~ `1.0986`.
- `logsumexp([1.0, 2.0, 3.0])` ~ `log(e + e^2 + e^3)` ~ `3.4076`.
- `logsumexp([1000.0, 1000.0, 1000.0])` ~ `1000.0 + log(3)` ~ `1001.0986`
  (the unstable form `log(sum(exp(x)))` would overflow to `inf`).
- `logsumexp([-1000.0, -1000.0, -1000.0])` ~ `-1000.0 + log(3)`
  ~ `-998.9014` (no overflow either way, but the principle still
  applies: subtract the max first).

## Complexity requirement

- O(n) time, one pass to find the max, one pass to compute the sum.
  (Or one pass with a running max-and-sum if you want; both are fine.)

## Constraints (for practice)

- Use `numpy`. Subtract the **max** of the input from every element
  before exponentiating. Adding the max back at the end is what makes
  the computation stable. The shape is:

  ```
  m = max(x)
  return m + log(sum(exp(x_i - m) for x_i in x))
  ```

- Do **not** write `log(sum(exp(x)))` directly. That is the unstable
  form and the test will catch it with large inputs.
- No Python loops in the implementation.

## Disallowed examples

```python
import math
import numpy as np
arr = np.asarray(x)                                 # WRONG: unstable form
return float(np.log(np.sum(np.exp(arr))))
```

```python
# WRONG: stable in principle, but the form is wrong
return float(np.log(np.sum(np.exp(x - np.max(x)))))  # missing the +max(x) at the end
```

## Hints

- The stable form is: `m = np.max(arr); return float(m + np.log(np.sum(np.exp(arr - m))))`.
- When you subtract `m` from each `x_i`, all of `exp(x_i - m)` are at
  most `1.0` (the one equal to `m` gives `exp(0) = 1`). The sum is at
  most `n`. `log` of that is at most `log(n)`. The final answer is
  `m + log(sum(...))`, which is finite even when `m` is huge.
- `float(scalar)` converts a numpy scalar back to a Python `float`.
  The return type is `float`, not `np.float64`.
