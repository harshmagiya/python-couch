# ex10_tree_dfs_inorder

Read: `theory.md` (3-4 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def inorder(root: "Node | None") -> list[int]:
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

- Return the inorder traversal of the binary tree: left subtree, then root, then right subtree.
- The result is a flat `list[int]` of node values in the order visited.
- For an empty tree (`root is None`), return `[]`.
- For a single node, return `[root.val]`.

Inorder is one of the three classical DFS orderings; the others are preorder (root, left, right) and postorder (left, right, root). The exercises use inorder because of its BST invariant (below).

## Examples

- `inorder(None) == []`
- `inorder(Node(1)) == [1]`
- For a tree `1 -> [2, 3]` (root 1, left 2, right 3):
  - Left subtree inorder: `[2]`.
  - Root: `[1]`.
  - Right subtree inorder: `[3]`.
  - Total: `[2, 1, 3]`.
- For a left-skewed tree `1 -> 2 -> 3 -> 4` (each is the left child of the next):
  `inorder(...) == [4, 3, 2, 1]`
- For a right-skewed tree `1 -> 2 -> 3 -> 4` (each is the right child of the next):
  `inorder(...) == [1, 2, 3, 4]`
- For a binary search tree with values `[4, 2, 6, 1, 3, 5, 7]`:
  - Inorder returns the values in **sorted** order: `[1, 2, 3, 4, 5, 6, 7]`.

## Complexity requirement

- O(n) time, where n is the number of nodes.
- O(h) recursion-stack space, where h is the tree height. Worst case O(n) (skewed tree).

## Constraints (for practice)

- Use recursion. The natural form is a helper `def walk(node, out): ...` that appends to an output list.
- The traversal order is strictly **left, root, right** for inorder.
- No `sorted()` shortcut. The point is the recursion.
- An iterative version with an explicit stack is allowed (and the helper-iterative translation is a useful exercise), but the prompt asks for the recursive form.

## Disallowed examples

```python
def inorder(root):                            # WRONG: BFS, not DFS
    if root is None:
        return []
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        out.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    return out
```

BFS produces level-order, not inorder. Even if the test happens to pass on
a specific tree, the algorithm is wrong.

```python
def inorder(root):                            # WRONG: preorder, not inorder
    if root is None:
        return []
    return [root.val] + inorder(root.left) + inorder(root.right)
```

That's preorder: root, left, right. The prompt asks for left, root, right.

```python
def inorder(root):                            # WRONG: postorder, not inorder
    if root is None:
        return []
    return inorder(root.left) + inorder(root.right) + [root.val]
```

That's postorder: left, right, root.

```python
def inorder(root):                            # WRONG: uses sorted() shortcut
    if root is None:
        return []
    return sorted([root.val] + (inorder(root.left) if root.left else [])
                            + (inorder(root.right) if root.right else []))
```

This happens to work for a BST (because inorder of a BST is sorted), but
not for a general binary tree. The recursion is the point; the
`sorted(...)` shortcut is not allowed.

## Hints

- The base case is `node is None`, which returns `[]`.
- The recursive case returns `inorder(node.left) + [node.val] + inorder(node.right)`.
- For a BST, the result is sorted. For a non-BST, it is in the "left, root, right" order — not sorted.
- Tracing on a 3-node tree is the fastest way to internalise the order.
