# Tree DFS: Inorder Traversal

## What problem this solves

Walk a binary tree in the **left, root, right** order and return the node values as a flat list. Inorder is one of three classical DFS orderings (the others are preorder and postorder); it is the one most associated with the **binary search tree** invariant: inorder of a BST is sorted output. Understanding inorder is the entry point to understanding tree shape, the BST invariant, and a wide family of tree-rewriting problems.

## Mental model

The recursion is the cleanest expression:

```
def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)
```

Read it left to right: walk the left subtree, then the root, then the right subtree. The base case is the empty tree, which contributes nothing.

A more efficient (and equally common) form accumulates into a shared output list:

```
def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)
```

Both produce the same answer; the second avoids building intermediate lists.

## The BST invariant

If the tree is a **binary search tree** (every node's left subtree contains only smaller values and every node's right subtree contains only larger values), inorder returns the values in **sorted order**. This is the reason BSTs are shaped the way they are, and the reason `bisect` works the way it does: both rely on the same "left-then-right gives me sorted output" invariant.

## Why it matters in real projects

- Decision-tree feature attribution methods like `TreeSHAP` and `XGBoost`'s built-in attribution walk the tree in inorder (or a related order) to compute per-feature contributions.
- AST traversal in compilers and DSLs uses the same three-order pattern (preorder for "execute on entry", inorder for "execute between children", postorder for "execute on exit").
- `pd.json_normalize` and many data-pipeline shape transformations walk a tree in some DFS order.

## Common pitfalls

### Confusing the three orderings

- **Preorder** (root, left, right): use when you want to act on a node *before* its children. e.g. serialise a tree.
- **Inorder** (left, root, right): use when you want a BST's sorted output, or "between the two subtrees" semantics.
- **Postorder** (left, right, root): use when you want to act on a node *after* its children. e.g. delete a tree (delete children first), or compute a subtree aggregate.

A common bug is to write preorder or postorder and submit it as inorder. The test catches this for non-BST inputs.

### Forgetting the base case

`if node is None: return []` (or `return` in the accumulating form) is the base case. Without it, the recursion descends forever and crashes with a `RecursionError` or `AttributeError` on `None.left`.

### Confusing "inorder is sorted" with "inorder sorts the input"

Inorder does **not** sort the input. It visits nodes in the left-then-right order. The result is sorted **only** if the tree is a BST. For a non-BST, the result is some other ordering, not sorted.

### Using BFS

BFS produces level-order, not inorder. They coincide on a single-path tree (skewed left or right) but diverge as soon as the tree has both children. The test catches this.

### Iterative-with-stack confusion

The iterative form uses a stack and an explicit state machine ("going down" vs "visiting"). It's a separate, harder exercise to translate the recursion into a stack — and the prompt does ask for recursion, not the iterative form.

## Edge cases

- `root is None` -> `[]`.
- Single node -> `[val]`.
- Left-skewed (each node has only a left child) -> the values come out in reverse insertion order.
- Right-skewed -> the values come out in insertion order.
- Full BST -> sorted output.
- Non-BST with the same set of values -> some other order (not sorted).
- A tree where some internal node has only a right child; the left subtree is `None`.

## Quick check

```
        2
       / \
      1   3
```

- inorder(left=1)  = [1]
- root = 2
- inorder(right=3) = [3]
- Total: [1, 2, 3]. ✓

This is also a BST, so the result is sorted — which it is.

A non-BST counter-check:

```
        1
       / \
      3   2
```

- inorder(3) = [3]
- root = 1
- inorder(2) = [2]
- Total: [3, 1, 2]. **Not sorted** (because 1 is not in BST position).

## ML/research connection

Inorder traversal of a BST returns values in sorted order — the same invariant that `bisect` in the stdlib relies on, and the same one that `TreeSHAP` and `XGBoost` decision-tree feature attribution walk to compute per-feature contributions. The "inorder of a BST is sorted" rule is the deep connection between tree shape and binary search; once you have it, you can see it in every decision-tree paper and library.
