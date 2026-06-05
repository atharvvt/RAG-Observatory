from app.ingestion import DocumentLoader


def main():

    loader = DocumentLoader()

    documents = loader.load_directory(
        "data/raw"
    )

    print(
        f"\nLoaded {len(documents)} documents\n"
    )

    for doc in documents:

        print("=" * 50)

        print(
            f"Source: {doc.source}"
        )

        print(
            f"Type: {doc.file_type}"
        )

        print(
            f"Length: {len(doc.content)} chars"
        )

        print(
            doc.content[:150]
        )

        print()


if __name__ == "__main__":
    main()