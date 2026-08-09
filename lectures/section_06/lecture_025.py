"""
Lecture 25: Inheritance
Author: MOHD SAQIB
"""

class BaseLLM:
    """Base class for language models."""
    
    def __init__(self, model_name: str, context_window: int):
        self.model_name = model_name
        self.context_window = context_window

    def get_info((self) -> str:
        return f"Model: {self.model_name} (Window: {self.context_window} tokens)"

class OpenAILLM(BaseLLM):
    """Derived class for OpenAI provider."""
    
    def __init__(self, model_name: str, api_key: str):
        super().__init__(model_name=model_name, context_window=128000)
        self.api_key = api_key

    def generate_response(self, prompt: str) -> str:
        return f"OpenAI [{self.model_name}] responding to: '{prompt}'"

if __name__ == "__main__":
    model = OpenAILLM("gpt-4o", "sk-proj-sample")
    print(model.get_info())
    print(model.generate_response("Explain quantum computing"))