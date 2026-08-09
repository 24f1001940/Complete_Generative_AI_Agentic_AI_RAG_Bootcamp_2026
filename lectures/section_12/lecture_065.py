"""
Lecture 65: Average Word2Vec
"""

import numpy as np


def average_embedding(words, model):
    vectors = [model.wv[word] for word in words if word in model.wv]

    if not vectors:
        return np.zeros(model.vector_size)

    return np.mean(vectors, axis=0)


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
    ]

    model = Word2Vec(
        sentences, vector_size=50, window=2,
        min_count=1, workers=1, seed=42
    )

    sentence = ["machine", "learning"]
    embedding = average_embedding(sentence, model)

    print("Average Word2Vec embedding:")
    print(embedding)


if __name__ == "__main__":
    main()
