"""
Lecture 51: Practical use cases of NLP
Author: MOHD SAQIB
"""

def get_nlp_use_cases():
    """Returns a dictionary mapping NLP use cases to their descriptions."""
    return {
        "Sentiment Analysis": "Determining the emotional tone behind a body of text (e.g., product reviews).",
        "Machine Translation": "Automatically translating text from one language to another (e.g., Google Translate).",
        "Named Entity Recognition (NER)": "Identifying and classifying key entities in text into predefined categories.",
        "Chatbots & Virtual Assistants": "Conversational agents that interact with users using natural language (e.g., Siri, Alexa).",
        "Text Summarization": "Condensing large blocks of text into shorter, meaningful summaries."
    }

if __name__ == "__main__":
    print("Practical NLP Use Cases:\n")
    for use_case, desc in get_nlp_use_cases().items():
        print(f"- {use_case}: {desc}")