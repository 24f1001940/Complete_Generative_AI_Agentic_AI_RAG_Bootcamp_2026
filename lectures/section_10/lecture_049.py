"""
Lecture 49: Deploying simple demo apps
"""
import streamlit as st

def main():
    st.set_page_config(page_title="Deployment Guide", layout="centered")
    
    st.title("Deploying Your Streamlit App 🚀")
    
    st.markdown("""
    ## 3 Simple Steps to Deploy on Streamlit Community Cloud:
    
    **1. Prepare your files**
    Ensure all your code is in a main file (e.g., `app.py`). You must also include a `requirements.txt` file detailing your dependencies.
    """)
    
    st.code("streamlit==1.32.0\npandas==2.2.1\nnumpy==1.26.4", language="text")
    
    st.markdown("""
    **2. Push to GitHub**
    Create a repository on GitHub and commit your `app.py` and `requirements.txt` files to the main branch.
    
    **3. Deploy**
    - Go to [share.streamlit.io](https://share.streamlit.io)
    - Click **New app**
    - Select your GitHub repository, branch, and main file path.
    - Click **Deploy!**
    """)
    
    st.success("Your app is now live and accessible via a public URL!")

if __name__ == "__main__":
    main()