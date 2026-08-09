"""
Lecture 164: CrewAI Automation: Multi-Agent Orchestration Engine
"""

def main():
    agents = [
        ("Researcher", "Find relevant information"),
        ("Analyst", "Analyze the information"),
        ("Writer", "Prepare the final response"),
    ]

    print("Multi-agent workflow:")

    for name, role in agents:
        print(f"{name}: {role}")

    print("\nWorkflow:")
    print("Researcher -> Analyst -> Writer")


if __name__ == "__main__":
    main()
