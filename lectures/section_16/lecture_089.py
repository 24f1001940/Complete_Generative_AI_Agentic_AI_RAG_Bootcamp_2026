"""
Lecture 89: Output Control & Prompt Templates
"""

TEMPLATE = """
You are an AI assistant.

Question:
{question}

Answer format:
{format_style}
"""


def main():
    prompt = TEMPLATE.format(
        question="What is RAG?",
        format_style="exactly three bullet points",
    )

    print(prompt.strip())


if __name__ == "__main__":
    main()
