"""
Lecture 150: Cypher Query Language & LangChain Graph Ingestion
"""

def main():
    queries = [
        "CREATE (p:Person {name: 'Alex'})",
        "MATCH (p:Person) RETURN p",
        "MATCH (p:Person)-[:KNOWS]->(f:Person) RETURN p, f",
    ]

    print("Example Cypher queries:")
    for query in queries:
        print(query)


if __name__ == "__main__":
    main()
