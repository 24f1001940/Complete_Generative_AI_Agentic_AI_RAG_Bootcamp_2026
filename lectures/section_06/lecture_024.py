"""
Lecture 24: Constructors and attributes
Author: MOHD SAQIB
"""

class LLMConfig:
    """Manages model configuration attributes."""
    provider_default = "OpenAI"  # Class attribute

    def __init__(self, model_name: str, temperature: float = 0.7, max_tokens: int = 1024):
        self.model_name = model_name         # Instance attribute
        self.temperature = temperature       # Instance attribute
        self.max_tokens = max_tokens         # Instance attribute

    def update_temperature(self, new_temp: float) -> None:
        self.temperature = max(0.0, min(1.0, new_temp))

if __name__ == "__main__":
    config = LLMConfig("gpt-4o", temperature=0.8)
    print(f"Model: {config.model_name} | Initial Temp: {config.temperature}")
    config.update_temperature(0.2)
    print(f"Updated Temp: {config.temperature}")