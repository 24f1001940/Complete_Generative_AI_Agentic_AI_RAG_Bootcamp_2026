"""
Lecture 53: Text preprocessing
Author: MOHD SAQIB
"""
import re

def preprocess_text(text: str) -> str:
    """Applies standard text normalization techniques."""
    # 1. Lowercasing
    text = text.lower()
    
    # 2. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # 3. Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 4. Remove punctuation and special characters (keep only alphanumeric and spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # 5. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

if __name__ == "__main__":
    raw_text = "<html><body>WOW!!! Check out this link: https://example.com. It is AWESOME!!!    </body></html>"
    clean_text = preprocess_text(raw_text)
    
    print("Raw Text:  ", raw_text)
    print("Clean Text:", clean_text)