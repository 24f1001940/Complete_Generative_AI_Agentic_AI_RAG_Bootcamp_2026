"""
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
    print("\nExtracted Entities:")
    for ent, label in extracted:
        print(f" - [{label}] {ent}")