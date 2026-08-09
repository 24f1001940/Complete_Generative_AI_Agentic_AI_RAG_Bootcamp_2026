"""
Lecture 06: Course Resources and Project Files
Author: MOHD SAQIB
"""

from pathlib import Path

def verify_repo_structure(base_dir: Path):
    expected_folders = [
        "section_data",
        "lectures",
        "resources/ebooks",
        "resources/section_notes",
        "resources/assignments",
        "resources/quizzes",
    ]
    status = {}
    for folder in expected_folders:
        folder_path = base_dir / folder
        status[folder] = folder_path.exists()
    return status

if __name__ == "__main__":
    root_dir = Path(__file__).resolve().parent.parent.parent
    results = verify_repo_structure(root_dir)
    print("Repository Directory Status:", results)