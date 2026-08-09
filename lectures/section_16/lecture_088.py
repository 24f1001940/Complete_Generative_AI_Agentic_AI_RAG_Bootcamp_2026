"""
Lecture 88: Chain-of-Thought Style, Reasoning & Structured Prompting
"""

def main():
    prompt = """
Solve the problem carefully.

Return:
1. Approach
2. Important calculation or evidence
3. Final answer

Keep the final answer concise.
""".strip()

    print(prompt)


if __name__ == "__main__":
    main()
