import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

st.set_page_config(
    page_title="Section 20 GenAI Studio",
    page_icon="🤖",
    layout="wide",
)

st.title("Section 20: First GenAI Applications")
st.caption(
    "Use the sidebar to switch between lectures 107 to 114. This single file contains all demos so you do not need to keep changing code."
)

LECTURE_OPTIONS = {
    "Lecture 107": "Simple GenAI app using Ollama",
    "Lecture 108": "LLM prompt and output chain",
    "Lecture 109": "LCEL basics",
    "Lecture 110": "LangServe API deployment",
    "Lecture 111": "Chatbot with message history",
    "Lecture 112": "Prompt templates with memory",
    "Lecture 113": "Conversational Q&A chatbot",
    "Lecture 114": "Working with retriever + vector store",
}

lecture_choice = st.sidebar.radio(
    "Choose a lecture",
    list(LECTURE_OPTIONS.keys()),
    index=0,
)

model_name = st.sidebar.selectbox(
    "Ollama model",
    ["llama3.2:3b", "llama3.1:8b", "gemma2:2b", "gemma4:12b"],
    index=0,
)

st.sidebar.info(
    "Tip: for smooth recording, start with a small model such as llama3.2:3b or gemma2:2b. Large models can make Streamlit reruns slow on laptops."
)

SAMPLE_DOCS = [
    "LangChain is a framework for building AI applications with LLMs.",
    "Retrievers find the most relevant document chunks for a question.",
    "Vector stores keep embeddings and allow semantic search.",
    "Ollama helps run models locally on your own machine.",
    "LCEL connects prompts, models, and parsers in one pipeline.",
]


def lecture_header(number: int, title: str, subtitle: str) -> None:
    st.subheader(f"Lecture {number} – {title}")
    st.write(subtitle)


@st.cache_resource(show_spinner=False)
def get_llm(selected_model: str) -> OllamaLLM:
    return OllamaLLM(model=selected_model, num_ctx=2048)


@st.cache_resource(show_spinner=False)
def get_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


@st.cache_resource(show_spinner=False)
def get_vector_store() -> FAISS:
    return FAISS.from_texts(SAMPLE_DOCS, get_embeddings())



def safe_invoke_llm(llm: OllamaLLM, prompt: str) -> str:
    try:
        return llm.invoke(prompt)
    except Exception as e:
        return f"Generation failed: {e}"



def show_code(title: str, code: str, language: str = "python") -> None:
    with st.expander(f"Show code: {title}", expanded=False):
        st.code(code, language=language)



def build_history_text(messages, limit: int = 6) -> str:
    recent = messages[-limit:]
    return "\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in recent)



def init_messages(key: str, greeting: str):
    if key not in st.session_state:
        st.session_state[key] = [{"role": "assistant", "content": greeting}]



def display_chat(messages):
    for msg in messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])


# -----------------------------
# Lecture 107
# -----------------------------
def render_lecture_107():
    lecture_header(
        107,
        "Simple GenAI app using Ollama",
        "A tiny local GenAI app: user prompt → Ollama → response.",
    )

    st.markdown("### Visual flow")
    st.code("User → Streamlit App → Ollama → Local LLM → Response", language="text")

    prompt = st.text_area(
        "Enter your prompt",
        value="Explain transformers in simple words.",
        height=120,
        key="l107_prompt",
    )

    if st.button("Generate Response", key="l107_btn"):
        if prompt.strip():
            llm = get_llm(model_name)
            with st.spinner("Generating response..."):
                response = safe_invoke_llm(llm, prompt)
            st.subheader("Response")
            st.write(response)
        else:
            st.warning("Please enter a prompt first.")

    show_code(
        "Lecture 107 app",
        """
import streamlit as st
from langchain_ollama import OllamaLLM

st.title("Simple GenAI App Using Ollama")
prompt = st.text_area("Enter your prompt here:")

if st.button("Generate Response"):
    llm = OllamaLLM(model="llama3.2:3b")
    response = llm.invoke(prompt)
    st.write(response)
""".strip(),
    )


# -----------------------------
# Lecture 108
# -----------------------------
def render_lecture_108():
    lecture_header(
        108,
        "LLM Prompt and Output Chain",
        "Build a structured prompt before calling the model so the output becomes cleaner and more consistent.",
    )

    st.markdown("### Visual flow")
    st.code("User Input → Prompt Builder → LLM → Generated Output", language="text")

    user_input = st.text_input(
        "Question",
        value="Explain retrieval augmented generation.",
        key="l108_question",
    )
    tone = st.selectbox(
        "Tone",
        ["simple", "professional", "friendly", "exam-style"],
        index=0,
        key="l108_tone",
    )
    max_points = st.slider(
        "How many bullet points?",
        min_value=2,
        max_value=6,
        value=4,
        key="l108_points",
    )

    prompt = f"""
You are a helpful AI tutor.

Answer the user's question in a {tone} tone.
Use exactly {max_points} bullet points.
End with one short summary line.

Question:
{user_input}

Answer:
"""

    st.markdown("### Built prompt")
    st.code(prompt.strip(), language="text")

    if st.button("Generate structured response", key="l108_btn"):
        llm = get_llm(model_name)
        with st.spinner("Generating response..."):
            response = safe_invoke_llm(llm, prompt)
        st.subheader("Response")
        st.write(response)

    show_code( 
        "Lecture 108 prompt chain",
        '''
def build_prompt(question, tone="simple", max_points=4):
    return f"""
You are a helpful AI tutor.

Answer the user's question in a {tone} tone.
Use exactly {max_points} bullet points.
End with one short summary line.

Question:
{question}

Answer:
"""
'''.strip(),
    )


# -----------------------------
# Lecture 109
# -----------------------------
def render_lecture_109():
    lecture_header(
        109,
        "LCEL basics",
        "Use LangChain Expression Language to connect prompt → model → parser as one clean pipeline.",
    )

    st.markdown("### Visual flow")
    st.code("Prompt Template | LLM | Output Parser", language="text")

    topic = st.text_input(
        "Topic",
        value="LangChain Expression Language",
        key="l109_topic",
    )

    prompt = PromptTemplate.from_template(
        "You are a helpful AI tutor. Explain {topic} in simple words."
    )
    llm = get_llm(model_name)
    parser = StrOutputParser()
    chain = prompt | llm | parser

    st.markdown("### LCEL chain")
    st.code(
        """
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

prompt = PromptTemplate.from_template(
    "You are a helpful AI tutor. Explain {topic} in simple words."
)
llm = OllamaLLM(model="llama3.2:3b")
parser = StrOutputParser()

chain = prompt | llm | parser
""".strip(),
        language="python",
    )

    if st.button("Run LCEL chain", key="l109_btn"):
        with st.spinner("Running chain..."):
            try:
                response = chain.invoke({"topic": topic})
                st.subheader("Response")
                st.write(response)
            except Exception as e:
                st.error(f"Generation failed: {e}")

    show_code(
        "Lecture 109 one-line invocation",
        """
response = chain.invoke({"topic": "LangChain Expression Language"})
print(response)
""".strip(),
    )


# -----------------------------
# Lecture 110
# -----------------------------
def render_lecture_110():
    lecture_header(
        110,
        "LangServe API deployment",
        "Turn a LangChain chain into an HTTP API so other apps can call it.",
    )

    st.markdown("### Concept")
    st.code(
        "LCEL Chain → LangServe → FastAPI endpoint → HTTP request/response",
        language="text",
    )

    topic = st.text_input(
        "API demo topic",
        value="transformers",
        key="l110_topic",
    )

    request_payload = {"input": {"topic": topic}}
    st.markdown("### Example request payload")
    st.json(request_payload)

    llm = get_llm(model_name)
    api_prompt = f"You are a helpful AI tutor. Explain {topic} in simple words."
    if st.button("Simulate API response", key="l110_btn"):
        with st.spinner("Generating simulated API output..."):
            answer = safe_invoke_llm(llm, api_prompt)
        st.markdown("### Example API response")
        st.json({"output": answer})

    st.markdown("### LangServe deployment code")
    st.code(
        """
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="Simple GenAI API", version="1.0")
add_routes(app, chain, path="/explain")
""".strip(),
        language="python",
    )

    st.markdown("This lecture is about exposing the chain as an API, not about changing the model itself.")


# -----------------------------
# Lecture 111
# -----------------------------
def render_lecture_111():
    lecture_header(
        111,
        "Chatbot with message history",
        "A chatbot should remember the current conversation during the same session.",
    )

    st.markdown("### Visual flow")
    st.code(
        "User Message → Session State → LLM Response → Save Response → Display Chat",
        language="text",
    )

    state_key = "messages_l111"
    init_messages(
        state_key,
        "Hi! I am your local AI assistant. How can I help you today?"
    )
    messages = st.session_state[state_key]

    if st.button("Clear chat", key="l111_clear"):
        st.session_state[state_key] = [
            {"role": "assistant", "content": "Hi! I am your local AI assistant. How can I help you today?"}
        ]
        st.rerun()

    display_chat(messages)

    user_input = st.chat_input("Type your message here...", key="l111_chat")

    if user_input:
        messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        history_text = build_history_text(messages, limit=8)
        prompt = f"""
You are a helpful AI assistant.

Use the conversation history when it helps.
Conversation history:
{history_text}

Assistant:
"""
        llm = get_llm(model_name)
        with st.spinner("Thinking..."):
            response = safe_invoke_llm(llm, prompt)

        messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

    show_code(
        "Lecture 111 chat history app",
        """
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I am your local AI assistant."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here...")
""".strip(),
    )


# -----------------------------
# Lecture 112
# -----------------------------
def render_lecture_112():
    lecture_header(
        112,
        "Prompt templates with memory",
        "Use a reusable prompt template so the chatbot can use history in a structured way.",
    )

    st.markdown("### Visual flow")
    st.code("Session History → Prompt Template → Local LLM → Response", language="text")

    state_key = "messages_l112"
    init_messages(
        state_key,
        "Hello! I am your AI tutor. Ask me a question and I will use the conversation history."
    )
    messages = st.session_state[state_key]

    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("Ask your question...", key="l112_chat")

    def build_prompt(history_messages, latest_user_input):
        recent = history_messages[-6:]
        history_text = "\n".join(
            f"{m['role'].capitalize()}: {m['content']}" for m in recent
        )
        return f"""
You are a helpful AI tutor.

Use the conversation history naturally.
If the history is relevant, refer to it.
If it is not relevant, answer only the current question.

Write in simple and clear language.

Conversation history:
{history_text}

Latest user message:
{latest_user_input}

Assistant:
"""

    if user_input:
        messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        prompt = build_prompt(messages, user_input)

        with st.expander("Show built prompt", expanded=False):
            st.code(prompt.strip(), language="text")

        llm = get_llm(model_name)
        with st.spinner("Generating response..."):
            response = safe_invoke_llm(llm, prompt)

        messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

    st.markdown("This lecture improves memory by combining a template, recent history, and the latest question.")

    show_code(
        "Lecture 112 memory-aware prompt function",
        '''
def build_prompt(history_messages, latest_user_input):
    recent = history_messages[-6:]
    history_text = "\\n".join(
        f"{m['role'].capitalize()}: {m['content']}" for m in recent
    )
    return f"""
You are a helpful AI tutor.

Use the conversation history naturally.
If the history is relevant, refer to it.
If it is not relevant, answer only the current question.

Write in simple and clear language.

Conversation history:
{history_text}

Latest user message:
{latest_user_input}

Assistant:
"""
'''.strip(),
)


# -----------------------------
# Lecture 113
# -----------------------------
def render_lecture_113():
    lecture_header(
        113,
        "Conversational Q&A chatbot",
        "A mini-project that combines memory, structured prompts, and a clean chat interface.",
    )

    st.markdown("### Visual flow")
    st.code(
        "User → Chat History → Prompt Template → Ollama LLM → Response → Update History",
        language="text",
    )

    state_key = "messages_l113"
    init_messages(
        state_key,
        "Hello! I am your conversational Q&A chatbot. Ask me anything."
    )
    messages = st.session_state[state_key]

    if st.button("Reset conversation", key="l113_reset"):
        st.session_state[state_key] = [
            {"role": "assistant", "content": "Hello! I am your conversational Q&A chatbot. Ask me anything."}
        ]
        st.rerun()

    max_turns = st.slider("History window", 2, 10, 8, key="l113_window")

    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("Ask a follow-up question...", key="l113_chat")

    def build_qa_prompt(history_messages, latest_user_input):
        recent = history_messages[-max_turns:]
        history_text = "\n".join(
            f"{m['role'].capitalize()}: {m['content']}" for m in recent
        )
        return f"""
You are a helpful AI tutor and question-answering assistant.

Use the conversation history only when it helps the answer.
Answer clearly and directly.
If the user asks a follow-up question, connect it to the earlier discussion.
Use simple language and give one short example if useful.

Conversation history:
{history_text}

Latest user message:
{latest_user_input}

Assistant:
"""

    if user_input:
        messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        prompt = build_qa_prompt(messages, user_input)

        with st.expander("Show Q&A prompt", expanded=False):
            st.code(prompt.strip(), language="text")

        llm = get_llm(model_name)
        with st.spinner("Generating Q&A answer..."):
            response = safe_invoke_llm(llm, prompt)

        messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)

    show_code(
        "Lecture 113 conversational Q&A chatbot",
        '''
# This lecture combines:
# 1) message history
# 2) structured prompt
# 3) local Ollama model
# 4) chat UI
'''.strip(),
    )


# -----------------------------
# Lecture 114
# -----------------------------
def render_lecture_114():
    lecture_header(
        114,
        "Working with retriever + vector store",
        "Use a retriever and a vector store so the chatbot can answer from external documents.",
    )

    st.markdown("### Visual flow")
    st.code(
        "Question → Retriever → Vector Store → Relevant Chunks → LLM → Answer",
        language="text",
    )

    st.markdown("### Sample documents")
    for i, doc in enumerate(SAMPLE_DOCS, start=1):
        st.write(f"{i}. {doc}")

    top_k = st.slider("Top-k retrieved chunks", 1, 4, 2, key="l114_k")
    query = st.text_input(
        "Ask a question about the sample documents",
        value="What is LangChain?",
        key="l114_query",
    )

    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": top_k})

    if st.button("Retrieve and answer", key="l114_btn"):
        with st.spinner("Retrieving relevant chunks..."):
            results = retriever.invoke(query)

        st.subheader("Retrieved chunks")
        for i, doc in enumerate(results, start=1):
            st.success(f"Chunk {i}: {doc.page_content}")

        context = "\n".join(doc.page_content for doc in results)
        prompt = f"""
You are a helpful AI tutor.

Use the context below to answer the question.
If the answer is not in the context, say that you do not know.

Context:
{context}

Question:
{query}

Answer:
"""

        st.markdown("### Prompt sent to the LLM")
        st.code(prompt.strip(), language="text")

        llm = get_llm(model_name)
        with st.spinner("Generating final answer..."):
            answer = safe_invoke_llm(llm, prompt)

        st.subheader("Final answer")
        st.write(answer)

    st.info(
        "This is the first retrieval-based step in the course: the chatbot can now use external documents."
    )

    show_code(
        "Lecture 114 retriever + vector store core",
        '''
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_texts(documents, embedding_model)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke(query)
'''.strip(),
    )


st.sidebar.markdown("---")
st.sidebar.markdown("### What to install")
st.sidebar.code(
    "pip install streamlit langchain langchain-core langchain-community langchain-ollama langchain-huggingface faiss-cpu sentence-transformers",
    language="bash",
)
st.sidebar.markdown("Install Ollama separately, then pull a model such as `llama3.2:3b`.")
st.sidebar.markdown("---")
st.sidebar.markdown("### Recording tip")
st.sidebar.write(
    "Use this single app for all Section 20 lectures. Switch lectures from the sidebar instead of editing the code again and again."
)

if lecture_choice == "Lecture 107":
    render_lecture_107()
elif lecture_choice == "Lecture 108":
    render_lecture_108()
elif lecture_choice == "Lecture 109":
    render_lecture_109()
elif lecture_choice == "Lecture 110":
    render_lecture_110()
elif lecture_choice == "Lecture 111":
    render_lecture_111()
elif lecture_choice == "Lecture 112":
    render_lecture_112()
elif lecture_choice == "Lecture 113":
    render_lecture_113()
elif lecture_choice == "Lecture 114":
    render_lecture_114()
