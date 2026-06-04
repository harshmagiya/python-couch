# ex09_tree_bfs_level_order

Read: `theory.md` (3-4 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def level_order(root: "Node | None") -> list[list[int]]:
    ...
```

The `Node` class for a binary tree is defined for you in `test_solution.py`:

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

Behavior:

- Return a list of lists. The outer list has one entry per *level* of the tree (top-down). The inner list at index `i` is the values at level `i`, left-to-right.
- For an empty tree (`root is None`), return `[]`.
- For a single node, return `[[root.val]]`.

## Examples

- `level_order(None) == []`
- `level_order(Node(1)) == [[1]]`
- For a tree `1 -> [2, 3]` (root 1, left 2, right 3): `level_order(...) == [[1], [2, 3]]`
- For a tree
  ```
        1
       / \
      2   3
     / \   \
    4   5   6
  ```
  `level_order(...) == [[1], [2, 3], [4, 5, 6]]`
- For a left-skewed tree `1 -> 2 -> 3 -> 4` (each node's right is None, left is the next):
  `level_order(...) == [[1], [2], [3], [4]]`

## Complexity requirement

- O(n) time, where n is the number of nodes.
- O(n) worst-case space for the queue (the last level can hold up to n/2 nodes in a full tree).

## Constraints (for practice)

- Use a `collections.deque` as the queue. The "level boundary" pattern: record the queue's length *before* the inner loop, then drain exactly that many items, pushing their children to the back of the queue for the next level.
- No recursion that emulates BFS by collecting levels from a depth-parameterised DFS. The point of the exercise is the queue.

## Disallowed examples

```python
def level_order(root):                            # WRONG: this is DFS, not BFS
    out: list[list[int]] = []

    def dfs(node, depth):
        if node is None:
            return
        if len(out) == depth:
            out.append([])
        out[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return out
```

The DFS above happens to produce the same answer for this exercise, but it
traverses depth-first, not breadth-first. The exercise is about practising
the *queue* pattern. The DFS shape is also banned for a deeper reason:
it scales poorly to "level-order variant" problems (e.g. "right side view",
"average of each level") where the order of operations inside the level
matters and the queue pattern is the natural fit.

```python
def level_order(root):                            # WRONG: stack, not queue (DFS)
    if root is None:
        return []
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        out.append(node.val)                       # also: this flattens levels
        if node.right: stack.append(node.right)
        if node.left:  stack.append(node.left)
    return out
```

A `list.pop()` is a stack, not a queue, so this is depth-first order, not
breadth-first. It also flattens levels into a single list, which violates
the per-level grouping required by the prompt.

## Hints

- At each iteration of the outer `while` loop, snapshot the queue's current size — that's the number of nodes on the current level.
- Inner loop: pop exactly that many nodes, append their values to the inner list, push their children to the queue.
- The inner list is the *current* level. When the inner loop exits, the queue holds the *next* level.
