# ex16_top_k_streaming

Read: `theory.md` (3-5 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def top_k(nums: list[int], k: int) -> list[int]:
    ...
```

Behavior:

- Return the `k` largest elements of `nums`, in **descending** order.
- "Largest" means largest by value. Ties are not specified by the prompt; the implementation may return them in any order among equals.
- For `k = 0`, return `[]`.
- For `k >= len(nums)`, return `sorted(nums, reverse=True)` (i.e. all elements, sorted).
- For `k < 0`, raise `ValueError`.
- For empty `nums` with `k > 0`, raise `ValueError`.

## Examples

- `top_k([5, 1, 3, 2, 4], 3) == [5, 4, 3]`
- `top_k([1, 2, 3], 5) == [3, 2, 1]` (k > n, return all sorted)
- `top_k([], 3)` raises `ValueError`
- `top_k([5, 1, 3, 2, 4], 0) == []`
- `top_k([-1, -5, -2, -3], 2) == [-1, -2]`
- `top_k([7], 1) == [7]`

## Complexity requirement

- O(n log k) time, using a **min-heap of size k** via `heapq`.
- O(k) extra space (the heap holds at most k elements).

## Constraints (for practice)

- Maintain a min-heap of the `k` largest elements seen so far.
- For each `nums[i]`:
  - If the heap has fewer than `k` elements, push `nums[i]`.
  - Otherwise, if `nums[i]` is larger than the smallest element in the heap (the heap's root), pop the smallest and push `nums[i]`. Otherwise discard `nums[i]`.
- At the end, the heap contains the `k` largest elements. Sort them in descending order to return.

## Disallowed examples

```python
def top_k(nums, k):                                # WRONG: full sort, O(n log n)
    if k < 0:
        raise ValueError("k must be >= 0")
    if k == 0:
        return []
    return sorted(nums, reverse=True)[:k]
```

This works but doesn't use a heap; it's O(n log n) time and doesn't
demonstrate the heap-based streaming approach. The prompt explicitly
asks for the heap.

```python
def top_k(nums, k):                                # WRONG: BFS / selection by repeated max
    if k < 0:
        raise ValueError("k must be >= 0")
    if k == 0:
        return []
    out = []
    remaining = list(nums)
    for _ in range(min(k, len(nums))):
        m = max(remaining)                          # O(n) per iteration
        out.append(m)
        remaining.remove(m)                        # O(n) per iteration
    return out
```

Each iteration is O(n) (max + remove), and you do it k times, for O(n*k)
total. Worse than the heap for n >> k. Banned.

## Hints

- `heapq` is a min-heap. The "smallest of the `k` largest" is at index 0.
- The "if bigger than the smallest, replace" rule keeps the heap's size at most `k` and ensures the heap always contains the `k` largest seen so far.
- Use `heapq.heappushpop(heap, x)` which is "pop smallest, push x" in one call — slightly faster than separate `heappush` and `heappop`.
- At the end, the heap is in *ascending* order (min-heap property). `sorted(heap, reverse=True)` gives you the descending output.
