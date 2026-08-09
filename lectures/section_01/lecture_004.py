"""
Lecture 04: Tools, Software, and Accounts Needed
Author: MOHD SAQIB
"""

REQUIRED_TOOLS = {
    "Local Editors": ["VS Code / Cursor", "Jupyter Lab"],
    "Package Managers": ["Python 3.11+", "Conda", "UV (Fastest Python Package Manager)"],
    "Cloud Accounts": ["GitHub", "Hugging Face Hub", "Streamlit Community Cloud"],
    "API Keys (Optional/Recommended)": ["Groq", "OpenAI / Anthropic", "Tavily Search"],
}

if __name__ == "__main__":
    for category, tools in REQUIRED_TOOLS.items():
        print(f"{category}: {', '.join(tools)}")