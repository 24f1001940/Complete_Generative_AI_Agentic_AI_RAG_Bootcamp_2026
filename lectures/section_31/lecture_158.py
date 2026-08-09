"""
Lecture 158: System Design: Context Engineering & Production Memory
"""

def build_context(system, memory, retrieved, user_query):
    return {
        "system": system,
        "memory": memory,
        "retrieved_context": retrieved,
        "user_query": user_query,
    }


def main():
    context = build_context(
        "You are a helpful assistant.",
        ["User prefers concise answers."],
        ["RAG retrieves relevant information."],
        "What is RAG?",
    )

    for key, value in context.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
