import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_empty_text():
    assert solution.parse_kv_lines("") == {}


def test_ignores_empty_lines_and_comments():
    text = "\n  # comment\n\n a=1 \n#x\n b = 2\n"
    assert solution.parse_kv_lines(text) == {"a": "1", "b": "2"}


def test_last_key_wins():
    text = "a=1\na=2\na=3\n"
    assert solution.parse_kv_lines(text) == {"a": "3"}


def test_value_may_contain_equals():
    text = "token = a=b=c\n"
    assert solution.parse_kv_lines(text) == {"token": "a=b=c"}


def test_missing_equals_raises_value_error():
    with pytest.raises(ValueError):
        solution.parse_kv_lines("a:1\n")


def test_empty_key_raises_value_error():
    with pytest.raises(ValueError):
        solution.parse_kv_lines("   =x\n")
