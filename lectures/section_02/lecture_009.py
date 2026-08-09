"""
Lecture 09: Create Virtual Environments with Conda
Author: MOHD SAQIB
"""

def generate_conda_setup_script(env_name="genai_bootcamp"):
    script = f"""
    # 1. Create environment with Python 3.11
    conda create -n {env_name} python=3.11 -y

    # 2. Activate environment
    conda activate {env_name}

    # 3. Verify path
    which python
    """
    return script

if __name__ == "__main__":
    print(generate_conda_setup_script())