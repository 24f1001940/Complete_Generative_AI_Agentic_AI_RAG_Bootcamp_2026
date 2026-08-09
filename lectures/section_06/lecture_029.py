"""
Lecture 29: Magic methods
Author: MOHD SAQIB
"""

class PromptTemplate:
    def __init__(self, template: str, author: str):
        self.template = template
        self.author = author

    def __str__(self) -> str:
        return f"PromptTemplate('{self.template[:20]}...')"

    def __repr__(self) -> str:
        return f"PromptTemplate(template='{self.template}', author='{self.author}')"

    def __len__(self) -> int:
        return len(self.template)

    def __call__(self, **kwargs) -> str:
        return self.template.format(**kwargs)

if __name__ == "__main__":
    prompt = PromptTemplate("Hello {name}, welcome to {course}!", author="MOHD SAQIB")
    print("String Repr:", str(prompt))
    print("Length:", len(prompt))
    print("Executable Call:", prompt(name="Saqib", course="GenAI Bootcamp"))