"""
Lecture 46: Widgets and interaction
"""
import streamlit as st

def main():
    st.header("Widgets and Interaction")
    st.write("Streamlit widgets allow users to interact with your Python code directly.")

    # Text Input
    user_name = st.text_input("Enter your name:", placeholder="e.g., John Doe")

    # Slider
    age = st.slider("Select your age:", min_value=0, max_value=120, value=25)

    # Selectbox
    role = st.selectbox("Choose your role:", ["Data Scientist", "AI Engineer", "Developer", "Other"])

    # Button
    if st.button("Submit Profile"):
        if user_name:
            st.success(f"Profile saved! Hello {user_name}. You are a {age}-year-old {role}.")
        else:
            st.error("Please enter a name before submitting.")

if __name__ == "__main__":
    main()