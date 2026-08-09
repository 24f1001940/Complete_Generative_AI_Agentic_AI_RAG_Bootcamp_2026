"""
Lecture 22: Custom exception handling
Author: MOHD SAQIB
"""

class LLMAPIError(Exception):
    """Base exception for LLM API failures."""
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.status_code = status_code

class RateLimitExceededError(LLMAPIError):
    """Raised when API rate limits are breached."""
    def __init__(self, message="Rate limit exceeded. Please retry later."):
        super().__init__(message, status_code=429)

def invoke_llm_service(tokens_requested: int):
    if tokens_requested > 4000:
        raise RateLimitExceededError("Requested tokens exceed maximum limit per call.")
    return {"status": "success", "tokens": tokens_requested}

if __name__ == "__main__":
    try:
        result = invoke_llm_service(5000)
    except RateLimitExceededError as e:
        print(f"Caught Error [{e.status_code}]: {e}")
    except LLMAPIError as e:
        print(f"General API Error: {e}")
    else:
        print("Execution Succeeded:", result)
    finally:
        print("LLM Request lifecycle execution complete.")