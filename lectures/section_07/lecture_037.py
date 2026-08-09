"""
Lecture 37: Practical utility patterns
Author: MOHD SAQIB
"""
import functools

def memory_cache(func):
    """Utility decorator for caching LLM responses by prompt arguments."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print(f"[CACHE HIT] Returning cached output for key: {key}")
            return cache[key]
        print(f"[CACHE MISS] Executing calculation for key: {key}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

@memory_cache
def expensive_embedding_lookup(text: str) -> list[float]:
    # Mocking expensive embedding generation
    return [round(len(text) * 0.1, 2), 0.42, 0.99]

if __name__ == "__main__":
    print(expensive_embedding_lookup("LangChain RAG Architecture"))
    # Second call uses cache
    print(expensive_embedding_lookup("LangChain RAG Architecture"))