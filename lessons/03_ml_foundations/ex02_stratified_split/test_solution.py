from collections import Counter

from testutils import load_solution


solution = load_solution(__file__)


def test_basic_split_sizes():
    xs = list(range(10))
    ys = [0, 1] * 5
    x_tr, x_te, y_tr, y_te = solution.train_test_split(xs, ys, test_size=0.3, seed=42)
    assert len(x_te) == 3
    assert len(x_tr) == 7
    assert len(y_te) == 3
    assert len(y_tr) == 7


def test_deterministic_seed():
    xs = list(range(20))
    ys = [0] * 10 + [1] * 10
    out1 = solution.train_test_split(xs, ys, test_size=0.25, seed=1)
    out2 = solution.train_test_split(xs, ys, test_size=0.25, seed=1)
    assert out1 == out2


def test_stratify_rough_proportions_binary():
    xs = list(range(100))
    ys = [0] * 90 + [1] * 10
    _, _, _, y_te = solution.train_test_split(xs, ys, test_size=0.2, seed=0, stratify=True)
    c = Counter(y_te)
    # 20 test items, roughly 90/10 split -> expect 18/2
    assert c[0] == 18
    assert c[1] == 2


def test_stratify_multiclass_total_exact():
    xs = list(range(30))
    ys = [0] * 10 + [1] * 10 + [2] * 10
    x_tr, x_te, y_tr, y_te = solution.train_test_split(xs, ys, test_size=1 / 3, seed=123, stratify=True)
    assert len(x_te) == 10
    assert len(x_tr) == 20
    assert Counter(y_te) == {0: 3, 1: 3, 2: 4} or Counter(y_te) == {0: 4, 1: 3, 2: 3} or Counter(y_te) == {0: 3, 1: 4, 2: 3}
