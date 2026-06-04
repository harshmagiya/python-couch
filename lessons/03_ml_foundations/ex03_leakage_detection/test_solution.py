from testutils import load_solution


solution = load_solution(__file__)


def test_empty_rows():
    assert solution.leakage_columns([], "y") == []


def test_detects_direct_copy_leakage():
    rows = [
        {"y": 1, "a": 1, "b": 0},
        {"y": 0, "a": 0, "b": 0},
        {"y": 1, "a": 1, "b": 1},
    ]
    assert solution.leakage_columns(rows, "y") == ["a"]


def test_no_leakage_when_not_perfect():
    rows = [
        {"y": 1, "a": 1},
        {"y": 0, "a": 1},
    ]
    assert solution.leakage_columns(rows, "y") == []


def test_excludes_label_key():
    rows = [
        {"label": 2, "label_copy": 2, "x": 3},
        {"label": 3, "label_copy": 3, "x": 4},
    ]
    assert solution.leakage_columns(rows, "label") == ["label_copy"]
