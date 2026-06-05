from dataclasses import dataclass
from pathlib import Path


@dataclass
class Document:
    content: str
    source: str
    file_type: str