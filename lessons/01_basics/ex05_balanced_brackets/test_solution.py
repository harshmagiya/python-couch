import pytest

from testutils import load_solution


solution = load_solution(__file__)


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", True),
        ("()", True),
        ("([])", True),
        ("([{}])", True),
        ("([)]", False),
        ("]", False),
        ("(", False),
        ("a + (b * [c])", True),
        ("{[()]}{}", True),
        ("{[()]}{", False),
    ],
)
def test_is_balanced_cases(s: str, expected: bool):
    assert solution.is_balanced(s) is expected
