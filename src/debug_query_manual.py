# debug_query.py
from qdrant_client import QdrantClient

client = QdrantClient(
    url="http://localhost:6333"
)

print(
    client.get_collection(
        "poc_multi_embeddings"
    )
)