"""
Lecture 86: Role & Persona Prompting
"""

def build_prompt(role, task):
    return f"""
You are a {role}.

Task:
{task}
""".strip()


def main():
    print(
        build_prompt(
            "Python instructor",
            "Explain decorators to a beginner.",
        )
    )


if __name__ == "__main__":
    main()
