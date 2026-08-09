"""
Lecture 39: Pydantic Data Validation: Fields, Constraints & Custom Validators
Author: MOHD SAQIB
"""
from pydantic import BaseModel, Field, field_validator, ValidationError

class LLMQueryRequest(BaseModel):
    prompt: str = Field(..., min_length=5, max_length=1000, description="Input user prompt")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="Sampling temperature")
    max_tokens: int = Field(default=512, gt=0, le=4096, description="Maximum token generation limit")
    model_name: str = Field(default="gpt-4o", description="Target language model identifier")

    @field_validator("model_name")
    @classmethod
    def validate_allowed_models(cls, value: str) -> str:
        allowed = {"gpt-4o", "gpt-4o-mini", "claude-3-5-sonnet", "llama-3.3-70b"}
        if value.lower() not in allowed:
            raise ValueError(f"Model '{value}' is not allowed. Supported: {allowed}")
        return value.lower()

if __name__ == "__main__":
    # Valid Request
    valid_req = LLMQueryRequest(
        prompt="Explain vector database indexing",
        temperature=0.3,
        model_name="GPT-4O"
    )
    print("Valid Pydantic Request Model:")
    print(valid_req)

    # Invalid Request Triggering Validation Errors
    try:
        LLMQueryRequest(
            prompt="Hi",  # Too short (<5 chars)
            temperature=3.5,  # Exceeds max 2.0
            model_name="unsupported-model"
        )
    except ValidationError as err:
        print("
Caught Expected Validation Error:")
        print(err)