"""
Lecture 84: Model Capabilities, Limitations, Hallucinations & Context Windows
"""

def main():
    capabilities = [
        "Text generation",
        "Summarization",
        "Classification",
        "Question answering",
        "Code generation",
    ]

    limitations = [
        "Hallucinations",
        "Finite context window",
        "Prompt sensitivity",
        "Knowledge limitations",
    ]

    print("Capabilities:")
    for item in capabilities:
        print(" -", item)

    print("\nLimitations:")
    for item in limitations:
        print(" -", item)


if __name__ == "__main__":
    main()
