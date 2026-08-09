"""
Lecture 151: Graph RAG: Combining Knowledge Graphs & Vector Search
"""

def main():
    vector_results = ["AI", "Machine Learning", "Neural Networks"]

    graph_results = [
        ("AI", "includes", "Machine Learning"),
        ("Machine Learning", "uses", "Neural Networks"),
    ]

    print("Vector retrieval:")
    for item in vector_results:
        print(" -", item)

    print("
Graph retrieval:")
    for source, relation, target in graph_results:
        print(f" - {source} --{relation}--> {target}")


if __name__ == "__main__":
    main()
