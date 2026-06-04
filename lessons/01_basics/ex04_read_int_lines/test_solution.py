from pathlib import Path

import pytest

from testutils import load_solution


solution = load_solution(__file__)


def test_reads_ints_ignoring_blanks_and_comments(tmp_path: Path):
    p = tmp_path / "nums.txt"
    p.write_text("# counts\n10\n -3\n\n7\n  # trailing comment line\n", encoding="utf-8")
    assert solution.read_int_lines(p) == [10, -3, 7]


def test_invalid_int_raises_value_error_with_line_number(tmp_path: Path):
    p = tmp_path / "nums.txt"
    p.write_text("1\n2\nnope\n4\n", encoding="utf-8")

    with pytest.raises(ValueError) as exc:
        solution.read_int_lines(p)

    msg = str(exc.value).lower()
    assert "line" in msg
    assert "3" in msg


def test_plus_sign_ok(tmp_path: Path):
    p = tmp_path / "nums.txt"
    p.write_text("+5\n", encoding="utf-8")
    assert solution.read_int_lines(p) == [5]
