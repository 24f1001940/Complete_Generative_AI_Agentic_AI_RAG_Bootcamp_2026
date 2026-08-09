"""
Lecture 103: Embedding Models: OpenAI, Ollama & Hugging Face
"""

def main():
    providers = {
        "OpenAI": "API-based embedding models",
        "Ollama": "Local model ecosystem",
        "Hugging Face": "Large ecosystem of open models",
    }

    for provider, description in providers.items():
        print(f"{provider}: {description}")


if __name__ == "__main__":
    main()
