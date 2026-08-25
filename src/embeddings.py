from __future__ import annotations

from sentence_transformers import SentenceTransformer

from src.config import ModelSpec


class EmbeddingRegistry:
    def __init__(self, specs: tuple[ModelSpec, ...]):
        self.specs = specs
        self._models: dict[str, SentenceTransformer] = {}

    def _model(self, spec: ModelSpec) -> SentenceTransformer:
        if spec.vector_name not in self._models:
            model = SentenceTransformer(spec.model_id, device="cpu")
            dimension = model.get_sentence_embedding_dimension()
            if dimension != spec.expected_dimension:
                raise ValueError(
                    f"Dimensão inesperada para {spec.model_id}: "
                    f"esperado={spec.expected_dimension}, obtido={dimension}"
                )
            self._models[spec.vector_name] = model
        return self._models[spec.vector_name]

    def embed_passages(self, spec: ModelSpec, texts: list[str]) -> list[list[float]]:
        prepared = [f"passage: {text}" for text in texts]
        vectors = self._model(spec).encode(
            prepared,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return vectors.tolist()

    def embed_query(self, spec: ModelSpec, query: str) -> list[float]:
        vectors = self._model(spec).encode(
            [f"query: {query}"],
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return vectors[0].tolist()
