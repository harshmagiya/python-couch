import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _from_list(values):
    """Build a binary tree from a list. None entries mean absent nodes.

    Example: _from_list([1, 2, 3, None, 5]) builds
              1
             / \
            2   3
             \
              5
    """
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


def _assert_no_dfs_disguised_as_bfs(func) -> None:
    """AST-only check. Reject a recursive depth-parameterised DFS solution.

    The function must use a queue and the level-boundary pattern. A pure
    recursion with a `depth` argument and `out[depth].append(...)` is
    technically a depth-first traversal that happens to produce level-order
    output, and the prompt bans it.
    """
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        # Look for a `def ... (...)` whose body contains a `def` (a nested
        # function) that recurses.
        if isinstance(node, ast.FunctionDef):
            for child in ast.walk(node):
                if (
                    child is not node
                    and isinstance(child, ast.FunctionDef)
                    and child.name != "__init__"
                ):
                    nested_name = child.name
                    for sub in ast.walk(child):
                        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name):
                            if sub.func.id == nested_name:
                                raise AssertionError(
                                    "Do not use a recursive helper in this exercise; "
                                    "use a queue-based BFS."
                                )


def test_empty():
    assert solution.level_order(None) == []


def test_single_node():
    assert solution.level_order(Node(1)) == [[1]]


def test_two_nodes_left_only():
    #   1
    #  /
    # 2
    root = Node(1, Node(2))
    assert solution.level_order(root) == [[1], [2]]


def test_two_nodes_right_only():
    # 1
    #  \
    #   2
    root = Node(1, None, Node(2))
    assert solution.level_order(root) == [[1], [2]]


def test_three_nodes_balanced():
    #   1
    #  / \
    # 2   3
    root = Node(1, Node(2), Node(3))
    assert solution.level_order(root) == [[1], [2, 3]]


def test_full_three_levels():
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    root = _from_list([1, 2, 3, 4, 5, None, 6])
    assert solution.level_order(root) == [[1], [2, 3], [4, 5, 6]]


def test_left_skewed():
    # 1 -> 2 -> 3 -> 4
    root = Node(1, Node(2, Node(3, Node(4))))
    assert solution.level_order(root) == [[1], [2], [3], [4]]


def test_right_skewed():
    # 1 -> 2 -> 3 -> 4 (each as right child)
    root = Node(1, None, Node(2, None, Node(3, None, Node(4))))
    assert solution.level_order(root) == [[1], [2], [3], [4]]


def test_root_only_with_left_and_right_subtrees_of_different_depths():
    #         1
    #        / \
    #       2   3
    #      /     \
    #     4       5
    #    /
    #   6
    root = _from_list([1, 2, 3, 4, None, None, 5, 6])
    assert solution.level_order(root) == [[1], [2, 3], [4, 5], [6]]


def test_constraint_no_dfs_helper():
    _assert_no_dfs_disguised_as_bfs(solution.level_order)
