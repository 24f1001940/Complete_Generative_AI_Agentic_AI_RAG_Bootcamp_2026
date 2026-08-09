"""
RAG ingestion demonstration
"""

from pathlib import Path


def main():
    sample = Path("sample_document.txt")
    sample.write_text(
        "RAG combines retrieval with generation. "
        "Documents are ingested, split, embedded, and indexed.",
        encoding="utf-8",
    )

    text = sample.read_text(encoding="utf-8")

    chunk_size = 60
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    print("Created chunks:")
    for number, chunk in enumerate(chunks, 1):
        print(f"{number}: {chunk}")


if __name__ == "__main__":
    main()
