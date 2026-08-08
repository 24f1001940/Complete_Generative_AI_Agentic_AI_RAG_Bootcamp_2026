# Section 26: Advanced RAG Strategies & Evaluation

This is a lecture-wise Streamlit app for:
- Lecture 137: Advanced Retrieval: Semantic Chunking, Hybrid Search & RRF
- Lecture 138: Query Transformations: Expansion, Decomposition & HyDE
- Lecture 139: Multimodal RAG, Contextual Memory & Next-Gen Retrieval Patterns
- Lecture 140: Safeguards & Evaluation: Guardrails & LLM-as-a-Judge

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
- One file for all 4 lectures
- Switch lectures from the sidebar
- Shows visuals, examples, and code blocks for recording
- Avoids editing files between lectures

## Optional environment variables
Not required for this demo app, but useful later if you connect real services:
- GROQ_API_KEY
- OPENAI_API_KEY
- LANGSMITH_API_KEY
- LANGCHAIN_TRACING_V2=true

## Recording workflow
1. Open the app once.
2. Select Lecture 137.
3. Record.
4. Switch to Lectures 138, 139, and 140.
