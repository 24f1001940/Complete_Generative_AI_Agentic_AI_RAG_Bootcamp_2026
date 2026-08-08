import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = ROOT / "section_data" / "sections.json"
LECTURES_DIR = ROOT / "lectures"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for section in data["sections"]:

    section_number = section["section_number"]

    section_dir = (
        LECTURES_DIR /
        f"section_{section_number:02d}"
    )

    section_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    for lecture in section["lectures"]:

        lecture_number = lecture["lecture_number"]
        lecture_title = lecture["lecture_title"]

        python_file = (
            section_dir /
            f"lecture_{lecture_number:03d}.py"
        )

        markdown_file = (
            section_dir /
            f"lecture_{lecture_number:03d}.md"
        )

        if not python_file.exists():

            python_file.write_text(
                f'''"""
Lecture {lecture_number}
{lecture_title}

Complete Generative AI, Agentic AI & RAG Bootcamp
Author: MOHD SAQIB
"""

# Add the lecture code here.

''',
                encoding="utf-8"
            )

        if not markdown_file.exists():

            markdown_file.write_text(
                f"""# Lecture {lecture_number}: {lecture_title}

## Learning Objective

Add the learning objective for this lecture.

## Concepts Covered

- Add concept 1
- Add concept 2
- Add concept 3

## Code

The corresponding Python implementation is available in:

`lecture_{lecture_number:03d}.py`

## Practice

Add exercises, assignments, or experiments here.

## Resources

Add useful links and references here.
""",
                encoding="utf-8"
            )

print("Lecture structure created successfully.")