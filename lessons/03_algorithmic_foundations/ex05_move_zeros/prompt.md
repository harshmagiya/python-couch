# ex05_move_zeros

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def move_zeros(nums: list[int]) -> list[int]:
    ...
```

Behavior:

- Move every `0` to the end of the list.
- Preserve the relative order of the **non-zero** elements.
- Mutate the input list in place **and** return it (so the return value is
  the same list object as `nums`).
- The function must use only O(1) extra space (a few pointer variables are
  fine; a helper list of the same length is not).

## Examples

- `move_zeros([0, 1, 0, 3, 12])` returns `[1, 3, 12, 0, 0]`
  (call it `xs`; after the call, `xs is nums` is `True` and `xs == [1, 3, 12, 0, 0]`).
- `move_zeros([0, 0, 0])` returns `[0, 0, 0]`.
- `move_zeros([1, 2, 3])` returns `[1, 2, 3]`.
- `move_zeros([])` returns `[]`.
- `move_zeros([0])` returns `[0]`.
- `move_zeros([1, 0])` returns `[1, 0]`.

## Complexity requirement

- O(n) time.
- O(1) extra space (not counting the input itself).

## Constraints (for practice)

- No helper list, no `sorted(..., key=...)` trick (it would put zeros first
  and you would then reverse — and the "stable order" requirement would
  still be wrong, because `sorted` is not guaranteed stable for
  arbitrary keys in older Pythons; in 3.7+ it is, but the prompt's
  intent is for you to use a partition pattern).
- No list comprehension that builds a fresh list of length `n`.

## Disallowed examples

```python
non_zero = [x for x in nums if x != 0]                  # WRONG: O(n) extra list
zeros = [0] * (len(nums) - len(non_zero))
return non_zero + zeros                                  # also: not in-place
```

```python
return sorted(nums, key=lambda x: 0 if x == 0 else 1)   # WRONG: not in-place; brittle
```
