"""
Lecture 63: Word embeddings + Word2Vec Intuition
"""

def main():
    try:
        from gensim.models import Word2Vec
    except ImportError:
        print("Missing dependency: gensim")
        print("Install with: pip install gensim")
        return

    sentences = [
        ["machine", "learning", "is", "powerful"],
        ["deep", "learning", "is", "useful"],
        ["machine", "learning", "is", "useful"],
        ["deep", "learning", "is", "powerful"],
    ]

    model = Word2Vec(
        sentences,
        vector_size=50,
        window=2,
        min_count=1,
        workers=1,
        seed=42,
    )

    print("Vector for 'learning':")
    print(model.wv["learning"])

    print("\nSimilar words:")
    print(model.wv.most_similar("learning"))


if __name__ == "__main__":
    main()
