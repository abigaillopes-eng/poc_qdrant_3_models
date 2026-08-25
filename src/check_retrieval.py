# check_retrieval.py

from qdrant_client import QdrantClient

client = QdrantClient(
    url="http://localhost:6333"
)

info = client.get_collection(
    "poc_multi_embeddings"
)

print(info)