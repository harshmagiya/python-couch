# ex08_reverse_list_in_place

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def reverse_list_in_place(nums: list[int]) -> list[int]:
    ...
```

Behavior:

- Reverse the order of elements in `nums` *in place* (mutate the input list).
- Also return the same list object (so the caller can use the return value
  or the original reference; both point to the reversed list).
- The function must use only O(1) extra space (a few index variables are
  fine; a helper list of the same length is not).

## Examples

- `reverse_list_in_place([1, 2, 3, 4])` mutates the input to `[4, 3, 2, 1]`
  and returns the same list object.
- `reverse_list_in_place([1, 2])` -> `[2, 1]`.
- `reverse_list_in_place([1])` -> `[1]`.
- `reverse_list_in_place([])` -> `[]`.

## Complexity requirement

- O(n) time.
- O(1) extra space (the input list itself doesn't count).

## Constraints (for practice)

- No slicing (`nums[::-1]`) — that builds a new list.
- No `reversed(nums)` or `list(reversed(nums))` — that returns a new list.
- No `nums.reverse()` (that's a one-liner but defeats the point: this
  exercise is about practicing the head/tail pointer swap).
- No helper list.

## Disallowed examples

```python
return nums[::-1]                                    # WRONG: new list
```

```python
return list(reversed(nums))                          # WRONG: new list
```

```python
return nums.reverse() or nums                        # WRONG: .reverse() returns None;
                                                     # the OR trick works but defeats the exercise
```

```python
return [nums[i] for i in range(len(nums) - 1, -1, -1)]  # WRONG: new list
```
