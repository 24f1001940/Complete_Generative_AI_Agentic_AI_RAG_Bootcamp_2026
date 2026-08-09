"""
Lecture 154: System Optimization: Speed, Memory & Token Efficiency
"""

def estimate_tokens(text):
    # Rough educational estimate, not a tokenizer.
    return max(1, len(text.split()))


def main():
    prompt = (
        "Explain retrieval augmented generation with a short example "
        "and mention two benefits."
    )

    print("Approximate token count:", estimate_tokens(prompt))
    print("Optimization levers:")
    for item in [
        "Reduce unnecessary prompt text",
        "Use appropriate model size",
        "Cache repeated work",
        "Control retrieved context",
        "Stream responses when useful",
    ]:
        print(" -", item)


if __name__ == "__main__":
    main()
