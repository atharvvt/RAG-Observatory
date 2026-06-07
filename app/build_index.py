from app.ingestion import DocumentLoader
from app.chunking import TextChunker
from app.embedding import EmbeddingModel

from vector_store.chroma_store import (
    ChromaVectorStore
)

from configs.settings import load_config


def main():

    config = load_config()

    loader = DocumentLoader()

    documents = loader.load_directory("data/raw")

    chunker = TextChunker(
        chunk_size=config["chunking"]["chunk_size"],
        chunk_overlap=config["chunking"]["chunk_overlap"],
    )

    chunks = chunker.chunk_documents(documents)

    print(f"Created {len(chunks)} chunks")

    embedding_model = EmbeddingModel(config["embedding"]["model"])

    embeddings = ( embedding_model.embed_texts([c.text for c in chunks]))

    store = ChromaVectorStore(
        collection_name=config["vector_store"]["collection_name"],
        persist_directory=config["vector_store"]["persist_directory"],
    )

    store.add_chunks(chunks,embeddings)

    print(f"Stored {store.count()} chunks")


if __name__ == "__main__":
    main()