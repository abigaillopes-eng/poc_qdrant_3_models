from __future__ import annotations


def evaluate_rankings(results_by_query: list[dict]) -> dict:
    total = len(results_by_query)
    hit_at_1 = sum(item["rank"] == 1 for item in results_by_query)
    hit_at_3 = sum(1 <= item["rank"] <= 3 for item in results_by_query)
    reciprocal_rank_sum = sum(1.0 / item["rank"] for item in results_by_query if item["rank"])
    return {
        "queries": total,
        "accuracy_at_1": hit_at_1 / total if total else 0.0,
        "recall_at_3": hit_at_3 / total if total else 0.0,
        "mrr": reciprocal_rank_sum / total if total else 0.0,
    }


def find_rank(ids: list[int], expected_id: int) -> int:
    try:
        return ids.index(expected_id) + 1
    except ValueError:
        return 0
