"""
Lecture 52: Tokenization and terminology
Author: MOHD SAQIB
"""
import re

def basic_word_tokenizer(text: str) -> list[str]:
    """A simple regex-based word tokenizer."""
    # Matches sequences of word characters
    return re.findall(r'\b\w+\b', text)

def basic_sentence_tokenizer(text: str) -> list[str]:
    """A simple regex-based sentence tokenizer."""
    # Splits by period, exclamation, or question mark followed by a space
    return re.split(r'(?<=[.!?]) +', text)

if __name__ == "__main__":
    sample_text = "Hello there! Welcome to the NLP foundations course. Are you ready to learn?"
    
    print("Original Text:", sample_text)
    
    sentences = basic_sentence_tokenizer(sample_text)
    print("\nSentence Tokens:")
    for i, s in enumerate(sentences):
        print(f"  {i+1}: {s}")
        
    words = basic_word_tokenizer(sample_text)
    print("\nWord Tokens (First 5):")
    print(" ", words[:5])