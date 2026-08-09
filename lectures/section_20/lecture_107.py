"""
Lecture 107: Simple GenAI app using Ollama
"""

def main():
    try:
        import requests
    except ImportError:
        print("Missing dependency: requests")
        print("Install with: pip install requests")
        return

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3.2",
        "prompt": "Explain RAG in one sentence.",
        "stream": False,
    }

    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        print("Model response:")
        print(data.get("response", data))
    except requests.RequestException as exc:
        print("Could not reach Ollama.")
        print("Make sure Ollama is running and the selected model is available.")
        print("Error:", exc)


if __name__ == "__main__":
    main()
