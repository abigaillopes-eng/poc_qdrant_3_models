from dataclasses import dataclass

from src.fusion import reciprocal_rank_fusion


@dataclass
class Hit:
    id: int
    payload: dict


def test_rrf_rewards_consensus():
    rankings = {
        "a": [Hit(1, {"title": "A"}), Hit(2, {"title": "B"})],
        "b": [Hit(2, {"title": "B"}), Hit(1, {"title": "A"})],
        "c": [Hit(2, {"title": "B"}), Hit(3, {"title": "C"})],
    }
    fused = reciprocal_rank_fusion(rankings)
    assert fused[0]["id"] == 2
