"""
Lecture 11: Jupyter Notebooks vs Scripts
Author: MOHD SAQIB
"""

COMPARISON = [
    {"Feature": "Workflow", "Notebook (.ipynb)": "Exploratory & Interactive", "Script (.py)": "Production & Automated"},
    {"Feature": "State Management", "Notebook (.ipynb)": "In-memory cell state", "Script (.py)": "Sequential top-to-bottom"},
    {"Feature": "Deployment", "Notebook (.ipynb)": "Difficult to test/deploy", "Script (.py)": "Standard production entrypoint"},
]

if __name__ == "__main__":
    for row in COMPARISON:
        print(f"[{row['Feature']}] -> Notebooks: {row['Notebook (.ipynb)']} | Scripts: {row['Script (.py)']}")