"""
Lecture 156: Deep Agents Architecture: Concepts & Sub-Agent Networks
"""

def main():
    tasks = {
        "planner": "Break the objective into subtasks.",
        "researcher": "Collect relevant information.",
        "coder": "Implement the required solution.",
        "reviewer": "Check the result.",
    }

    for agent, task in tasks.items():
        print(f"{agent}: {task}")


if __name__ == "__main__":
    main()
