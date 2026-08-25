from __future__ import annotations

from collections import defaultdict


def reciprocal_rank_fusion(rankings: dict[str, list], k: int = 60) -> list[dict]:
    scores: dict[int, float] = defaultdict(float)
    payloads: dict[int, dict] = {}
    contributions: dict[int, dict[str, int]] = defaultdict(dict)

    for model_name, hits in rankings.items():
        for rank, hit in enumerate(hits, start=1):
            point_id = int(hit.id)
            scores[point_id] += 1.0 / (k + rank)
            payloads[point_id] = dict(hit.payload or {})
            contributions[point_id][model_name] = rank

    ordered_ids = sorted(scores, key=scores.get, reverse=True)
    return [
        {
            "id": point_id,
            "rrf_score": scores[point_id],
            "payload": payloads[point_id],
            "ranks": contributions[point_id],
        }
        for point_id in ordered_ids
    ]
