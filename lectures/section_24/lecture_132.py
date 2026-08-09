"""
Lecture 132: Specialized Productivity Assistants: Math Solvers, Code Helpers & Study Tools
"""

def calculate(expression):
    allowed = set("0123456789+-*/(). ")

    if not set(expression) <= allowed:
        raise ValueError("Expression contains unsupported characters.")

    return eval(expression, {"__builtins__": {}}, {})


def main():
    expression = "12 * (8 + 2) / 5"

    print("Expression:", expression)
    print("Result:", calculate(expression))


if __name__ == "__main__":
    main()
