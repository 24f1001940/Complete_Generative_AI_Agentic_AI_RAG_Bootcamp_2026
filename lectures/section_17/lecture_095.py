"""
Lecture 95: Hugging Face NLP Pipelines & Practical Integration Project
"""

def main():
    try:
        from transformers import pipeline
    except ImportError:
        print("Missing dependency: transformers")
        print("Install with: pip install transformers torch")
        return

    classifier = pipeline("sentiment-analysis")

    reviews = [
        "The product is excellent.",
        "The service was disappointing.",
    ]

    for review in reviews:
        print("\nReview:", review)
        print("Result:", classifier(review))


if __name__ == "__main__":
    main()
