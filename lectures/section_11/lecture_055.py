"""
Lecture 55: Lemmatization
Author: MOHD SAQIB
"""

# Simulating a lemmatization dictionary (In practice, use nltk.stem.WordNetLemmatizer or spaCy)
LEMMATIZATION_DICT = {
    "am": "be", "are": "be", "is": "be", "was": "be", "were": "be",
    "mice": "mouse", "geese": "goose",
    "better": "good", "best": "good",
    "running": "run", "ran": "run"
}

def dummy_lemmatize(word: str) -> str:
    """Simulates dictionary/morphological based lemmatization."""
    word = word.lower()
    return LEMMATIZATION_DICT.get(word, word)

if __name__ == "__main__":
    tokens = ["The", "mice", "are", "running", "better", "today"]
    
    lemmatized_tokens = [dummy_lemmatize(token) for token in tokens]
    
    print("Original Tokens:  ", tokens)
    print("Lemmatized Tokens:", lemmatized_tokens)