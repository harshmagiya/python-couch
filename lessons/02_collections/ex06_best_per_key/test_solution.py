from testutils import load_solution


solution = load_solution(__file__)


def test_empty():
    assert solution.best_per_category([]) == {}


def test_single_category_picks_highest_score():
    records = [("fruit", "apple", 5), ("fruit", "banana", 7), ("fruit", "pear", 6)]
    assert solution.best_per_category(records) == {"fruit": ("banana", 7)}


def test_multiple_categories():
    records = [
        ("fruit", "apple", 5),
        ("veg", "carrot", 3),
        ("fruit", "banana", 7),
        ("veg", "beet", 10),
    ]
    assert solution.best_per_category(records) == {"fruit": ("banana", 7), "veg": ("beet", 10)}


def test_tie_breaker_item_lexicographic():
    records = [("x", "b", 2), ("x", "a", 2), ("x", "c", 2)]
    assert solution.best_per_category(records) == {"x": ("a", 2)}


def test_tie_breaker_applies_only_on_equal_score():
    records = [("x", "a", 1), ("x", "b", 2)]
    assert solution.best_per_category(records) == {"x": ("b", 2)}
