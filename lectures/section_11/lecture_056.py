"""
Lecture 56: Stopwords
Author: MOHD SAQIB
"""

# A minimal list of English stopwords
STOPWORDS = {"i", "me", "my", "myself", "we", "our", "ours", "you", "your", 
             "he", "him", "his", "she", "her", "it", "its", "they", "them", 
             "what", "which", "who", "whom", "this", "that", "these", "those", 
             "am", "is", "are", "was", "were", "be", "been", "have", "has", "had", 
             "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
             "of", "at", "by", "for", "with", "about", "against", "into", "through", 
             "to", "from", "up", "down", "in", "out", "on", "off", "over", "under"}

def remove_stopwords(text: str) -> list[str]:
    """Tokenizes text and removes standard stopwords."""
    words = text.lower().split()
    filtered_words = [word for word in words if word.strip('.,!?') not in STOPWORDS]
    return filtered_words

if __name__ == "__main__":
    sentence = "This is a simple sentence to demonstrate how we remove stopwords from the text."
    filtered = remove_stopwords(sentence)
    
    print("Original:", sentence)
    print("Filtered:", " ".join(filtered))