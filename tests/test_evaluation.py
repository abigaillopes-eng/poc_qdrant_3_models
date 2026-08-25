from src.evaluation import evaluate_rankings, find_rank


def test_find_rank():
    assert find_rank([5, 2, 9], 2) == 2
    assert find_rank([5, 2, 9], 7) == 0


def test_metrics():
    metrics = evaluate_rankings([{"rank": 1}, {"rank": 2}, {"rank": 0}])
    assert metrics["accuracy_at_1"] == 1 / 3
    assert metrics["recall_at_3"] == 2 / 3
