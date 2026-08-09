"""
Lecture 08: Install Anaconda and Conda Basics
Author: MOHD SAQIB
"""

CONDA_COMMANDS = {
    "Check Conda Version": "conda --version",
    "List Environments": "conda env list",
    "Create Environment": "conda create -n genai_env python=3.11 -y",
    "Activate Environment": "conda activate genai_env",
    "Deactivate Environment": "conda deactivate",
}

if __name__ == "__main__":
    print("Essential Conda Cheat Sheet:")
    for task, cmd in CONDA_COMMANDS.items():
        print(f"• {task:<22}: {cmd}")