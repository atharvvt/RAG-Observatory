from uuid import uuid4

from app.models import Document, Chunk


class TextChunker:
    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_documents(
        self,
        documents: list[Document],
    ) -> list[Chunk]:

        chunks = []

        for document in documents:
            chunks.extend(
                self._chunk_single_document(document)
            )

        return chunks

    def _chunk_single_document(
        self,
        document: Document,
    ) -> list[Chunk]:

        text = document.text

        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunks.append(
                Chunk(
                    chunk_id=str(uuid4()),
                    text=chunk_text,
                    source=document.source,
                )
            )

            start += (self.chunk_size - self.chunk_overlap)

        return chunks