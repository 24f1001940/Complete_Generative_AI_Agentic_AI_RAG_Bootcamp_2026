"""
Lecture 57: POS tagging
Author: MOHD SAQIB
"""

def dummy_pos_tagger(sentence: str) -> list[tuple]:
    """A mock POS tagger to demonstrate the concept without heavy libraries."""
    # Simplified mapping for demonstration
    tag_map = {
        "apple": "NOUN", "john": "PROPN", "runs": "VERB", 
        "quickly": "ADV", "the": "DET", "red": "ADJ", "in": "ADP"
    }
    
    words = sentence.lower().replace('.', '').split()
    tagged = []
    
    for word in words:
        tag = tag_map.get(word, "NOUN") # Default to NOUN if unknown
        tagged.append((word, tag))
        
    return tagged

if __name__ == "__main__":
    text = "John runs quickly in the red Apple"
    tags = dummy_pos_tagger(text)
    
    print(f"{'WORD':<10} | {'POS TAG'}")
    print("-" * 22)
    for word, tag in tags:
        print(f"{word:<10} | {tag}")