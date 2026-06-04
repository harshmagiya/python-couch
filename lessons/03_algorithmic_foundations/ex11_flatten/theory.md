# Recursion: Flatten Arbitrarily Nested Lists

## What problem this solves

Take a list whose elements are either an `int` or another list (which itself can contain ints or lists, and so on), and return a flat list of all the ints in depth-first order. This is the "tree traversal, return the leaves in order" problem on the simplest possible tree: one where every internal node is a list and every leaf is an `int`.

## Mental model

A list is a tree:

```
[1, [2, [3, [4]]], 5]
   /      \
  1   [2, [3, [4]]]
        /         \
       2      [3, [4]]
              /     \
             3       4
```

To flatten it:

- For each element:
  - If it's a list, recurse into it and concatenate the result.
  - Otherwise, keep it as a single element.

The recursion bottoms out at empty lists (return `[]`) and at non-list elements (return them as a 1-element list).

## Why it matters in real projects

- "Flatten" is the prototype for tree traversal, JSON path resolution, directory walking, and any "extract all leaf values" query.
- Once you can write this, you can write `map`, `filter`, `reduce` on a tree (replace the append with a transform), and many simple parsers.

## Common pitfalls

### Stopping at one level of nesting

- A non-recursive solution that only peeks one level deep (`for x in sub: ...`) leaves the inner lists untouched. The recursion has to keep going as long as the current element is itself a list.

### Returning a `list` (not a `list[int]`) is fine

- Python doesn't enforce the inner-type at runtime. The tests pass ints; the signature is `list` so the recursion is uniform.

### Building with `out += flatten(item)` is fine

- `list.extend` (or `+=`) is the natural way to splice the recursion result. Building a new list with `out.append(...)` in a loop is also correct.

## Edge cases

- Empty list -> `[]`.
- Already flat -> identity of elements.
- Deeply nested single chain.
- All-nested (no ints at the top level).
- Mixed at every level.
- Empty inner list (`[1, [], 2]`) — should contribute nothing.
- Negative numbers and zero (no special handling needed).

## Quick check

`[1, [2, [3, [4, [5]]]]]`

- flatten([1, [2, [3, [4, [5]]]]])
  -> [1] + flatten([2, [3, [4, [5]]]])
  -> [1] + [2] + flatten([3, [4, [5]]])
  -> [1, 2] + [3] + flatten([4, [5]])
  -> [1, 2, 3] + [4] + flatten([5])
  -> [1, 2, 3, 4, 5]. ✓

## ML/research connection

The recursion-on-tree pattern is the same one used by `pd.json_normalize` (flattening nested JSON columns into a flat table) and by pipeline config loaders that walk nested dicts of hyperparameters. Once you can write this, you can write any "extract all leaf values in DFS order" query that comes up in data-prep code.
