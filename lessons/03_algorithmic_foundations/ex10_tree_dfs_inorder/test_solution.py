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
    """Build a binary tree from a list. None entries mean absent nodes."""
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


def _assert_not_bfs(func) -> None:
    """AST-only check. Reject a queue-based BFS that produces level-order."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        # A recursive inorder never uses a queue or a stack. .popleft() and
        # .pop() on a list/deque are the unmistakable BFS/DFS-iterative
        # shapes; both are wrong for this exercise.
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in {"popleft", "pop"}:
                if node.func.value is not None:
                    raise AssertionError(
                        "Do not use a queue/BFS shape in this exercise; "
                        "inorder is a recursive DFS."
                    )


def test_empty():
    assert solution.inorder(None) == []


def test_single_node():
    assert solution.inorder(Node(1)) == [1]
    assert solution.inorder(Node(-5)) == [-5]


def test_two_nodes_left_only():
    #   1
    #  /
    # 2
    assert solution.inorder(Node(1, Node(2))) == [2, 1]


def test_two_nodes_right_only():
    # 1
    #  \
    #   2
    assert solution.inorder(Node(1, None, Node(2))) == [1, 2]


def test_three_nodes_balanced():
    #   2
    #  / \
    # 1   3
    assert solution.inorder(Node(2, Node(1), Node(3))) == [1, 2, 3]


def test_left_skewed():
    # 1 -> 2 -> 3 -> 4 (each is the left child of the next)
    root = Node(1, Node(2, Node(3, Node(4))))
    assert solution.inorder(root) == [4, 3, 2, 1]


def test_right_skewed():
    # 1 -> 2 -> 3 -> 4 (each is the right child of the next)
    root = Node(1, None, Node(2, None, Node(3, None, Node(4))))
    assert solution.inorder(root) == [1, 2, 3, 4]


def test_bst_returns_sorted():
    # A full BST:        4
    #                   / \
    #                  2   6
    #                 / \ / \
    #                1  3 5  7
    root = _from_list([4, 2, 6, 1, 3, 5, 7])
    assert solution.inorder(root) == [1, 2, 3, 4, 5, 6, 7]


def test_non_bst_not_sorted():
    # A non-BST with the same set of values as a balanced BST:
    #         1
    #        / \
    #       3   2
    # The inorder is [3, 1, 2], NOT sorted.
    root = Node(1, Node(3), Node(2))
    assert solution.inorder(root) == [3, 1, 2]


def test_with_negatives_and_duplicates_not_bst():
    # Not a BST (because 5 > 3 is on the left of 3):
    #         3
    #        / \
    #       5   1
    root = Node(3, Node(5), Node(1))
    assert solution.inorder(root) == [5, 3, 1]


def test_unbalanced_with_missing_children():
    #         1
    #        /
    #       2
    #      / \
    #     3   None
    #    /
    #   4
    root = _from_list([1, 2, None, 3, None, 4])
    assert solution.inorder(root) == [4, 3, 2, 1]


def test_constraint_not_bfs():
    _assert_not_bfs(solution.inorder)
