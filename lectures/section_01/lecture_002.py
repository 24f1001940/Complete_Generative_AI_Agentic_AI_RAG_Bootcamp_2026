"""
Lecture 02: What You Will Build in This Course
Author: MOHD SAQIB
"""

def list_capstones():
    return [
        {
            "Project": "Project 1",
            "Title": "Multi-Document RAG Q&A Engine",
            "Tech": "LangChain, ChromaDB, Hybrid Search, Citations",
        },
        {
            "Project": "Project 2",
            "Title": "Autonomous Web Research & Real-Time News Agent",
            "Tech": "LangGraph, Search Tools, State Synthesis",
        },
        {
            "Project": "Project 3",
            "Title": "Autonomous Code Engineering Agent & Cloud Deployment",
            "Tech": "Multi-Agent Networks, Docker, Streamlit Cloud, AWS",
        },
    ]


if __name__ == "__main__":
    for proj in list_capstones():
        print(f"[{proj['Project']}] {proj['Title']} -> Tech: {proj['Tech']}")