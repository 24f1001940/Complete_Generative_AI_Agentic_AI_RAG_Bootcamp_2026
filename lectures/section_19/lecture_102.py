"""
Lecture 102: Introduction to embeddings
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
    vector_a = [1.0, 2.0, 3.0]
    vector_b = [1.1, 2.1, 3.1]

    print("Cosine similarity:", cosine_similarity(vector_a, vector_b))


if __name__ == "__main__":
    main()
