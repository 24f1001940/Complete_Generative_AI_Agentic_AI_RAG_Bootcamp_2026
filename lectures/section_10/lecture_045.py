"""
Lecture 45: Getting started with Streamlit & Build your first app
"""
import streamlit as st

def main():
    # Set the page configuration
    st.set_page_config(page_title="My First App", page_icon="🚀")

    # Displaying a title and text
    st.title("My First Streamlit App")
    st.write("Welcome to the course! Streamlit makes it incredibly easy to build interactive web apps for AI and Data Science.")
    
    st.info("Run this app by typing `streamlit run lecture_045.py` in your terminal.")

if __name__ == "__main__":
    main()