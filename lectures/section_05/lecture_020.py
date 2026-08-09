"""
Lecture 20: Reading and writing text files
Author: MOHD SAQIB
"""
from pathlib import Path

def text_file_workflow(filepath: str):
    path = Path(filepath)
    
    # Writing content using standard context manager
    lines_to_write = [
        "Generative AI & Agentic AI Bootcamp\n",
        "Lesson: Reading and Writing Text Files\n",
        "Status: Active\n"
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        f.writelines(lines_to_write)
        
    # Appending additional content
    with open(path, mode="a", encoding="utf-8") as f:
        f.write("Appended: Production Ready Workflow\n")

    # Reading content line-by-line
    with open(path, mode="r", encoding="utf-8") as f:
        content = f.readlines()

    return [line.strip() for line in content]

if __name__ == "__main__":
    lines = text_file_workflow("demo_lecture_20.txt")
    print("Read File Lines:", lines)