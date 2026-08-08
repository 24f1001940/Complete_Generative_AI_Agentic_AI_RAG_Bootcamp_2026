import re
from collections import Counter
from typing import List

import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Section 25: RAG Infrastructure", page_icon="📚", layout="wide")

st.title("Section 25: RAG Infrastructure")
st.caption("Lecture-wise demo app for Lectures 133–136. Use the sidebar to switch lectures without editing code.")

LECTURES = {
    "Lecture 133": "RAG Core Principles: Architecture, Business Value & Fine-Tuning Tradeoffs",
    "Lecture 134": "Data Ingestion & Preprocessing: Unstructured (PDF, Word) & Structured (CSV, SQL)",
    "Lecture 135": "Vector Stores: ChromaDB, FAISS, Pinecone & AstraDB",
    "Lecture 136": "End-to-End LCEL Retrieval Pipelines & Vector Management",
}

lecture = st.sidebar.radio("Choose a lecture", list(LECTURES.keys()), index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### Install")
st.sidebar.code("""pip install -r requirements.txt
streamlit run app.py""", language="bash")
st.sidebar.markdown("One file contains all 4 lectures, so you can record lecture by lecture without changing code.")


def lecture_header(num: int, title: str, subtitle: str) -> None:
    st.subheader(f"Lecture {num} – {title}")
    st.write(subtitle)


def show_code(title: str, code: str, language: str = "python") -> None:
    with st.expander(f"Show code: {title}", expanded=False):
        st.code(code.strip(), language=language)


def split_sentences(text: str) -> List[str]:
    text = text.strip().replace("\n", " ")
    if not text:
        return []
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if p.strip()]


def chunk_text(text: str, chunk_size: int = 220) -> List[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def simple_embedding(text: str) -> Counter:
    words = re.findall(r"[a-zA-Z0-9]+", text.lower())
    return Counter(words)


def similarity(a: str, b: str) -> float:
    ca = simple_embedding(a)
    cb = simple_embedding(b)
    if not ca or not cb:
        return 0.0
    common = set(ca) & set(cb)
    dot = sum(ca[w] * cb[w] for w in common)
    na = sum(v * v for v in ca.values()) ** 0.5
    nb = sum(v * v for v in cb.values()) ** 0.5
    return round(dot / (na * nb), 3) if na and nb else 0.0


def summarize_stuff(text: str) -> str:
    s = split_sentences(text)
    return " ".join(s[:3]) if s else "No content provided."


def summarize_map_reduce(text: str) -> str:
    chunks = chunk_text(text, 160)
    if not chunks:
        return "No content provided."
    partials = []
    for ch in chunks:
        sents = split_sentences(ch)
        partials.append(sents[0] if sents else ch[:80])
    return " ".join(partials[:5]) + ("..." if len(partials) > 5 else "")


def summarize_refine(text: str) -> str:
    sents = split_sentences(text)
    if not sents:
        return "No content provided."
    summary = sents[0]
    for s in sents[1:]:
        if len(summary) < 220:
            summary += " " + s
        else:
            summary = summary[:220] + " ... " + s[:80]
    return summary


DEMO_DOCS = [
    "RAG stands for Retrieval-Augmented Generation and improves answer quality by adding external context.",
    "Ingestion turns PDFs, Word documents, CSV files, and SQL rows into clean text for downstream processing.",
    "Vector stores like ChromaDB and FAISS index embeddings so retrievers can find relevant chunks quickly.",
    "LCEL lets developers compose retrieval pipelines from retrievers, prompt templates, and model calls.",
    "Fine-tuning changes model behavior, while RAG changes the knowledge available at inference time.",
]


def render_lecture_133():
    lecture_header(133, "RAG Core Principles: Architecture, Business Value & Fine-Tuning Tradeoffs", "Understand the RAG pipeline and when it is better than fine-tuning for knowledge-heavy applications.")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### RAG architecture")
        st.code("User Question → Retriever → Relevant Context → LLM → Final Answer", language="text")
        st.markdown("### Simple comparison")
        data = [
            {"Approach": "RAG", "Best for": "Fresh/private knowledge", "Changes data?": "No", "Business value": "High"},
            {"Approach": "Fine-tuning", "Best for": "Behavior/style specialization", "Changes data?": "Yes", "Business value": "High"},
        ]
        st.dataframe(data, use_container_width=True, hide_index=True)
    with col2:
        question = st.text_input("Ask a RAG-style question", value="What is RAG?", key="l133_q")
        if st.button("Show RAG response", key="l133_btn"):
            context = [
                "RAG means Retrieval-Augmented Generation.",
                "It uses external documents to improve answer quality.",
                "It is useful when knowledge changes often.",
            ]
            prompt = f"""
You are a helpful AI assistant.

Use the retrieved context to answer the question.

Context:
{chr(10).join(context)}

Question:
{question}

Answer:
"""
            st.success("Response generated")
            st.write("RAG helps the model answer using external context instead of relying only on training memory.")
            st.markdown("### Built prompt")
            st.code(prompt.strip(), language="text")
    st.markdown("---")
    fig = go.Figure(go.Funnel(y=["User Question", "Retriever", "Relevant Context", "LLM", "Answer"], x=[100, 88, 76, 68, 62]))
    fig.update_layout(height=420, title="RAG pipeline")
    st.plotly_chart(fig, use_container_width=True)
    show_code("Lecture 133 concept code", '''
question = "What is RAG?"
retrieved_context = [
    "RAG means Retrieval-Augmented Generation.",
    "It uses external documents to improve answer quality."
]
context_text = "\n".join(retrieved_context)

prompt = f"""
Use the context below to answer the question.

Context:
{context_text}

Question:
{question}
"""
''')


def render_lecture_134():
    lecture_header(134, "Data Ingestion & Preprocessing: Unstructured (PDF, Word) & Structured (CSV, SQL)", "Convert different data sources into clean text so they can be used in a RAG pipeline.")
    left, right = st.columns([1.05, 0.95])
    sample_text = st.text_area(
        "Paste sample content",
        value=(
            "Artificial Intelligence is transforming industries. "
            "It automates repetitive tasks. "
            "It improves productivity. "
            "Businesses use AI in healthcare, finance, education, and robotics."
        ),
        height=150,
        key="l134_text",
    )
    with left:
        source = st.selectbox("Choose source type", ["PDF", "Word", "CSV", "SQL"], key="l134_source")
        if source in ["PDF", "Word"]:
            st.code(f"{source} Loader → Extract text → Clean whitespace → Normalize content", language="text")
        elif source == "CSV":
            st.code("CSV → DataFrame → Row text conversion → Clean text", language="text")
        else:
            st.code("SQL → Query rows → Convert rows to text → Clean text", language="text")
        if st.button("Preprocess sample", key="l134_btn"):
            cleaned = " ".join(sample_text.replace("\n", " ").split())
            chunks = chunk_text(cleaned, 120)
            st.success("Preprocessing complete")
            st.write("### Cleaned text")
            st.write(cleaned)
            st.write("### Chunks")
            for i, ch in enumerate(chunks, start=1):
                st.write(f"{i}. {ch}")
    with right:
        st.markdown("### Source-to-text pipeline")
        fig = go.Figure(go.Funnel(y=["Raw source", "Load", "Clean", "Chunk", "Retrieval ready"], x=[100, 90, 82, 74, 66]))
        fig.update_layout(height=380, title="Ingestion and preprocessing flow")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("### Example row conversion")
        st.code(
            '''
# CSV row example
Name: Rahul | Department: Engineering | Salary: 120000

# SQL row example
Name: Priya | Department: HR | Salary: 95000
''',
            language="text",
        )
    show_code("Lecture 134 preprocessing code", '''
def clean_text(text):
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text.strip()

cleaned_docs = [clean_text(doc) for doc in documents]
''')


def render_lecture_135():
    lecture_header(135, "Vector Stores: ChromaDB, FAISS, Pinecone & AstraDB", "Compare common vector store choices and see how retrieval uses embeddings to find relevant chunks.")
    docs = st.multiselect("Choose demo documents", DEMO_DOCS, default=DEMO_DOCS[:3], key="l135_docs")
    query = st.text_input("Enter a retrieval query", value="What improves answer quality in RAG?", key="l135_query")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### Vector store comparison")
        data = [
            {"Vector store": "ChromaDB", "Best for": "Local prototyping", "Strength": "Easy setup", "Scale": "Small to medium"},
            {"Vector store": "FAISS", "Best for": "Fast local similarity search", "Strength": "Very fast", "Scale": "Small to medium"},
            {"Vector store": "Pinecone", "Best for": "Managed cloud retrieval", "Strength": "Production-ready", "Scale": "Large"},
            {"Vector store": "AstraDB", "Best for": "Cloud-native vector storage", "Strength": "Managed and scalable", "Scale": "Large"},
        ]
        st.dataframe(data, use_container_width=True, hide_index=True)
    with col2:
        st.markdown("### Similarity retrieval demo")
        if st.button("Run semantic search", key="l135_btn"):
            scored = [(doc, similarity(query, doc)) for doc in docs]
            scored.sort(key=lambda x: x[1], reverse=True)
            st.write("### Ranked chunks")
            for i, (doc, score) in enumerate(scored, start=1):
                st.write(f"{i}. **{score}** — {doc}")
    st.markdown("---")
    fig = go.Figure(go.Funnel(y=["Documents", "Embeddings", "Vector Store", "Retriever", "Relevant Chunks"], x=[100, 88, 80, 72, 66]))
    fig.update_layout(height=420, title="Vector store retrieval pipeline")
    st.plotly_chart(fig, use_container_width=True)
    show_code("Lecture 135 vector store code", '''
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_texts(documents, embedding_model)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
''')


def render_lecture_136():
    lecture_header(136, "End-to-End LCEL Retrieval Pipelines & Vector Management", "Connect ingestion, embeddings, vector storage, retrieval, prompt construction, and generation into one pipeline.")
    col1, col2 = st.columns([1.05, 0.95])
    with col1:
        st.markdown("### End-to-end LCEL flow")
        st.code("Documents → Chunking → Embeddings → Vector Store → Retriever → Prompt Template → LLM → Answer", language="text")
        question = st.text_input("Question", value="What is RAG?", key="l136_q")
        top_k = st.slider("Top-k retrieval", 1, 5, 2, key="l136_k")
        if st.button("Run retrieval pipeline", key="l136_btn"):
            scored = [(doc, similarity(question, doc)) for doc in DEMO_DOCS]
            scored.sort(key=lambda x: x[1], reverse=True)
            selected = scored[:top_k]
            context = "\n".join([doc for doc, _ in selected])
            prompt = f"""
You are a helpful AI assistant.

Use the following context to answer the user's question.

Context:
{context}

Question:
{question}

Answer:
"""
            st.success("Pipeline completed")
            st.write("### Retrieved context")
            for i, (doc, score) in enumerate(selected, start=1):
                st.write(f"{i}. **{score}** — {doc}")
            st.write("### Final prompt")
            st.code(prompt.strip(), language="text")
            st.write("### Final answer")
            st.write("A RAG pipeline retrieves relevant external context and gives it to the model so the answer is grounded in those documents.")
    with col2:
        st.markdown("### Vector management checklist")
        checklist = [
            "Add new documents when knowledge changes",
            "Remove outdated documents",
            "Monitor retrieval quality",
            "Tune chunk sizes and top-k values",
            "Rebuild indexes when needed",
        ]
        for item in checklist:
            st.checkbox(item, value=True, disabled=True)
        st.markdown("### LCEL pipeline diagram")
        fig = go.Figure(go.Funnel(y=["Retriever", "Context formatter", "Prompt template", "LLM", "Answer"], x=[100, 90, 82, 74, 68]))
        fig.update_layout(height=380, title="LCEL retrieval workflow")
        st.plotly_chart(fig, use_container_width=True)
    show_code("Lecture 136 pipeline code", '''
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke(question)

context = "\n".join([doc.page_content for doc in results])

prompt = prompt_template.format(
    context=context,
    question=question
)

response = llm.invoke(prompt)
''')


if lecture == "Lecture 133":
    render_lecture_133()
elif lecture == "Lecture 134":
    render_lecture_134()
elif lecture == "Lecture 135":
    render_lecture_135()
elif lecture == "Lecture 136":
    render_lecture_136()