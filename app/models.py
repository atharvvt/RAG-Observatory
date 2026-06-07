from dataclasses import dataclass


@dataclass
class Document:
    text: str
    source: str


@dataclass
class Chunk:
    chunk_id: str
    text: str
    source: str