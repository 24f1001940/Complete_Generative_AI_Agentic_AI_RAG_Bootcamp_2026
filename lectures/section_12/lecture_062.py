"""
Lecture 62: TF-IDF
"""

def main():
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
    except ImportError:
        print("Missing dependency: scikit-learn")
        print("Install with: pip install scikit-learn")
        return

    documents = [
        "machine learning is powerful",
        "machine learning is useful",
        "deep learning is powerful",
    ]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)

    print("Features:")
    print(vectorizer.get_feature_names_out())
    print("\nTF-IDF matrix:")
    print(matrix.toarray())


if __name__ == "__main__":
    main()
