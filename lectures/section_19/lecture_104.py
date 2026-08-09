"""
Lecture 104: Similarity Search, Vector Stores & Vector Databases
"""

def cosine_similarity(a, b):
    import math

    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)


def main():
    documents = {
        "doc1": [1.0, 0.0, 0.0],
        "doc2": [0.9, 0.1, 0.0],
        "doc3": [0.0, 1.0, 0.0],
    }

    query = [1.0, 0.0, 0.0]

    results = []

    for doc_id, vector in documents.items():
        score = cosine_similarity(query, vector)
        results.append((doc_id, score))

    results.sort(key=lambda item: item[1], reverse=True)

    print("Similarity results:")
    for doc_id, score in results:
        print(f"{doc_id}: {score:.4f}")


if __name__ == "__main__":
    main()
