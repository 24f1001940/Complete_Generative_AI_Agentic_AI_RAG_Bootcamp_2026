"""
Lecture 118: API-based model integration
"""

import os


def main():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("GROQ_API_KEY is not set.")
        print("Set it in your environment before making a Groq API call.")
        print("The script is intentionally not sending a request without a key.")
        return

    try:
        from groq import Groq
    except ImportError:
        print("Missing dependency: groq")
        print("Install with: pip install groq")
        return

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Explain RAG in one sentence."}
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
