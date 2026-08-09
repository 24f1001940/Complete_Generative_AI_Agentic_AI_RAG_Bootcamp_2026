"""
Lecture 161: Project 3 & Capstone: Autonomous Code Engineering Agent & Cloud Deployment
"""

def plan_code_task(task):
    return [
        "Understand requirements",
        "Inspect project structure",
        "Plan changes",
        "Implement changes",
        "Run tests",
        "Review the diff",
        "Prepare deployment",
    ]


def main():
    task = "Add authentication to an application."

    print("Engineering plan for:", task)

    for step in plan_code_task(task):
        print(" -", step)


if __name__ == "__main__":
    main()
