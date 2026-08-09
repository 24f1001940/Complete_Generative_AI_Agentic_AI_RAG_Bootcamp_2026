"""
Lecture 36: Decorators
Author: MOHD SAQIB
"""
import functools
import time

def log_execution_time(func):
    """Decorator to measure and log function execution latency."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"[LOG] {func.__name__} executed in {elapsed:.6f} seconds.")
        return result
    return wrapper

@log_execution_time
def simulate_llm_inference(prompt: str) -> str:
    time.sleep(0.1)  # Simulate API latency
    return f"Response for prompt: '{prompt}'"

if __name__ == "__main__":
    output = simulate_llm_inference("Explain decorators in Python")
    print("Result:", output)