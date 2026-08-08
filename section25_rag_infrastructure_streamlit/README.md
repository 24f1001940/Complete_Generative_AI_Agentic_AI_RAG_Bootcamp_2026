# Section 25: RAG Infrastructure

This is a lecture-wise Streamlit app for:
- Lecture 133: RAG Core Principles: Architecture, Business Value & Fine-Tuning Tradeoffs
- Lecture 134: Data Ingestion & Preprocessing: Unstructured (PDF, Word) & Structured (CSV, SQL)
- Lecture 135: Vector Stores: ChromaDB, FAISS, Pinecone & AstraDB
- Lecture 136: End-to-End LCEL Retrieval Pipelines & Vector Management

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

## What this app is for
- One file for all 4 lectures
- Switch lectures from the sidebar
- Show visuals and code blocks while recording
- Avoid rewriting code between lectures

## Optional environment variables
Not required for this demo app, but useful later if you connect real services:
- GROQ_API_KEY
- OPENAI_API_KEY
- LANGSMITH_API_KEY
- LANGCHAIN_TRACING_V2=true

## Recording workflow
1. Open the app once.
2. Select Lecture 133 from the sidebar.
3. Record.
4. Switch to Lecture 134, 135, and 136.
