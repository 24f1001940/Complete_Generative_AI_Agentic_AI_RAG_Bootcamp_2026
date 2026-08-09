"""
Lecture 59: NLP mini projects
Author: MOHD SAQIB
"""
import re

def nlp_mini_pipeline(text: str) -> dict:
    """A mini end-to-end NLP pipeline encompassing previous lectures."""
    # 1. Preprocessing (Lowercasing & cleaning)
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # 2. Tokenization
    tokens = clean_text.split()
    
    # 3. Stopword Removal (mock list)
    stopwords = {"is", "the", "at", "a", "an", "and", "in"}
    filtered_tokens = [w for w in tokens if w not in stopwords]
    
    # 4. Word Frequency Analysis
    freq_dist = {}
    for word in filtered_tokens:
        freq_dist[word] = freq_dist.get(word, 0) + 1
        
    return {
        "original_length": len(text),
        "clean_tokens_count": len(filtered_tokens),
        "top_keywords": sorted(freq_dist.items(), key=lambda item: item[1], reverse=True)[:3]
    }

if __name__ == "__main__":
    sample_review = (
        "The food at this restaurant is amazing! The service is also amazing, "
        "and the atmosphere in the restaurant is perfect."
    )
    
    print("Executing NLP Mini Pipeline on text...")
    results = nlp_mini_pipeline(sample_review)
    
    print("\nPipeline Results:")
    for key, value in results.items():
        print(f" - {key.replace('_', ' ').title()}: {value}")