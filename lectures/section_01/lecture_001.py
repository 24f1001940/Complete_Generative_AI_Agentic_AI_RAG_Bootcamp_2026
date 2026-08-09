"""
Lecture 01: Welcome to the Course
Complete Generative AI, Agentic AI & RAG Bootcamp 2026
Author: MOHD SAQIB
"""

import sys
import streamlit as st


def main():
    st.title("🤖 Welcome to the Complete Generative AI Bootcamp!")
    st.write(
        """
    Welcome to the ultimate learning resource hub for modern GenAI engineering.
    In this bootcamp, you will master everything from foundational Python and NLP 
    to enterprise Retrieval-Augmented Generation (RAG) and Agentic Workflows.
    """
    )

    st.subheader("System Readiness Check")
    st.json(
        {
            "Python Version": sys.version.split()[0],
            "Execution Status": "Environment active and ready",
            "Course Status": "Bootcamp In Progress",
        }
    )


if __name__ == "__main__":
    main()