"""
Lecture 90: Prompt Evaluation, Prompt Debugging & Best Practices
"""

def evaluate_prompt(prompt):
    text = prompt.lower()

    return {
        "Contains task": "task:" in text,
        "Contains output guidance": "output:" in text,
        "Contains context": "context:" in text,
        "Has content": bool(prompt.strip()),
    }


def main():
    prompt = """
    Task: Explain RAG.
    Context: The learner is a beginner.
    Output: Three concise bullet points.
    """

    for check, passed in evaluate_prompt(prompt).items():
        print(f"{check}: {passed}")


if __name__ == "__main__":
    main()
