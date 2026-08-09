"""
Lecture 50: Roadmap to learn NLP
Author: MOHD SAQIB
"""

def display_nlp_roadmap():
    """Prints a structured roadmap for learning Natural Language Processing."""
    roadmap = {
        "Phase 1: NLP Foundations": ["Text Preprocessing", "Tokenization", "Stemming & Lemmatization", "POS Tagging", "NER"],
        "Phase 2: Text Representation": ["Bag of Words (BoW)", "TF-IDF", "Word2Vec", "GloVe"],
        "Phase 3: Deep Learning for NLP": ["RNNs", "LSTMs", "GRUs", "Seq2Seq Models"],
        "Phase 4: Advanced NLP (Transformers)": ["Attention Mechanism", "Transformers", "BERT", "GPT", "LLMs"]
    }
    
    print("🚀 NLP Learning Roadmap 🚀\n" + "="*30)
    for phase, topics in roadmap.items():
        print(f"\n{phase}:")
        for idx, topic in enumerate(topics, 1):
            print(f"  {idx}. {topic}")

if __name__ == "__main__":
    display_nlp_roadmap()