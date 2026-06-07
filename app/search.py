from configs.settings import load_config

from app.embedding import EmbeddingModel
from app.retriever import SemanticRetriever

from vector_store.chroma_store import (
    ChromaVectorStore
)


def main():

    config = load_config()

    embedding_model = (
        EmbeddingModel(
            config["embedding"]["model"]
        )
    )

    vector_store = (
        ChromaVectorStore(
            collection_name=config[
                "vector_store"
            ]["collection_name"],
            persist_directory=config[
                "vector_store"
            ]["persist_directory"],
        )
    )

    retriever = (
        SemanticRetriever(
            embedding_model,
            vector_store,
        )
    )

    while True:

        query = input(
            "\nAsk a question (q to quit): "
        )

        if query.lower() == "q":
            break

        results = retriever.retrieve(
            query,
            top_k=3,
        )

        docs = results[
            "documents"
        ][0]

        print("\nResults:\n")

        for i, doc in enumerate(
            docs,
            start=1,
        ):
            print(
                f"\n[{i}] {doc[:300]}"
            )


if __name__ == "__main__":
    main()
    