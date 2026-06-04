import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_uses_heapq(func) -> None:
    """The solution module must use heapq; the prompt requires the heap pattern.

    We check the *module* source (which includes the import at the top)
    rather than just the function source. The import is conventionally
    at module level.
    """
    import inspect as _inspect
    module = _inspect.getmodule(func)
    if module is None:
        raise AssertionError("Could not locate the solution module.")
    src = textwrap.dedent(_inspect.getsource(module))
    tree = ast.parse(src)
    has_import = False
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "heapq":
            has_import = True
            break
        if isinstance(node, ast.Import) and any(
            alias.name.split(".")[0] == "heapq" for alias in node.names
        ):
            has_import = True
            break
    if not has_import:
        raise AssertionError(
            "Import the heapq module for this exercise. The min-heap-of-size-k "
            "pattern is the whole point."
        )


def _assert_not_full_sort(func) -> None:
    """Reject `sorted(nums, reverse=True)[:k]` — the full-sort approach."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "sorted":
                # Check if the slice `[:k]` (or similar) is applied.
                # We allow `sorted(heap, reverse=True)` (where heap is
                # built up via heapq), but reject `sorted(nums, ...)[:k]`.
                # The argument must NOT be the input parameter `nums`.
                if node.args and isinstance(node.args[0], ast.Name):
                    if node.args[0].id in {"nums", "data", "arr", "input_list"}:
                        # Check the parent context for a slice.
                        # We can't easily walk up the tree, so we use a
                        # different approach: check that the function
                        # body contains a `heappush` or `heappop` call.
                        has_heap_call = False
                        for sub in ast.walk(tree):
                            if isinstance(sub, ast.Call):
                                func_repr = ast.unparse(sub.func) if hasattr(ast, "unparse") else ""
                                if "heap" in func_repr:
                                    has_heap_call = True
                                    break
                        if not has_heap_call:
                            raise AssertionError(
                                "Do not use `sorted(nums, ...)` as the main approach; "
                                "the heap is the point of the exercise."
                            )


def test_k_zero():
    assert solution.top_k([1, 2, 3], 0) == []


def test_k_negative_raises():
    with pytest.raises(ValueError):
        solution.top_k([1, 2, 3], -1)


def test_empty_nums_k_positive_raises():
    with pytest.raises(ValueError):
        solution.top_k([], 1)


def test_empty_nums_k_zero():
    assert solution.top_k([], 0) == []


def test_canonical():
    assert solution.top_k([5, 1, 3, 2, 4], 3) == [5, 4, 3]


def test_k_equals_n():
    assert solution.top_k([3, 1, 2], 3) == [3, 2, 1]


def test_k_greater_than_n():
    assert solution.top_k([1, 2, 3], 5) == [3, 2, 1]


def test_single_element():
    assert solution.top_k([7], 1) == [7]


def test_negatives():
    assert solution.top_k([-1, -5, -2, -3], 2) == [-1, -2]


def test_all_same():
    # All equal; any ordering is fine. Set comparison.
    out = solution.top_k([5, 5, 5, 5], 2)
    assert sorted(out) == [5, 5]


def test_descending_input():
    assert solution.top_k([9, 8, 7, 6, 5], 3) == [9, 8, 7]


def test_ascending_input():
    assert solution.top_k([1, 2, 3, 4, 5], 3) == [5, 4, 3]


def test_unsorted_input():
    out = solution.top_k([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 4)
    assert sorted(out) == [9, 6, 5, 5]
    # Verify it's the largest 4 (with ties).
    assert out == [9, 6, 5, 5]


def test_large_n_small_k_completes_quickly():
    """O(n log k) on n=100000, k=10 should be milliseconds."""
    import random
    import time
    random.seed(0)
    nums = [random.randint(0, 10**9) for _ in range(100000)]
    start = time.perf_counter()
    out = solution.top_k(nums, 10)
    elapsed = time.perf_counter() - start
    assert len(out) == 10
    assert out == sorted(out, reverse=True)
    assert elapsed < 1.0, f"top_k(100000, 10) took {elapsed:.3f}s; expected < 1s"


def test_constraint_uses_heapq():
    _assert_uses_heapq(solution.top_k)


def test_constraint_not_full_sort():
    _assert_not_full_sort(solution.top_k)
