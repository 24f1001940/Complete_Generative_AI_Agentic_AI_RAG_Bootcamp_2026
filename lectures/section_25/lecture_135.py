"""
Lecture 135: Vector Stores: ChromaDB, FAISS, Pinecone & AstraDB
"""

def main():
    stores = [
        "ChromaDB",
        "FAISS",
        "Pinecone",
        "AstraDB",
    ]

    print("Vector-store options discussed in this lecture:")
    for store in stores:
        print(" -", store)

    print("\nSelection depends on deployment, scale, persistence,")
    print("latency, filtering, and operational requirements.")


if __name__ == "__main__":
    main()
