from __future__ import annotations

from qdrant_client import QdrantClient, models

from src.config import COLLECTION_NAME, ModelSpec


class MultiEmbeddingStore:
    def __init__(self, client: QdrantClient, collection_name: str = COLLECTION_NAME):
        self.client = client
        self.collection_name = collection_name

    def recreate_collection(self, specs: tuple[ModelSpec, ...]) -> None:
        if self.client.collection_exists(self.collection_name):
            self.client.delete_collection(self.collection_name)

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config={
                spec.vector_name: models.VectorParams(
                    size=spec.expected_dimension,
                    distance=models.Distance.COSINE,
                )
                for spec in specs
            },
        )

    def upsert_documents(
        self,
        documents: list[dict],
        vectors_by_name: dict[str, list[list[float]]],
    ) -> None:
        points = []
        for index, document in enumerate(documents):
            point_vectors = {
                vector_name: vectors[index]
                for vector_name, vectors in vectors_by_name.items()
            }
            points.append(
                models.PointStruct(
                    id=document["id"],
                    vector=point_vectors,
                    payload=document,
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
            wait=True,
        )

    def search(self, vector_name: str, query_vector: list[float], limit: int = 5):
        result = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            using=vector_name,
            limit=limit,
            with_payload=True,
        )
        return result.points
