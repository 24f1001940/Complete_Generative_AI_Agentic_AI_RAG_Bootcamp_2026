"""
Lecture 12: Installing Libraries with pip and UV
Author: MOHD SAQIB
"""

REQUIREMENTS_CONTENT = """
streamlit>=1.35.0
pydantic>=2.7.0
python-dotenv>=1.0.0
numpy>=1.26.0
pandas>=2.2.0
"""

def generate_installation_guide():
    return f"""
# To install via pip:
pip install -r requirements.txt

# To install via UV (Recommended - Ultra Fast):
uv pip install -r requirements.txt
"""

if __name__ == "__main__":
    print("Sample requirements.txt:")
    print(REQUIREMENTS_CONTENT)
    print(generate_installation_guide())