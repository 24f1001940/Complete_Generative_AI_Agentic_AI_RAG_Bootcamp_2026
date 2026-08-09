"""
Lecture 114: Working with retriever + vector store
"""

def similarity(a, b):
    import math

    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))

    return dot / (na * nb) if na and nb else 0.0


def main():
    documents = {
        "python.txt": [1.0, 0.0, 0.0],
        "rag.txt": [0.9, 0.1, 0.0],
        "cooking.txt": [0.0, 1.0, 0.0],
    }

    query = [1.0, 0.0, 0.0]

    ranked = sorted(
        (
            (name, similarity(query, vector))
            for name, vector in documents.items()
        ),
        key=lambda item: item[1],
        reverse=True,
    )

    print("Retrieved documents:")
    for name, score in ranked:
        print(f"{name}: {score:.4f}")


if __name__ == "__main__":
    main()
