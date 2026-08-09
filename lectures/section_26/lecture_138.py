"""
Lecture 138: Query Transformations: Expansion, Decomposition & HyDE
"""

def expand_query(query):
    return [
        query,
        query + " detailed explanation",
        query + " examples and use cases",
    ]


def decompose(query):
    return [
        f"What are the key concepts in: {query}?",
        f"What examples explain: {query}?",
        f"What limitations should be considered for: {query}?",
    ]


def main():
    query = "retrieval augmented generation"

    print("Expanded queries:")
    for item in expand_query(query):
        print(" -", item)

    print("
Decomposed queries:")
    for item in decompose(query):
        print(" -", item)


if __name__ == "__main__":
    main()
