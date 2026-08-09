"""
Lecture 106: Retriever Fundamentals & Retrieval Pipelines
"""

def retrieve(documents, query):
    query_words = set(query.lower().split())
    scored = []

    for document in documents:
        words = set(document.lower().split())
        score = len(query_words.intersection(words))
        scored.append((score, document))

    return sorted(scored, key=lambda item: item[0], reverse=True)


def main():
    documents = [
        "Python is useful for AI",
        "RAG uses retrieval and generation",
        "Vector databases store embeddings",
    ]

    results = retrieve(documents, "AI Python")

    print("Retrieved documents:")
    for score, document in results:
        print(f"{score} -> {document}")


if __name__ == "__main__":
    main()
