"""
Lecture 64: CBOW + Skip-gram
"""

def main():
    try:
        from gensim.models import Word2Vec
    except ImportError:
        print("Missing dependency: gensim")
        print("Install with: pip install gensim")
        return

    sentences = [
        ["the", "cat", "sits", "on", "mat"],
        ["the", "dog", "sits", "on", "floor"],
        ["the", "cat", "likes", "food"],
        ["the", "dog", "likes", "food"],
    ]

    cbow = Word2Vec(
        sentences, vector_size=50, window=2, min_count=1,
        sg=0, workers=1, seed=42
    )

    skipgram = Word2Vec(
        sentences, vector_size=50, window=2, min_count=1,
        sg=1, workers=1, seed=42
    )

    print("CBOW vector for 'cat':")
    print(cbow.wv["cat"])

    print("\nSkip-gram vector for 'cat':")
    print(skipgram.wv["cat"])


if __name__ == "__main__":
    main()
