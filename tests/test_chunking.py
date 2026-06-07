from app.ingestion import DocumentLoader
from app.chunking import TextChunker


loader = DocumentLoader()

documents = loader.load_directory("data/raw")


chunker = TextChunker(
    chunk_size=100,
    chunk_overlap=20,
)

chunks = chunker.chunk_documents(documents)

print(f"\nCreated {len(chunks)} chunks\n")

for chunk in chunks[:5]:
    print("=" * 50)
    print(chunk.chunk_id)
    print(chunk.source)
    print(chunk.text)