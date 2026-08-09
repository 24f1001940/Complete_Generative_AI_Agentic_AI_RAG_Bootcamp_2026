##### `lectures/section_02/lecture_010.py`

"""
Lecture 10: Create Virtual Environments with UV
Author: MOHD SAQIB
"""

UV_COMMANDS = {
    "Install UV": "pip install uv",
    "Create Virtual Env": "uv venv .venv --python 3.11",
    "Activate (Unix/Mac)": "source .venv/bin/activate",
    "Activate (Windows)": ".venv\\Scripts\\activate",
    "Install Packages": "uv pip install streamlit langchain pydantic",
}

if __name__ == "__main__":
    print("High-Speed Package Management with UV:")
    for step, cmd in UV_COMMANDS.items():
        print(f"[{step}] -> {cmd}")