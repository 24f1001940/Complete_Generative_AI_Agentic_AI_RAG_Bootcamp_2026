import os
from pathlib import Path

files = {
    'lectures/section_11/lecture_050.py': '''"""
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
    
    print("🚀 NLP Learning Roadmap 🚀\\n" + "="*30)
    for phase, topics in roadmap.items():
        print(f"\\n{phase}:")
        for idx, topic in enumerate(topics, 1):
            print(f"  {idx}. {topic}")

if __name__ == "__main__":
    display_nlp_roadmap()
''',

    'lectures/section_11/lecture_050.md': '''# Lecture 50: Roadmap to learn NLP

## Key Concepts
- **Foundational NLP**: Rule-based systems, linguistics, and basic text normalization.
- **Vectorization**: Converting text into numbers (Embeddings, TF-IDF).
- **Deep Learning**: Sequential modeling using LSTMs and RNNs.
- **Modern NLP**: The shift towards Transformer architectures, Attention mechanisms, and Large Language Models (LLMs).
''',

    'lectures/section_11/lecture_051.py': '''"""
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
    print("Practical NLP Use Cases:\\n")
    for use_case, desc in get_nlp_use_cases().items():
        print(f"- {use_case}: {desc}")
''',

    'lectures/section_11/lecture_051.md': '''# Lecture 51: Practical use cases of NLP

## Key Concepts
- **Automation**: Using NLP to automate customer service, document processing, and data extraction.
- **Analytics**: Deriving actionable insights from unstructured text data via sentiment analysis and topic modeling.
- **Generative AI**: Building systems that can author text, draft emails, and write code based on human prompts.
''',

    'lectures/section_11/lecture_052.py': '''"""
Lecture 52: Tokenization and terminology
Author: MOHD SAQIB
"""
import re

def basic_word_tokenizer(text: str) -> list[str]:
    """A simple regex-based word tokenizer."""
    # Matches sequences of word characters
    return re.findall(r'\\b\\w+\\b', text)

def basic_sentence_tokenizer(text: str) -> list[str]:
    """A simple regex-based sentence tokenizer."""
    # Splits by period, exclamation, or question mark followed by a space
    return re.split(r'(?<=[.!?]) +', text)

if __name__ == "__main__":
    sample_text = "Hello there! Welcome to the NLP foundations course. Are you ready to learn?"
    
    print("Original Text:", sample_text)
    
    sentences = basic_sentence_tokenizer(sample_text)
    print("\\nSentence Tokens:")
    for i, s in enumerate(sentences):
        print(f"  {i+1}: {s}")
        
    words = basic_word_tokenizer(sample_text)
    print("\\nWord Tokens (First 5):")
    print(" ", words[:5])
''',

    'lectures/section_11/lecture_052.md': '''# Lecture 52: Tokenization and terminology

## Key Concepts
- **Corpus**: A large and structured set of texts used for statistical analysis and hypothesis testing.
- **Vocabulary**: The set of all unique tokens present in a corpus.
- **Tokenization**: The process of breaking down raw text into smaller units (tokens), such as words, subwords, or sentences.
''',

    'lectures/section_11/lecture_053.py': '''"""
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
    text = re.sub(r'http\\S+|www\\S+|https\\S+', '', text, flags=re.MULTILINE)
    
    # 4. Remove punctuation and special characters (keep only alphanumeric and spaces)
    text = re.sub(r'[^a-z0-9\\s]', '', text)
    
    # 5. Remove extra whitespace
    text = re.sub(r'\\s+', ' ', text).strip()
    
    return text

if __name__ == "__main__":
    raw_text = "<html><body>WOW!!! Check out this link: https://example.com. It is AWESOME!!!    </body></html>"
    clean_text = preprocess_text(raw_text)
    
    print("Raw Text:  ", raw_text)
    print("Clean Text:", clean_text)
''',

    'lectures/section_11/lecture_053.md': '''# Lecture 53: Text preprocessing

## Key Concepts
- **Normalization**: Converting text to a standard format (e.g., lowercasing) to reduce the vocabulary space.
- **Noise Removal**: Eliminating elements that do not contribute to the meaning of the text (HTML tags, URLs, special characters).
- **Regex**: Using Regular Expressions for powerful pattern matching and string manipulation.
''',

    'lectures/section_11/lecture_054.py': '''"""
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
''',

    'lectures/section_11/lecture_054.md': '''# Lecture 54: Stemming

## Key Concepts
- **Stemming**: A heuristic process that chops off the ends of words in the hope of achieving the goal correctly most of the time.
- **Root Form**: The base part of a word. Note that a stemmed word might not be a valid dictionary word (e.g., "happily" -> "happi").
- **Over-stemming / Under-stemming**: Common errors where too much or too little of the word is removed.
''',

    'lectures/section_11/lecture_055.py': '''"""
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
''',

    'lectures/section_11/lecture_055.md': '''# Lecture 55: Lemmatization

## Key Concepts
- **Lemmatization**: Using vocabulary and morphological analysis to return the base or dictionary form of a word (the lemma).
- **Context Dependent**: True lemmatization requires knowing the Part of Speech (POS). For example, "saw" could be a noun (a tool) or a verb (past tense of see).
- **Stemming vs. Lemmatization**: Lemmatization is more accurate and yields actual words, but is computationally more expensive than stemming.
''',

    'lectures/section_11/lecture_056.py': '''"""
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
''',

    'lectures/section_11/lecture_056.md': '''# Lecture 56: Stopwords

## Key Concepts
- **Stopwords**: The most common words in a language (like "the", "a", "is", "in") that often carry very little useful information for downstream NLP tasks.
- **Information Density**: Removing stopwords increases the density of meaningful terms in a dataset.
- **Exceptions**: Stopword removal is not always beneficial. Tasks like syntax parsing, text generation, and sometimes sentiment analysis require keeping them.
''',

    'lectures/section_11/lecture_057.py': '''"""
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
''',

    'lectures/section_11/lecture_057.md': '''# Lecture 57: POS tagging

## Key Concepts
- **Part-of-Speech (POS)**: Categorizing words based on their grammatical role in a sentence (e.g., Noun, Verb, Adjective, Adverb).
- **Contextual Meaning**: POS tagging helps resolve ambiguity. "Book that flight" (Book=Verb) vs. "Read that book" (Book=Noun).
- **Tag Sets**: Standard sets of abbreviations are used, such as the Penn Treebank tagset (e.g., NN for Noun, VB for Verb).
''',

    'lectures/section_11/lecture_058.py': '''"""
Lecture 58: Named entity recognition
Author: MOHD SAQIB
"""

def dummy_ner_extractor(text: str) -> list[tuple]:
    """A mock NER system to demonstrate identifying entities."""
    # Hardcoded entities for demonstration purposes
    entities = {
        "Jamia Millia Islamia": "ORG",
        "New Delhi": "LOC",
        "India": "LOC",
        "Mohd Saqib": "PERSON",
        "Google": "ORG",
        "2026": "DATE"
    }
    
    found_entities = []
    for entity, label in entities.items():
        if entity in text:
            found_entities.append((entity, label))
            
    return found_entities

if __name__ == "__main__":
    doc = "Mohd Saqib studies at Jamia Millia Islamia in New Delhi, India. He will graduate by 2026."
    extracted = dummy_ner_extractor(doc)
    
    print("Document:", doc)
    print("\\nExtracted Entities:")
    for ent, label in extracted:
        print(f" - [{label}] {ent}")
''',

    'lectures/section_11/lecture_058.md': '''# Lecture 58: Named entity recognition

## Key Concepts
- **Named Entity Recognition (NER)**: An information extraction task that seeks to locate and classify named entities mentioned in unstructured text.
- **Standard Categories**: Person (PER), Organization (ORG), Location (LOC), Date/Time (DATE), and Miscellaneous (MISC).
- **Applications**: Automating resume parsing, classifying news articles, and extracting knowledge graphs.
''',

    'lectures/section_11/lecture_059.py': '''"""
Lecture 59: NLP mini projects
Author: MOHD SAQIB
"""
import re

def nlp_mini_pipeline(text: str) -> dict:
    """A mini end-to-end NLP pipeline encompassing previous lectures."""
    # 1. Preprocessing (Lowercasing & cleaning)
    clean_text = re.sub(r'[^a-zA-Z\\s]', '', text).lower()
    
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
    
    print("\\nPipeline Results:")
    for key, value in results.items():
        print(f" - {key.replace('_', ' ').title()}: {value}")
''',

    'lectures/section_11/lecture_059.md': '''# Lecture 59: NLP Mini Projects

## Key Concepts
- **Pipelines**: Combining text preprocessing, tokenization, filtering, and analysis into a single cohesive function.
- **End-to-End Execution**: Taking raw unstructured data and outputting structured insights (like word frequencies or sentiment scores).
- **Practical Implementation**: Applying foundational NLP techniques to real-world datasets, setting the stage for advanced machine learning models.
'''
}

for filepath, content in files.items():
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding='utf-8')
    print(f'Created: {filepath}')