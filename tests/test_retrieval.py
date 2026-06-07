from configs.settings import load_config

from app.embedding import EmbeddingModel
from app.retriever import SemanticRetriever

from vector_store.chroma_store import (
    ChromaVectorStore
)

config = load_config()

embedding_model = EmbeddingModel(
    config["embedding"]["model"]
)

vector_store = ChromaVectorStore(
    collection_name=config[
        "vector_store"
    ]["collection_name"],
    persist_directory=config[
        "vector_store"
    ]["persist_directory"],
)

retriever = SemanticRetriever(
    embedding_model=embedding_model,
    vector_store=vector_store,
)

query = "What is retrieval augmented generation?"

results = retriever.retrieve(
    query=query,
    top_k=3,
)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]

for i in range(
    len(documents)
):
    print("\n" + "=" * 80)

    print(
        f"Rank: {i + 1}"
    )

    print(
        f"Source: {metadatas[i]['source']}"
    )

    print(
        f"Distance: {distances[i]}"
    )

    print(
        f"\n{documents[i]}"
    )