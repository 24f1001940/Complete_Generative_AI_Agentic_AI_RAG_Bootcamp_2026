
import json
from dataclasses import dataclass, asdict

import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Section 23: Production GenAI",
    page_icon="🚀",
    layout="wide",
)

st.title("Section 23: Production GenAI")
st.caption("Lecture-wise demo app for Lectures 125–128. Use the sidebar to switch lectures without editing code.")

LECTURES = {
    "Lecture 125": "Conversation Memory Design, Stateful Assistants & Middleware Controls",
    "Lecture 126": "LangSmith Observability: Tracing Workflows, Debugging & App Evaluation",
    "Lecture 127": "GenAI App Deployment: Streamlit Cloud, Hugging Face Spaces & LangServe APIs",
    "Lecture 128": "Enterprise Infrastructure: AWS Lifecycle, Scaling Architecture & Reliability",
}

lecture = st.sidebar.radio("Choose a lecture", list(LECTURES.keys()), index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### Installation")
st.sidebar.code(
    """pip install -r requirements.txt
streamlit run app.py""",
    language="bash",
)
st.sidebar.markdown(
    "This app is self-contained and uses simulated visuals so you can record lecture by lecture without changing files."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Optional environment variables")
st.sidebar.code(
    """GROQ_API_KEY=your_key_here
LANGSMITH_API_KEY=your_key_here
LANGCHAIN_TRACING_V2=true""",
    language="text",
)

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
def lecture_header(num: int, title: str, subtitle: str) -> None:
    st.subheader(f"Lecture {num} – {title}")
    st.write(subtitle)


def show_code(title: str, code: str, language: str = "python") -> None:
    with st.expander(f"Show code: {title}", expanded=False):
        st.code(code.strip(), language=language)


def latency_from_users(users: int) -> float:
    return round(0.35 + (users / 1500.0) ** 1.4 * 2.8, 2)


def cost_from_users(users: int) -> float:
    return round(0.08 + users * 0.0045, 2)


# ------------------------------------------------------------
# Lecture 125
# ------------------------------------------------------------
def render_lecture_125():
    lecture_header(
        125,
        "Conversation Memory Design, Stateful Assistants & Middleware Controls",
        "Design memory intentionally: keep useful context, summarize old turns, and control the flow with middleware.",
    )

    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        st.markdown("### Simulated conversation")
        if "sec23_messages" not in st.session_state:
            st.session_state.sec23_messages = [
                {"role": "assistant", "content": "Hello! I remember the current conversation."}
            ]
        if "sec23_summary" not in st.session_state:
            st.session_state.sec23_summary = "The assistant is helping the user learn GenAI concepts."

        for msg in st.session_state.sec23_messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        user_input = st.chat_input("Type a message for the memory demo...", key="sec23_chat")
        if user_input:
            st.session_state.sec23_messages.append({"role": "user", "content": user_input})

            if len(st.session_state.sec23_messages) > 8:
                recent_text = " ".join(m["content"] for m in st.session_state.sec23_messages[:-4])
                st.session_state.sec23_summary = (
                    "Earlier conversation: "
                    + recent_text[:180]
                    + ("..." if len(recent_text) > 180 else "")
                )
                st.session_state.sec23_messages = st.session_state.sec23_messages[-4:]

            response = f"Got it. I will use the current topic and the summary: {st.session_state.sec23_summary}"
            st.session_state.sec23_messages.append({"role": "assistant", "content": response})
            st.rerun()

    with col2:
        st.markdown("### Memory controls")
        summary_enabled = st.toggle("Enable summarization", value=True)
        trim_enabled = st.toggle("Enable trimming", value=True)
        human_review = st.toggle("Human-in-the-loop checkpoint", value=False)

        st.metric("Stored messages", len(st.session_state.sec23_messages))
        st.info("Stateful assistants remember useful context across turns. Middleware controls how that memory is used.")

        if summary_enabled:
            st.success("Summarization is ON")
        else:
            st.warning("Summarization is OFF")

        if trim_enabled:
            st.success("Trimming is ON")
        else:
            st.warning("Trimming is OFF")

        if human_review:
            st.error("Human review step enabled")

        st.markdown("### Current summary")
        st.write(st.session_state.sec23_summary)

        st.markdown("### Middleware pipeline")
        st.code(
            """
Input
  ↓
Middleware
  ↓
Memory / Summary / Trim
  ↓
Model
  ↓
Response
""".strip(),
            language="text",
        )

        show_code(
            "Lecture 125 idea",
            """
# Memory design logic
# - keep recent conversation
# - summarize older turns
# - remove noisy context
# - optionally require human review
""",
        )

    st.markdown("---")
    st.markdown("### Visual explanation")
    left, right = st.columns(2)
    with left:
        st.code("Short-term memory = recent messages", language="text")
        st.code("Long-term memory = summary / important facts", language="text")
    with right:
        st.code("Middleware = control layer", language="text")
        st.code("Stateful assistant = remembers conversation state", language="text")


# ------------------------------------------------------------
# Lecture 126
# ------------------------------------------------------------
def render_lecture_126():
    lecture_header(
        126,
        "LangSmith Observability: Tracing Workflows, Debugging & App Evaluation",
        "See inside the workflow so you can debug prompts, retrievers, tools, and outputs step by step.",
    )

    st.markdown("### Simulated trace")
    trace_steps = [
        {"step": "Input", "status": "ok", "latency_ms": 12},
        {"step": "Prompt build", "status": "ok", "latency_ms": 18},
        {"step": "Retriever", "status": "ok", "latency_ms": 40},
        {"step": "LLM", "status": "ok", "latency_ms": 260},
        {"step": "Parser", "status": "ok", "latency_ms": 8},
        {"step": "Final output", "status": "ok", "latency_ms": 5},
    ]

    fig = go.Figure(
        go.Bar(
            x=[x["latency_ms"] for x in trace_steps],
            y=[x["step"] for x in trace_steps],
            orientation="h",
        )
    )
    fig.update_layout(
        title="Trace timeline (simulated)",
        xaxis_title="Latency (ms)",
        yaxis_title="Step",
        height=420,
    )
    st.plotly_chart(fig, use_container_width=True)

    cols = st.columns([1, 1])
    with cols[0]:
        st.markdown("### Trace table")
        st.dataframe(trace_steps, use_container_width=True, hide_index=True)

    with cols[1]:
        st.markdown("### Debug checklist")
        st.code(
            """
What to inspect in a trace:
- user input
- prompt text
- retrieved chunks
- tool input/output
- model response
- parsing errors
- latency hotspots
""".strip(),
            language="text",
        )
        st.info("Observability helps you identify whether the prompt, retriever, tool, or model caused the issue.")

    st.markdown("### Evaluation questions")
    eval_score = st.slider("Overall quality score", 0, 100, 82)
    st.progress(eval_score / 100)
    st.write(f"Quality score: **{eval_score}/100**")

    show_code(
        "Lecture 126 idea",
        """
# In a real setup, LangSmith would show:
# - trace tree
# - prompt
# - model call
# - retriever result
# - latency
# - errors
""",
    )


# ------------------------------------------------------------
# Lecture 127
# ------------------------------------------------------------
def render_lecture_127():
    lecture_header(
        127,
        "GenAI App Deployment: Streamlit Cloud, Hugging Face Spaces & LangServe APIs",
        "Choose the right deployment style depending on whether you need a UI demo or an API backend.",
    )

    col1, col2 = st.columns(2)

    with col1:
        platform = st.selectbox(
            "Choose deployment target",
            ["Streamlit Cloud", "Hugging Face Spaces", "LangServe API"],
            index=0,
        )
        st.markdown("### Deployment flow")
        if platform == "Streamlit Cloud":
            st.code(
                """
GitHub repo
  ↓
Streamlit Cloud
  ↓
Browser UI
""".strip(),
                language="text",
            )
            st.success("Best for quick Streamlit demos and classroom projects.")
        elif platform == "Hugging Face Spaces":
            st.code(
                """
GitHub repo
  ↓
HF Spaces
  ↓
Public AI demo
""".strip(),
                language="text",
            )
            st.success("Great for shareable demos and AI showcases.")
        else:
            st.code(
                """
LangChain chain
  ↓
LangServe
  ↓
API endpoint
  ↓
Frontend / mobile / other backend
""".strip(),
                language="text",
            )
            st.success("Best when you want to expose AI logic as an API backend.")

    with col2:
        st.markdown("### UI vs API decision")
        need_ui = st.toggle("Need a visible web app UI", value=True)
        need_api = st.toggle("Need a reusable backend API", value=False)
        need_public_demo = st.toggle("Need a public demo link", value=True)

        if need_ui and not need_api:
            recommendation = "Streamlit Cloud"
        elif need_public_demo and need_ui:
            recommendation = "Hugging Face Spaces"
        elif need_api:
            recommendation = "LangServe API"
        else:
            recommendation = "Depends on your architecture"

        st.metric("Recommended target", recommendation)

        st.markdown("### Deployment checklist")
        st.code(
            """
- test locally first
- add requirements.txt
- use environment variables
- separate UI from backend
- keep the app lightweight
- verify model/API access after deployment
""".strip(),
            language="text",
        )

    st.markdown("---")
    st.markdown("### Architecture snapshot")
    st.code(
        """
Frontend (Streamlit / HF Spaces)
   ↓
Backend (LangServe API)
   ↓
Model / Retrieval / Tools
""".strip(),
        language="text",
    )

    show_code(
        "Lecture 127 idea",
        """
# Streamlit Cloud -> easy UI hosting
# Hugging Face Spaces -> public demos
# LangServe -> backend API deployment
""",
    )


# ------------------------------------------------------------
# Lecture 128
# ------------------------------------------------------------
def render_lecture_128():
    lecture_header(
        128,
        "Enterprise Infrastructure: AWS Lifecycle, Scaling Architecture & Reliability",
        "Understand how GenAI systems behave when users grow, load increases, and reliability becomes essential.",
    )

    users = st.slider("Estimated concurrent users", 10, 5000, 250, step=10)
    latency = latency_from_users(users)
    cost = cost_from_users(users)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Users", f"{users}")
    c2.metric("Latency (simulated)", f"{latency} sec")
    c3.metric("Monthly cost (simulated)", f"${cost}")
    c4.metric("Reliability concern", "Rising" if users > 1000 else "Stable")

    st.markdown("### Scaling architecture")
    st.code(
        """
Users
  ↓
Load Balancer
  ↓
Backend Service
  ↓
Model / Retrieval Layer
  ↓
Monitoring / Logging
""".strip(),
        language="text",
    )

    st.markdown("### Latency trend")
    user_points = [10, 100, 250, 500, 1000, 2000, 3000, 5000]
    latency_points = [latency_from_users(u) for u in user_points]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=user_points, y=latency_points, mode="lines+markers", name="Latency"))
    fig.update_layout(
        title="Simulated latency growth as users increase",
        xaxis_title="Concurrent users",
        yaxis_title="Latency (sec)",
        height=420,
    )
    st.plotly_chart(fig, use_container_width=True)

    cols = st.columns(2)
    with cols[0]:
        st.markdown("### Reliability checklist")
        st.code(
            """
- retries
- fallback models
- monitoring
- alerting
- queueing
- caching
- graceful failure handling
""".strip(),
            language="text",
        )
    with cols[1]:
        st.markdown("### AWS lifecycle thinking")
        st.code(
            """
Build → Deploy → Monitor → Scale → Maintain
""".strip(),
            language="text",
        )
        st.info("Production systems must stay stable not only at launch, but across the whole lifecycle.")

    st.markdown("### Failure handling demo")
    fail_prob = st.slider("Failure likelihood", 0, 100, 12)
    if fail_prob > 50:
        st.error("Primary service unstable: use retry / fallback / queue.")
    elif fail_prob > 20:
        st.warning("System under pressure: watch latency and errors.")
    else:
        st.success("System healthy: current load looks manageable.")

    show_code(
        "Lecture 128 idea",
        """
# Enterprise thinking:
# - plan for growth
# - monitor latency
# - handle failures gracefully
# - separate responsibilities
# - keep the system maintainable
""",
    )


if lecture == "Lecture 125":
    render_lecture_125()
elif lecture == "Lecture 126":
    render_lecture_126()
elif lecture == "Lecture 127":
    render_lecture_127()
elif lecture == "Lecture 128":
    render_lecture_128()
