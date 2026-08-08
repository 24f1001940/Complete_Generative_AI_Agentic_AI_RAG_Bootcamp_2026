import os
import time
import streamlit as st

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None

try:
    from groq import Groq
except Exception:
    Groq = None

try:
    from langchain_ollama import OllamaLLM
except Exception:
    OllamaLLM = None

try:
    from openai import OpenAI
except Exception:
    OpenAI = None

st.set_page_config(
    page_title="Section 21 Open-Source LLM Workflows",
    page_icon="⚡",
    layout="wide",
)

if load_dotenv is not None:
    load_dotenv()

st.title("Section 21: Open-Source LLM Workflows")
st.caption(
    "Switch lectures 115 to 120 from the sidebar. One file, lecture-wise demos, no repeated editing."
)

LECTURE_MAP = {
    "Lecture 115": "Groq Cloud and LPUs",
    "Lecture 116": "Open-source models with Groq",
    "Lecture 117": "Using local and hosted models",
    "Lecture 118": "API-based model integration",
    "Lecture 119": "Speed and latency considerations",
    "Lecture 120": "Model routing strategies",
}

lecture_choice = st.sidebar.radio("Choose a lecture", list(LECTURE_MAP.keys()), index=0)

st.sidebar.header("General Settings")
groq_model = st.sidebar.selectbox(
    "Groq / hosted model",
    [
        "llama-3.3-70b-versatile",
        "openai/gpt-oss-20b",
        "openai/gpt-oss-120b",
        "qwen/qwen3.6-27b",
    ],
    index=0,
)
local_model = st.sidebar.selectbox(
    "Local Ollama model",
    ["llama3.2:3b", "llama3.1:8b", "gemma2:2b"],
    index=0,
)
use_streaming_demo = st.sidebar.checkbox("Show quick speed demo", value=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### Install package list")
st.sidebar.code(
    "pip install streamlit groq python-dotenv openai\npip install langchain-ollama",
    language="bash",
)
st.sidebar.markdown("Install Ollama separately if you want local-model sections to actually run.")
st.sidebar.markdown("---")
st.sidebar.info("For smooth recording, keep the local model small.")

SAMPLE_DOCS = [
    "LangChain is a framework for building AI applications with LLMs.",
    "Retrievers find the most relevant document chunks for a question.",
    "Vector stores keep embeddings and allow semantic search.",
    "Ollama helps run models locally on your own machine.",
    "LCEL connects prompts, models, and parsers in one pipeline.",
]


def lecture_header(num: int, title: str, subtitle: str) -> None:
    st.subheader(f"Lecture {num} – {title}")
    st.write(subtitle)


def show_code(title: str, code: str, language: str = "python") -> None:
    with st.expander(f"Show code: {title}", expanded=False):
        st.code(code.strip(), language=language)


def get_groq_client():
    if Groq is None:
        return None
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return None
    return Groq(api_key=key)


def simple_speed_demo(label: str, delay: float, text: str):
    start = time.perf_counter()
    time.sleep(delay)
    elapsed = time.perf_counter() - start
    st.success(f"{label}: {elapsed:.2f} sec")
    st.write(text)


def render_lecture_115():
    lecture_header(115, "Groq Cloud and LPUs", "Groq is a fast hosted inference platform for low-latency GenAI apps.")
    st.code("User → Groq Cloud → Hosted Model → Fast Response", language="text")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**What to tell students**")
        st.write("Groq is a cloud inference platform focused on speed and responsiveness.")
    with c2:
        st.markdown("**Why it matters**")
        st.write("Fast responses improve user experience in chatbots, Q&A systems, and agent workflows.")
    if use_streaming_demo and st.button("Run quick simulated latency demo", key="l115_speed"):
        left, right = st.columns(2)
        with left:
            simple_speed_demo("Fast response path", 0.4, "Feels smooth for the user.")
        with right:
            simple_speed_demo("Slow response path", 1.8, "Feels more delayed and less interactive.")
    show_code(
        "Lecture 115 concept code",
        """
# Concept only: user sends prompt to a fast hosted model provider
question = "Explain transformers in simple words."
# Groq cloud handles the request and returns a quick response
""",
    )


def render_lecture_116():
    lecture_header(116, "Open-source models with Groq", "Use Groq to run open-weight models through a fast hosted API.")
    st.code("Task → Choose Open Model → Groq API → Response", language="text")
    model_choice = st.selectbox(
        "Pick an open model for the demo",
        ["llama-3.3-70b-versatile", "openai/gpt-oss-20b", "openai/gpt-oss-120b", "qwen/qwen3.6-27b"],
        index=0,
        key="l116_model",
    )
    question = st.text_area("Prompt", value="Explain semantic search in simple words.", height=110, key="l116_prompt")
    if st.button("Run Groq model", key="l116_run"):
        client = get_groq_client()
        if client is None:
            st.warning("Groq API key or groq package is not available in this environment.")
        else:
            with st.spinner("Calling Groq..."):
                try:
                    result = client.chat.completions.create(
                        model=model_choice,
                        messages=[
                            {"role": "system", "content": "You are a helpful AI tutor."},
                            {"role": "user", "content": question},
                        ],
                    )
                    st.subheader("Response")
                    st.write(result.choices[0].message.content)
                except Exception as e:
                    st.error(f"Groq call failed: {e}")
    show_code(
        "Lecture 116 Groq SDK example",
        """
import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a helpful AI tutor."},
        {"role": "user", "content": "Explain embeddings in simple words."}
    ]
)

print(response.choices[0].message.content)
""",
    )


def render_lecture_117():
    lecture_header(117, "Using local and hosted models", "Compare local Ollama-style execution with hosted Groq-style execution.")
    st.code("Local: You → Your Computer → Local LLM → Response\nHosted: You → Cloud/API → Hosted LLM → Response", language="text")
    use_case = st.selectbox(
        "Choose a use case",
        ["Private documents", "Fast public chatbot", "Simple learning demo", "Large-scale app"],
        key="l117_case",
    )
    if use_case == "Private documents":
        route, reason = "Local model", "Privacy and data control are more important."
    elif use_case == "Fast public chatbot":
        route, reason = "Hosted model", "Fast responses and easy scaling are more important."
    elif use_case == "Simple learning demo":
        route, reason = "Local model", "A local setup is good for learning and experimentation."
    else:
        route, reason = "Hosted model", "Hosted inference is easier to scale and integrate."
    st.success(f"Recommended route: {route}")
    st.write(reason)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Local option")
        st.code(
            """
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3.2:3b")
response = llm.invoke("Explain embeddings in simple words.")
""",
            language="python",
        )
    with c2:
        st.markdown("#### Hosted option")
        st.code(
            """
from groq import Groq
client = Groq(api_key=os.environ["GROQ_API_KEY"])
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[...]
)
""",
            language="python",
        )
    show_code(
        "Lecture 117 decision rule",
        """
if privacy_is_important:
    use_local_model()
elif speed_is_important:
    use_hosted_model()
else:
    choose_best_fit()
""",
    )


def render_lecture_118():
    lecture_header(118, "API-based model integration", "Integrate Groq or similar hosted models through a clean API wrapper.")
    st.code("Frontend → API Call → Model Provider → Response", language="text")
    question = st.text_input("Question", value="What is a vector database?", key="l118_question")
    if st.button("Run API integration demo", key="l118_run"):
        client = get_groq_client()
        if client is None:
            st.warning("Groq API key or groq package is not available.")
        else:
            with st.spinner("Calling model API..."):
                try:
                    result = client.chat.completions.create(
                        model=groq_model,
                        messages=[
                            {"role": "system", "content": "You are a helpful AI tutor."},
                            {"role": "user", "content": question},
                        ],
                    )
                    st.subheader("Response")
                    st.write(result.choices[0].message.content)
                except Exception as e:
                    st.error(f"API call failed: {e}")
    st.code(
        """
def ask_model(question: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful AI tutor."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
""",
        language="python",
    )
    st.write("This lecture is about keeping the model call behind a reusable API wrapper.")


def render_lecture_119():
    lecture_header(119, "Speed and latency considerations", "Understand how speed affects user experience and why response time matters.")
    st.code("Request → Processing → Response", language="text")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Simulated fast response")
        if st.button("Run fast demo", key="l119_fast"):
            simple_speed_demo("Fast path", 0.35, "Short wait, smoother interaction.")
    with c2:
        st.markdown("#### Simulated slow response")
        if st.button("Run slow demo", key="l119_slow"):
            simple_speed_demo("Slow path", 1.8, "Longer wait, more noticeable delay.")
    st.code(
        """
- Keep prompts short and focused
- Use streaming when possible
- Avoid unnecessary history
- Choose the right model
- Cache repeated prefixes
""",
        language="text",
    )
    show_code(
        "Lecture 119 latency idea",
        """
# Latency = time from request to response
# Fast apps feel more interactive, even when answers are similar.
""",
    )


def render_lecture_120():
    lecture_header(120, "Model routing strategies", "Choose different models for different tasks, privacy needs, and performance goals.")
    st.code("Request → Router → Best Model → Response", language="text")
    task = st.text_input("Describe the task", value="Summarize this public article", key="l120_task")
    privacy = st.selectbox("Privacy level", ["Public", "Sensitive / Private"], key="l120_privacy")
    importance = st.selectbox("What matters most?", ["Speed", "Quality", "Cost", "Privacy"], key="l120_priority")
    complexity = st.selectbox("Task complexity", ["Simple", "Moderate", "Hard"], key="l120_complexity")

    def route_model(task_text: str, privacy_level: str, priority: str, complexity_level: str):
        t = task_text.lower()
        if privacy_level.startswith("Sensitive"):
            return "Local model", "Sensitive content should stay on your own machine."
        if "summarize" in t or "summary" in t:
            return "Fast hosted model", "Summarization usually benefits from a responsive hosted model."
        if "code" in t or "programming" in t:
            return "Specialized code model", "Code tasks often work better with a model tuned for coding."
        if complexity_level == "Hard" or priority == "Quality":
            return "Stronger hosted model", "Complex tasks often need higher-capability models."
        if priority == "Speed":
            return "Fast hosted model", "When speed matters most, choose a low-latency path."
        if priority == "Cost":
            return "Cheaper/smaller model", "Lower-cost models are enough for many simple tasks."
        return "General model", "A balanced general model is a good default choice."

    route, reason = route_model(task, privacy, importance, complexity)
    st.success(f"Recommended route: {route}")
    st.write(reason)

    if st.button("Show routing pseudocode", key="l120_route"):
        st.code(
            """
def choose_model(task, privacy, priority, complexity):
    if privacy == "Sensitive":
        return "local_model"
    if "summarize" in task.lower():
        return "fast_hosted_model"
    if "code" in task.lower():
        return "code_model"
    if complexity == "Hard":
        return "strong_reasoning_model"
    return "general_model"
""",
            language="python",
        )
    show_code(
        "Lecture 120 routing idea",
        """
# Routing means the app decides which model should handle each request.
# This makes the system more flexible, faster, cheaper, and safer.
""",
    )

st.sidebar.markdown("---")
st.sidebar.markdown("### Runtime note")
st.sidebar.write("Use this one file for all lectures, then switch from the sidebar.")
st.sidebar.write("For live model calls, set GROQ_API_KEY in your environment.")
st.sidebar.write("For local model sections, install and run Ollama separately.")

if lecture_choice == "Lecture 115":
    render_lecture_115()
elif lecture_choice == "Lecture 116":
    render_lecture_116()
elif lecture_choice == "Lecture 117":
    render_lecture_117()
elif lecture_choice == "Lecture 118":
    render_lecture_118()
elif lecture_choice == "Lecture 119":
    render_lecture_119()
elif lecture_choice == "Lecture 120":
    render_lecture_120()
