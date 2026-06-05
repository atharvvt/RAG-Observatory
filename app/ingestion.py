from pathlib import Path

from pypdf import PdfReader

from app.models import Document


class DocumentLoader:

    SUPPORTED_EXTENSIONS = {
        ".txt",
        ".md",
        ".pdf",
    }

    def load_directory(self, directory: str) -> list[Document]:
        documents = []

        directory_path = Path(directory)

        for file_path in directory_path.iterdir():

            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                continue

            document = self.load_file(file_path)

            if document:
                documents.append(document)

        return documents

    def load_file(self, file_path: Path) -> Document | None:

        suffix = file_path.suffix.lower()

        try:

            if suffix in [".txt", ".md"]:

                text = file_path.read_text(
                    encoding="utf-8"
                )

            elif suffix == ".pdf":

                text = self._read_pdf(file_path)

            else:
                return None

            return Document(
                content=text,
                source=file_path.name,
                file_type=suffix,
            )

        except Exception as e:

            print(
                f"Error reading {file_path}: {e}"
            )

            return None

    def _read_pdf(self, file_path: Path) -> str:

        reader = PdfReader(str(file_path))

        pages = []

        for page in reader.pages:
            pages.append(page.extract_text())

        return "\n".join(pages)