"""
Lecture 140: Safeguards & Evaluation: Guardrails & LLM-as-a-Judge
"""

def basic_guardrail(text):
    blocked_terms = {"password", "secret-key", "private-key"}
    words = set(text.lower().split())

    return not bool(words.intersection(blocked_terms))


def judge(reference, answer):
    reference_words = set(reference.lower().split())
    answer_words = set(answer.lower().split())

    overlap = len(reference_words & answer_words)
    score = overlap / max(len(reference_words), 1)

    return score


def main():
    answer = "RAG retrieves relevant context before generation."
    reference = "RAG retrieves relevant context before generation."

    print("Guardrail passed:", basic_guardrail(answer))
    print("Simple overlap score:", judge(reference, answer))


if __name__ == "__main__":
    main()
