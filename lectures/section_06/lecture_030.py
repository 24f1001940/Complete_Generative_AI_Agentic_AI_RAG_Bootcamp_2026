"""
Lecture 30: Operator overloading
Author: MOHD SAQIB
"""

class TokenBudget:
    def __init__(self, token_count: int):
        self.token_count = token_count

    def __add__(self, other):
        if isinstance(other, TokenBudget):
            return TokenBudget(self.token_count + other.token_count)
        return TokenBudget(self.token_count + int(other))

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenBudget):
            return self.token_count == other.token_count
        return False

    def __repr__(self) -> str:
        return f"TokenBudget(tokens={self.token_count})"

if __name__ == "__main__":
    b1 = TokenBudget(1500)
    b2 = TokenBudget(2500)
    total = b1 + b2
    print("Total Combined Budget:", total)
    print("Budgets Equal?:", b1 == b2)