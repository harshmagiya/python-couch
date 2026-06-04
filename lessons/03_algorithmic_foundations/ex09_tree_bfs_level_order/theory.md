# Tree BFS: Level-Order Traversal

## What problem this solves

Walk a binary tree one level at a time, top-down, and group the values by level. The result is a list of lists: `out[i]` is the values at level `i`, left-to-right. This is the workhorse for "report by layer" algorithms and the natural starting point for the entire BFS-on-trees family.

## Mental model

A **queue** holds the nodes waiting to be processed. The invariant: at any moment, the queue contains exactly the nodes of the *current* level followed by the nodes of the *next* level (and possibly further levels, but those will be drained in order).

The classic BFS loop is:

1. Snapshot `level_size = len(queue)`.
2. Inner loop, `level_size` iterations:
   - Pop the leftmost node.
   - Append its value to the *current* inner list.
   - Push its children (if any) to the right of the queue.
3. After the inner loop, the queue holds only the next level's nodes. Append the current inner list to the output and reset.

When the queue is empty, the traversal is done.

```
tree:
        1
       / \
      2   3
     / \   \
    4   5   6

queue starts: [1]
level_size = 1
  pop 1, out=[[1]]; push 2, 3 -> queue=[2, 3]
level_size = 2
  pop 2, inner=[2]; push 4, 5 -> queue=[3, 4, 5]
  pop 3, inner=[2,3]; push 6 -> queue=[4, 5, 6]
  out=[[1], [2, 3]]
level_size = 3
  pop 4, inner=[4]; no children -> queue=[5, 6]
  pop 5, inner=[4, 5]; no children -> queue=[6]
  pop 6, inner=[4, 5, 6]; no children -> queue=[]
  out=[[1], [2, 3], [4, 5, 6]]
queue empty, done.
```

## Why it matters in real projects

- BFS on trees is the same algorithm as BFS on graphs (just specialised for the tree case where you don't need a `visited` set).
- "Level-order" problems in interviews and production code: right-side view, average of each level, connect same-level nodes with next pointers, find the minimum depth, etc.
- Decision-tree layer-by-layer evaluation: in some ML systems you process a tree level by level for parallelism (e.g. batched inference on GPU).
- BFS-based graph neural networks: many GNN aggregation schemes walk a graph level by level.

## Common pitfalls

### Forgetting the level boundary

If you just drain the queue in one big loop and push children as you go, you get a single flat list — not the per-level grouping the prompt requires. Always snapshot `len(queue)` *before* the inner loop.

### Using a list as a queue

`list.pop(0)` is O(n). Use `collections.deque` and `popleft()`, which is O(1).

### Using a stack by accident

`list.pop()` (right-end) is a stack, not a queue. DFS order, not BFS. Use `popleft()`.

### Using recursion to emulate BFS

A depth-parameterised DFS that records the depth of each visit *happens* to produce level-order output for this particular problem, but it traverses the tree in the wrong order. The "right side view of a binary tree" problem, for instance, distinguishes them clearly. The queue is the right tool.

### Including `None` children in the queue

You can choose to push `None` children and skip them at pop time, or skip them at push time. Either works; pushing only non-`None` children is cleaner.

## Edge cases

- `root is None` -> `[]`.
- Single node -> `[[val]]`.
- Left-skewed tree (each node has only a left child) -> each level is `[val]`.
- Right-skewed tree (each node has only a right child) -> same.
- Full binary tree.
- Tree where some levels are incomplete (e.g. parent has only a left child; the right child is `None`).

## Quick check

```
        1
       / \
      2   3
     / \   \
    4   5   6
```

- Level 0: `[1]`.
- Level 1: `[2, 3]`.
- Level 2: `[4, 5, 6]`.

Output: `[[1], [2, 3], [4, 5, 6]]`. ✓

## ML/research connection

Level-order traversal is the same pattern as BFS in graph algorithms; in ML it appears in decision-tree layer-by-layer evaluation (where you process a tree level by level for parallelism, e.g. batched inference on GPU) and in BFS-based graph neural network aggregations (where the k-th "layer" of message passing is exactly the k-th BFS level).
