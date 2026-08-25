from dataclasses import dataclass


@dataclass(frozen=True)
class ModelSpec:
    vector_name: str
    model_id: str
    expected_dimension: int


MODELS = (
    ModelSpec("e5_small_384", "intfloat/multilingual-e5-small", 384),
    ModelSpec("e5_base_768", "intfloat/multilingual-e5-base", 768),
    ModelSpec("e5_large_1024", "intfloat/multilingual-e5-large", 1024),
)

COLLECTION_NAME = "poc_multi_embeddings"
QDRANT_URL = "http://localhost:6333"
