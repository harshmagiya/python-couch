# Heap / Priority Queue: Top-k Streaming

## What problem this solves

Find the `k` largest elements of a sequence, ideally without sorting the entire sequence. The full-sort solution is O(n log n) and produces more output than you need; the heap-of-size-k solution is O(n log k) and uses O(k) extra memory. For n in the millions and k small (say, k = 100), the difference is huge. The same pattern underlies top-k predictions, beam search, streaming median, k-summable sketches, and priority queues in A*-style search.

## Mental model

Maintain a **min-heap of the `k` largest elements seen so far**. The heap's root is the smallest of those `k` elements — i.e. the smallest of the values large enough to be in the top-k.

For each new element `x`:

- If the heap has fewer than `k` elements, push `x`. There's room.
- Otherwise, if `x > heap[0]` (the current smallest of the top-k), then `x` deserves to be in the top-k and the current smallest does not. Replace: pop the smallest, push `x`.
- Otherwise, `x` is too small to be in the top-k. Discard.

At the end, the heap contains the `k` largest elements in *unsorted* order (min-heap property, but not sorted fully). Sort the heap in descending order to produce the output.

## Why a min-heap, not a max-heap

A common question: "if we want the largest, shouldn't we use a max-heap?" The answer is: a min-heap of the *k largest* is the right tool because we want the *smallest* of the k largest to be the one we compare against (so we know whether to replace it). With a min-heap, that smallest is at the root, and the comparison is O(1). With a max-heap, finding the smallest of the k would be O(k).

`heapq` in Python is a min-heap. For a max-heap, you negate the values on push/pop or wrap with a `MaxHeap` class.

## Why it matters in real projects

- **Top-k predictions**: in a multi-class classifier, you want the top-5 predicted probabilities. With 10,000 classes, sorting is wasteful; a min-heap of size 5 is O(n log 5) = O(n).
- **Beam search** in NLP (sequence-to-sequence models): at each decoding step, keep the top-k partial hypotheses. The heap pattern is exactly top-k streaming.
- **Streaming median**: maintain two heaps (a max-heap of the lower half and a min-heap of the upper half) and balance them as new elements arrive. The same "swap the root when the new element deserves to be in the heap" pattern.
- **A* search** and Dijkstra's algorithm: priority queues over frontier nodes. `heapq` is the workhorse.
- **k-summable sketches and approximate quantiles**: streaming algorithms that estimate quantiles using a heap-of-size-k of "summary" points.

## Common pitfalls

### Forgetting to handle `k = 0`

The heap is empty, the loop does nothing, the result is `[]`. Easy. But the special case needs to be in the implementation.

### Forgetting to handle `k > n`

If `k > n`, the heap grows up to size `n` (never exceeds it) and contains all the elements. The "if heap has fewer than k" branch handles this naturally — every element is pushed. At the end, you sort the heap (which has all elements) and return the whole thing. Don't `IndexError` on the heap's root when the heap is empty.

### Comparing with the wrong side of the inequality

The rule is "if x is larger than the smallest of the top-k, replace". The smallest of the top-k is `heap[0]` (min-heap). The check is `x > heap[0]`, not `x < heap[0]`. The off-by-direction bug is a classic.

### Using a max-heap by accident

If you push negated values and compare wrong, the order of operations gets confused. Stick to the min-heap of size k as described.

### Returning the heap unsorted

The min-heap property says the smallest is at the root, but the rest of the heap is not fully sorted. `sorted(heap, reverse=True)` is required to produce the descending output.

### Using `sorted(nums, reverse=True)[:k]`

This works but is the full-sort approach. The prompt bans it.

## Edge cases

- `k = 0` -> `[]`.
- `k < 0` -> `ValueError`.
- `nums = []` with `k > 0` -> `ValueError`.
- `k >= len(nums)` -> return all elements sorted descending.
- All-same `nums` -> return `k` copies of the value, in any order.
- Negative numbers (the largest is the least-negative).
- Very large `k` (close to `n`): the heap grows to nearly the full input.

## Quick check

`nums = [5, 1, 3, 2, 4]`, `k = 3`.

- Push 5: heap = [5].
- Push 1: heap = [1, 5].
- Push 3: heap = [1, 5, 3]. (k = 3, full.)
- 2 > 1? Yes. Pop 1, push 2: heap = [2, 5, 3].
- 4 > 2? Yes. Pop 2, push 4: heap = [3, 5, 4].

Final heap: [3, 5, 4]. Sorted desc: [5, 4, 3]. ✓

## ML/research connection

The min-heap-of-size-k pattern is the workhorse of top-k predictions in classification (with thousands of classes, sorting the full distribution is wasteful), beam search in sequence-to-sequence decoding, and streaming median in online statistics. The same "swap the root when the new element deserves to be in the heap" logic appears in A* search and Dijkstra's algorithm via priority queues.
