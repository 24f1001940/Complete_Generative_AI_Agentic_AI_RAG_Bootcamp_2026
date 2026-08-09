"""
Lecture 54: Stemming
Author: MOHD SAQIB
"""

def simple_suffix_stemmer(word: str) -> str:
    """A very basic heuristic stemmer simulating suffix stripping."""
    suffixes = ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']
    
    # Sort suffixes by length descending to match longest suffix first
    suffixes.sort(key=len, reverse=True)
    
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]
    return word

if __name__ == "__main__":
    # Note: In production, use nltk.stem.PorterStemmer
    words_to_stem = ["running", "flies", "happily", "investment", "dogs", "generous"]
    
    print("Simple Stemming Results:")
    for word in words_to_stem:
        stemmed = simple_suffix_stemmer(word)
        print(f"  {word:12} -> {stemmed}")