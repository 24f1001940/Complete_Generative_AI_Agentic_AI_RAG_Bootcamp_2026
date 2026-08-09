"""
Lecture 14: Python Core Concepts (Part 2) - Data Structures
Author: MOHD SAQIB
"""

def demo_data_structures():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens_squared = [x**2 for x in numbers if x % 2 == 0]

    skills = ["Python", "LangChain", "RAG", "Streamlit"]
    skill_map = {skill: len(skill) for skill in skills}

    unique_tags = {"ai", "ml", "rag", "ai"}
    config_tuple = ("localhost", 8080)

    return {
        "evens_squared": evens_squared,
        "skill_map": skill_map,
        "unique_tags": list(unique_tags),
        "config": config_tuple
    }

if __name__ == "__main__":
    res = demo_data_structures()
    print("List Comprehension:", res["evens_squared"])
    print("Skill Map:", res["skill_map"])