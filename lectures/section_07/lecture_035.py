"""
Lecture 35: Closures
Author: MOHD SAQIB
"""

def create_rate_limiter(max_calls: int):
    """Closure that maintains and enforces invocation counts across function calls."""
    calls_made = 0

    def rate_limited_function(action_name: str) -> str:
        nonlocal calls_made
        if calls_made >= max_calls:
            return f"Rate limit exceeded! Allowed: {max_calls}, Attempted: {calls_made + 1}"
        calls_made += 1
        return f"Executing {action_name} [Call {calls_made}/{max_calls}]"

    return rate_limited_function

if __name__ == "__main__":
    limiter = create_rate_limiter(max_calls=2)
    print(limiter("API Call 1"))
    print(limiter("API Call 2"))
    print(limiter("API Call 3"))