"""
Lecture 87: Zero-shot, One-shot & Few-shot Prompting
"""

def main():
    prompts = {
        "Zero-shot": "Classify: This product is excellent.",
        "One-shot": "Example: Excellent product -> Positive. Classify: Useful tool ->",
        "Few-shot": (
            "Excellent product -> Positive\n"
            "Terrible service -> Negative\n"
            "Fast delivery -> Positive\n"
            "Classify: Helpful support ->"
        ),
    }

    for name, prompt in prompts.items():
        print(f"\n{name}:")
        print(prompt)


if __name__ == "__main__":
    main()
