# Section 23: Production GenAI

This is a lecture-wise Streamlit app for Section 23.

## Lectures included
- Lecture 125: Conversation Memory Design, Stateful Assistants & Middleware Controls
- Lecture 126: LangSmith Observability: Tracing Workflows, Debugging & App Evaluation
- Lecture 127: GenAI App Deployment: Streamlit Cloud, Hugging Face Spaces & LangServe APIs
- Lecture 128: Enterprise Infrastructure: AWS Lifecycle, Scaling Architecture & Reliability

## Install steps

### 1) Create a virtual environment
python -m venv venv

### 2) Activate it
Windows:
venv\Scripts\activate

### 3) Install packages
pip install -r requirements.txt

### 4) Run the app
streamlit run app.py

## Optional environment variables
If you later connect LangSmith or hosted model APIs, add them to .env or your shell:
- GROQ_API_KEY
- LANGSMITH_API_KEY
- LANGCHAIN_TRACING_V2=true

## Recording workflow
Open the app once, then switch lectures from the sidebar:
- Lecture 125
- Lecture 126
- Lecture 127
- Lecture 128
