"""
Lecture 160: Project 2: Autonomous Web Research & Real-Time News Agent
"""

from datetime import datetime


def create_research_plan(topic):
    return [
        f"Search current information about {topic}",
        "Collect multiple relevant sources",
        "Extract important claims",
        "Compare the evidence",
        "Produce a concise report",
    ]


def main():
    topic = "generative AI"

    print("Research started:", datetime.now().isoformat())

    for step in create_research_plan(topic):
        print(" -", step)

    print("\nThis teaching demo creates the agent plan without making live web requests.")


if __name__ == "__main__":
    main()
