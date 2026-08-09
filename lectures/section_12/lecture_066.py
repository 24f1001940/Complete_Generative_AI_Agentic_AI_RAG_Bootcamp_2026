"""
Lecture 66: Practical NLP feature engineering
"""

import re


def clean_text(text):
    text = text.lower()
    return re.sub(r"[^a-zA-Z\s]", "", text)


def main():
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
    except ImportError:
        print("Missing dependency: scikit-learn")
        print("Install with: pip install scikit-learn")
        return

    documents = [
        "I love Natural Language Processing!",
        "NLP is useful for AI applications.",
        "Machine learning and NLP work together.",
    ]

    cleaned = [clean_text(doc) for doc in documents]

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=20,
    )

    features = vectorizer.fit_transform(cleaned)

    print("Features:")
    print(vectorizer.get_feature_names_out())
    print("\nFeature matrix:")
    print(features.toarray())


if __name__ == "__main__":
    main()
