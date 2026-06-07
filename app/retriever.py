from app.embedding import EmbeddingModel

from vector_store.chroma_store import (
    ChromaVectorStore
)


class SemanticRetriever:

    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: ChromaVectorStore,
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_embedding = (
            self.embedding_model.embed_query(
                query
            )
        )

        results = (
            self.vector_store.search(
                query_embedding=query_embedding,
                top_k=top_k,
            )
        )

        return results