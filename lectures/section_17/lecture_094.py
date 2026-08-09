"""
Lecture 94: Choosing the Right Hugging Face Model
"""

def choose_model(task):
    models = {
        "sentiment": "Sequence classification model",
        "generation": "Causal language model",
        "embedding": "Sentence embedding model",
        "summarization": "Sequence-to-sequence model",
        "translation": "Translation model",
    }

    return models.get(task, "Search Hugging Face for the required task.")


def main():
    for task in [
        "sentiment",
        "generation",
        "embedding",
        "summarization",
        "translation",
    ]:
        print(f"{task}: {choose_model(task)}")


if __name__ == "__main__":
    main()
