from testutils import load_solution


solution = load_solution(__file__)


def test_confusion_counts_perfect():
    y_true = [1, 0, 1, 0]
    y_pred = [1, 0, 1, 0]
    assert solution.confusion_counts(y_true, y_pred) == (2, 0, 2, 0)


def test_confusion_counts_mixed():
    y_true = [1, 1, 0, 0, 1]
    y_pred = [1, 0, 1, 0, 0]
    # tp=1 (idx0), fp=1 (idx2), tn=1 (idx3), fn=2 (idx1, idx4)
    assert solution.confusion_counts(y_true, y_pred) == (1, 1, 1, 2)


def test_confusion_counts_nondefault_positive():
    y_true = [2, 2, 1, 1]
    y_pred = [2, 1, 2, 1]
    assert solution.confusion_counts(y_true, y_pred, positive=2) == (1, 1, 1, 1)


def test_precision_recall_f1_basic():
    y_true = [1, 1, 0, 0, 1]
    y_pred = [1, 0, 1, 0, 0]
    p, r, f1 = solution.precision_recall_f1(y_true, y_pred)
    assert p == 0.5  # 1 / (1+1)
    assert r == 1 / 3
    assert round(f1, 10) == round(2 * p * r / (p + r), 10)


def test_precision_recall_f1_zero_denoms():
    y_true = [0, 0, 0]
    y_pred = [0, 0, 0]
    assert solution.precision_recall_f1(y_true, y_pred) == (0.0, 0.0, 0.0)
