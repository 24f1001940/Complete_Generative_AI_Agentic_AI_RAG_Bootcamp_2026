"""
Lecture 105: FAISS & ChromaDB in Practice
"""

def main():
    try:
        import numpy as np
        import faiss
    except ImportError:
        print("FAISS example requires:")
        print("pip install faiss-cpu numpy")
        return

    vectors = np.array(
        [
            [1.0, 0.0],
            [0.9, 0.1],
            [0.0, 1.0],
        ],
        dtype="float32",
    )

    query = np.array([[1.0, 0.0]], dtype="float32")

    index = faiss.IndexFlatL2(2)
    index.add(vectors)

    distances, indices = index.search(query, k=2)

    print("Nearest indices:", indices)
    print("Distances:", distances)


if __name__ == "__main__":
    main()
