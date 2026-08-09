"""
Lecture 159: Project 1: Multi-Document RAG Q&A Engine with Semantic Citations
"""

from dataclasses import dataclass


@dataclass
class Document:
    source: str
    text: str


def retrieve(documents, keyword):
    keyword = keyword.lower()
    return [
        doc for doc in documents
        if keyword in doc.text.lower()
    ]


def main():
    documents = [
        Document("python.txt", "Python is widely used in AI."),
        Document("rag.txt", "RAG retrieves context before generation."),
        Document("agents.txt", "Agents can use tools to complete tasks."),
    ]

    query = "RAG"
    matches = retrieve(documents, query)

    print("Answer context:")
    for doc in matches:
        print(f"[Source: {doc.source}] {doc.text}")


if __name__ == "__main__":
    main()
