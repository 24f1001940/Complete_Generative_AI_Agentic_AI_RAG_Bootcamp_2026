"""
Lecture 99: Chains, Retrievers & RAG Basics
"""

def main():
    pipeline = [
        "User Query",
        "Retriever",
        "Relevant Documents",
        "Prompt",
        "Language Model",
        "Answer",
    ]

    print("Basic RAG pipeline:")
    print(" -> ".join(pipeline))


if __name__ == "__main__":
    main()
