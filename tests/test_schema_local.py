from typing import Any, cast

from qdrant_client import QdrantClient

from src.config import MODELS
from src.qdrant_store import MultiEmbeddingStore


def test_collection_accepts_named_vectors_with_different_dimensions():
    client = QdrantClient(":memory:")
    store = MultiEmbeddingStore(client, "test_multi_dims")
    store.recreate_collection(MODELS)
    info = client.get_collection("test_multi_dims")
    vectors = info.config.params.vectors
    assert vectors is not None
    named_vectors = cast(dict[str, Any], vectors)
    assert named_vectors["e5_small_384"].size == 384
    assert named_vectors["e5_base_768"].size == 768
    assert named_vectors["e5_large_1024"].size == 1024
