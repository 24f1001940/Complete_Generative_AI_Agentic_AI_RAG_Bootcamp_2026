"""
Lecture 93: Hugging Face Pipelines & Text Generation
"""

def main():
    try:
        from transformers import pipeline
    except ImportError:
        print("Missing dependency: transformers")
        print("Install with: pip install transformers torch")
        return

    generator = pipeline("text-generation", model="distilgpt2")

    result = generator(
        "Artificial intelligence is",
        max_new_tokens=30,
    )

    print(result)


if __name__ == "__main__":
    main()
