"""
Lecture 91: Introduction to Hugging Face & Transformers Ecosystem
"""

def main():
    try:
        from transformers import pipeline
    except ImportError:
        print("Missing dependency: transformers")
        print("Install with: pip install transformers torch")
        return

    classifier = pipeline("sentiment-analysis")
    result = classifier("I really enjoyed this course.")

    print(result)


if __name__ == "__main__":
    main()
