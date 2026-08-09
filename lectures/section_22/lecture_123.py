"""
Lecture 123: Structured Outputs with Pydantic, TypedDict & Dataclasses
"""

from dataclasses import dataclass
from typing import TypedDict

try:
    from pydantic import BaseModel, Field
except ImportError:
    BaseModel = None


class UserDict(TypedDict):
    name: str
    age: int


@dataclass
class UserData:
    name: str
    age: int


if BaseModel is not None:
    class UserModel(BaseModel):
        name: str
        age: int = Field(ge=0)


def main():
    typed: UserDict = {"name": "Alex", "age": 21}
    data = UserData(name="Alex", age=21)

    print("TypedDict:", typed)
    print("Dataclass:", data)

    if BaseModel is not None:
        model = UserModel(name="Alex", age=21)
        print("Pydantic:", model.model_dump())
    else:
        print("Install pydantic to run the Pydantic example.")


if __name__ == "__main__":
    main()
