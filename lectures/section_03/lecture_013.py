"""
Lecture 13: Python Core Concepts (Part 1)
Author: MOHD SAQIB
"""

def demo_core_concepts():
    age = 22
    name = "Saqib"
    is_active = True
    score = 98.5

    greeting = f"Developer: {name} | Score: {score}"
    
    if score >= 90:
        status = "Excellent"
    elif score >= 70:
        status = "Good"
    else:
        status = "Needs Improvement"

    return {
        "greeting": greeting,
        "status": status,
        "types": [type(age).__name__, type(name).__name__, type(is_active).__name__]
    }

if __name__ == "__main__":
    print(demo_core_concepts())