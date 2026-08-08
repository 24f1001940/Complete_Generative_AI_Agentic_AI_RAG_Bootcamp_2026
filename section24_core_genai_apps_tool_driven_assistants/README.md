# Section 24: Core GenAI Applications & Tool-Driven Assistants

This is a single lecture-wise Streamlit app for:
- Lecture 129: Conversational Q&A Systems
- Lecture 130: Text Summarization Engines
- Lecture 131: Tool Integration, Function Calling & SQL Database Assistants
- Lecture 132: Specialized Productivity Assistants

## Install steps

### 1) Create a virtual environment
```bash
python -m venv venv
```

### 2) Activate it
Windows:
```bash
venv\Scripts\activate
```

### 3) Install packages
```bash
pip install -r requirements.txt
```

### 4) Run the app
```bash
streamlit run app.py
```

## What this app does
- Uses one Streamlit file for all 4 lectures
- Lets you switch lectures from the sidebar
- Shows visuals, demos, and code snippets
- Avoids editing the code between lectures

## Optional environment variables
Not required for this demo app, but if you later connect real providers:
- GROQ_API_KEY
- OPENAI_API_KEY
- LANGSMITH_API_KEY
- LANGCHAIN_TRACING_V2=true

## Recording workflow
1. Open the app once.
2. Select Lecture 129 from the sidebar.
3. Record.
4. Switch to Lecture 130 and record.
5. Repeat for Lecture 131 and Lecture 132.
