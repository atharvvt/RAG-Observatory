from configs.settings import load_config

from vector_store.chroma_store import (
    ChromaVectorStore
)

config = load_config()

store = ChromaVectorStore(
    collection_name=config[
        "vector_store"
    ]["collection_name"],
    persist_directory=config[
        "vector_store"
    ]["persist_directory"],
)

print(
    f"Chunks in DB: {store.count()}"
)