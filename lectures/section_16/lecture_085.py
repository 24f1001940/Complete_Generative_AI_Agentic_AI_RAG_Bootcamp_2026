"""
Lecture 85: Prompt Engineering Fundamentals
"""

def create_prompt(task, context, output_format):
    return f"""
Task:
{task}

Context:
{context}

Output format:
{output_format}
""".strip()


def main():
    prompt = create_prompt(
        "Explain RAG to a beginner",
        "The learner knows Python but is new to GenAI",
        "Three concise bullet points",
    )

    print(prompt)


if __name__ == "__main__":
    main()
