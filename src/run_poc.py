from __future__ import annotations

import json

from qdrant_client import QdrantClient

from src.config import COLLECTION_NAME, MODELS, QDRANT_URL
from src.documents import DOCUMENTS, GOLDEN_QUERIES
from src.embeddings import EmbeddingRegistry
from src.evaluation import evaluate_rankings, find_rank
from src.fusion import reciprocal_rank_fusion
from src.qdrant_store import MultiEmbeddingStore


def main() -> None:
    client = QdrantClient(url=QDRANT_URL)
    registry = EmbeddingRegistry(MODELS)
    store = MultiEmbeddingStore(client, COLLECTION_NAME)

    print("1. Criando collection com três named vectors...")
    store.recreate_collection(MODELS)

    texts = [document["text"] for document in DOCUMENTS]
    vectors_by_name = {
        spec.vector_name: registry.embed_passages(spec, texts)
        for spec in MODELS
    }

    print("2. Dimensões geradas:")
    for spec in MODELS:
        print(f"   {spec.vector_name}: {len(vectors_by_name[spec.vector_name][0])}")

    store.upsert_documents(DOCUMENTS, vectors_by_name)

    model_evaluations: dict[str, list[dict]] = {spec.vector_name: [] for spec in MODELS}
    fusion_evaluation: list[dict] = []

    for golden in GOLDEN_QUERIES:
        query = golden["query"]
        expected_id = golden["expected_id"]
        rankings = {}

        print(f"\nQUERY: {query}")
        for spec in MODELS:
            query_vector = registry.embed_query(spec, query)
            hits = store.search(spec.vector_name, query_vector, limit=5)
            rankings[spec.vector_name] = hits
            ids = [int(hit.id) for hit in hits]
            rank = find_rank(ids, expected_id)
            model_evaluations[spec.vector_name].append({"rank": rank})
            print(f"  {spec.vector_name}: ids={ids}, rank_esperado={rank}")

        fused = reciprocal_rank_fusion(rankings)
        fused_ids = [item["id"] for item in fused]
        fused_rank = find_rank(fused_ids, expected_id)
        fusion_evaluation.append({"rank": fused_rank})
        print(f"  FUSÃO RRF: ids={fused_ids}, rank_esperado={fused_rank}")

    summary = {
        model: evaluate_rankings(items)
        for model, items in model_evaluations.items()
    }
    summary["fusion_rrf"] = evaluate_rankings(fusion_evaluation)

    print("\n3. MÉTRICAS")
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    info = client.get_collection(COLLECTION_NAME)
    print("\n4. SCHEMA DA COLLECTION")
    print(info.config.params.vectors)


if __name__ == "__main__":
    main()
