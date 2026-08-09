"""
Lecture 15: Function Basics
Author: MOHD SAQIB
"""

def calculate_rag_cost(prompt_tokens: int, completion_tokens: int, rate_per_k: float = 0.002) -> float:
    """Calculates total LLM API cost based on token counts."""
    total_tokens = prompt_tokens + completion_tokens
    cost = (total_tokens / 1000) * rate_per_k
    return round(cost, 6)

if __name__ == "__main__":
    cost = calculate_rag_cost(1500, 500)
    print(f"Total Request Cost: ${cost}")