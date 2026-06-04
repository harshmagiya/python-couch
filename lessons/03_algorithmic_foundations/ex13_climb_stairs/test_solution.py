import ast
import inspect
import textwrap

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def _assert_no_full_dp_array(func) -> None:
    """AST-only check. Reject a DP array of length proportional to n."""
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in {"dp", "ways", "table", "memo"}:
                    if isinstance(node.value, ast.ListComp):
                        raise AssertionError(
                            "Do not build a full DP array for this exercise; "
                            "keep only the last two values (O(1) space)."
                        )


def _assert_not_unmemoised_recursion(func) -> None:
    """AST-only check. Reject `return climb_stairs(n-1) + climb_stairs(n-2)`.

    This is exponentially slow and is not the O(n) bottom-up the prompt
    asks for. A `@functools.cache` decorator would make it O(n), but the
    prompt does not request top-down with memo; it asks for bottom-up.
    """
    src = textwrap.dedent(inspect.getsource(func))
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            fn_name = node.name
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name):
                    if sub.func.id == fn_name:
                        # The function calls itself. Now check whether it
                        # has a `@functools.cache` (or `lru_cache`) decorator.
                        has_cache = any(
                            (isinstance(d, ast.Name) and d.id in {"cache", "lru_cache"})
                            or (isinstance(d, ast.Attribute) and d.attr in {"cache", "lru_cache"})
                            for d in node.decorator_list
                        )
                        if not has_cache:
                            raise AssertionError(
                                "Do not use bare recursion in this exercise; "
                                "it is exponentially slow. Use bottom-up with O(1) space."
                            )


def test_zero():
    assert solution.climb_stairs(0) == 1


def test_one():
    assert solution.climb_stairs(1) == 1


def test_two():
    assert solution.climb_stairs(2) == 2


def test_three():
    assert solution.climb_stairs(3) == 3


def test_four():
    assert solution.climb_stairs(4) == 5


def test_five():
    assert solution.climb_stairs(5) == 8


def test_ten():
    assert solution.climb_stairs(10) == 89


def test_negative_raises():
    with pytest.raises(ValueError):
        solution.climb_stairs(-1)


def test_large_input_completes_quickly():
    """O(n) time should complete n=10000 in milliseconds, not seconds."""
    import time
    start = time.perf_counter()
    result = solution.climb_stairs(10000)
    elapsed = time.perf_counter() - start
    assert result > 0
    assert elapsed < 1.0, f"climb_stairs(10000) took {elapsed:.3f}s; expected < 1s"


def test_constraint_no_full_dp_array():
    _assert_no_full_dp_array(solution.climb_stairs)


def test_constraint_not_unmemoised_recursion():
    _assert_not_unmemoised_recursion(solution.climb_stairs)
