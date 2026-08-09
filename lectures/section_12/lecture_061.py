"""
Lecture 61: Bag of Words + N-grams
"""

def main():
    try:
        from sklearn.feature_extraction.text import CountVectorizer
    except ImportError:
        print("Missing dependency: scikit-learn")
        print("Install with: pip install scikit-learn")
        return

    documents = [
        "I love artificial intelligence",
        "I love machine learning",
        "Artificial intelligence is powerful",
    ]

    vectorizer = CountVectorizer(ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(documents)

    print("Vocabulary:")
    print(vectorizer.get_feature_names_out())
    print("\nBag of Words + N-gram matrix:")
    print(matrix.toarray())


if __name__ == "__main__":
    main()
