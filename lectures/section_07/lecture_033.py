"""
Lecture 33: Generators
Author: MOHD SAQIB
"""

def token_stream_generator(prompt: str):
    """Simulates dynamic streaming output of tokens from an LLM."""
    tokens = prompt.split()
    for token in tokens:
        yield token

if __name__ == "__main__":
    prompt_text = "Generative AI applications require scalable streaming architectures."
    stream = token_stream_generator(prompt_text)

    print("Streaming Tokens:")
    for token in stream:
        print(f"Token: {token}")

    # Generator Expression
    squares_gen = (x**2 for x in range(5))
    print("Generator Expression Output:", list(squares_gen))