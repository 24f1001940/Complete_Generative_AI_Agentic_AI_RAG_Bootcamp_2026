# Lecture 39: Pydantic Data Validation: Fields, Constraints & Custom Validators

## Key Concepts
- **`BaseModel`**: The foundational class for strongly typed data models in Python.
- **Field Constraints**: Enforcing rules with `Field(...)` using bounds like `min_length`, `max_length`, `ge`, `le`, `gt`.
- **Custom Validators**: Using `@field_validator` to write custom domain logic and data transformations.