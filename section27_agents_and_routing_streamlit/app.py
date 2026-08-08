
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Section 28: Agents & Routing",
    page_icon="🤖",
    layout="wide",
)

st.title("Section 28: Agents & Routing")
st.caption(
    "Lecture-wise demo app for Lectures 145–148. Switch lectures from the sidebar without editing code."
)

LECTURES = {
    "Lecture 145": "ReAct Architecture, ToolNode Basics & Structured Decisions",
    "Lecture 146": "Agentic RAG: Query Planning, Thought Chains & Reflection",
    "Lecture 147": "Production RAG: Corrective RAG & Adaptive RAG",
    "Lecture 148": "Multi-Agent Systems: Protocols, Supervisors & Routing",
}

lecture = st.sidebar.radio("Choose a lecture", list(LECTURES.keys()), index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("### Install")
st.sidebar.code(
    "pip install -r requirements.txt\nstreamlit run app.py",
    language="bash",
)
st.sidebar.markdown(
    "This app is a single reusable file for the entire section so you can record lecture by lecture."
)
st.sidebar.markdown("---")
st.sidebar.info(
    "Tip: keep the demos lightweight while recording so the app stays responsive on your laptop."
)

def lecture_header(num: int, title: str, subtitle: str) -> None:
    st.subheader(f"Lecture {num} – {title}")
    st.write(subtitle)

def show_code(title: str, code: str, language: str = "python") -> None:
    with st.expander(f"Show code: {title}", expanded=False):
        st.code(code.strip(), language=language)

def show_flow(title: str, steps):
    fig = go.Figure()
    x = list(range(len(steps)))
    fig.add_trace(go.Scatter(
        x=x, y=[1] * len(steps), mode="markers+text",
        text=steps, textposition="bottom center",
        marker=dict(size=26), hoverinfo="none"
    ))
    for i in range(len(steps) - 1):
        fig.add_annotation(
            x=i + 0.95, y=1,
            ax=i + 0.05, ay=1,
            axref="x", ayref="y",
            xref="x", yref="y",
            showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2
        )
    fig.update_layout(
        title=title,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, range=[0.7, 1.3]),
        height=220,
        margin=dict(l=20, r=20, t=50, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

def lecture_145():
    lecture_header(
        145,
        "ReAct Architecture, ToolNode Basics & Structured Decisions",
        "Understand reasoning + acting, how ToolNode works, and how structured decisions keep agents reliable.",
    )

    c1, c2 = st.columns([1.05, 0.95])

    with c1:
        st.markdown("### ReAct loop")
        st.code("Thought → Action → Observation → Thought → Answer", language="text")
        show_flow("ReAct execution loop", ["Thought", "Action", "Observation", "Thought", "Answer"])

        q = st.text_input("Ask a sample tool question", value="What is 34 plus 18?")
        if st.button("Run decision demo", key="l145_run"):
            if "plus" in q.lower() or "add" in q.lower():
                action = "calculator"
                observation = 52
            else:
                action = "direct_answer"
                observation = "No tool needed"
            st.success(f"Chosen action: {action}")
            st.write(f"Observation: {observation}")
            st.write(f"Final answer: {observation if action == 'calculator' else 'Respond directly'}")

    with c2:
        st.markdown("### Architecture view")
        st.code(
            "User Request\n   ↓\nSupervisor / Reasoning\n   ↓\nTool Selection\n   ↓\nToolNode Execution\n   ↓\nObservation\n   ↓\nFinal Answer",
            language="text",
        )
        st.info("ReAct combines reasoning and acting in a loop. ToolNode executes tools inside the workflow.")

    show_code(
        "Lecture 145 tool snippet",
        """
from langchain.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    \"\"\"Add two numbers.\"\"\"
    return a + b

result = add_numbers.invoke({"a": 34, "b": 18})
""",
    )

def lecture_146():
    lecture_header(
        146,
        "Agentic RAG: Query Planning, Thought Chains & Reflection",
        "Use planning and reflection to make retrieval smarter for complex questions.",
    )

    c1, c2 = st.columns([1.05, 0.95])

    with c1:
        st.markdown("### Agentic RAG flow")
        st.code("Plan → Retrieve → Reason → Reflect → Answer", language="text")
        show_flow("Agentic RAG workflow", ["Plan", "Retrieve", "Reason", "Reflect", "Answer"])

        q = st.text_input(
            "Complex question",
            value="How does Agentic RAG work and when should it be used?",
            key="l146_q",
        )
        if st.button("Run planning demo", key="l146_run"):
            if " and " in q.lower() or "when" in q.lower():
                sub_questions = [
                    "How does Agentic RAG work?",
                    "When should Agentic RAG be used?",
                ]
            else:
                sub_questions = [q]
            st.success("Query plan generated")
            st.write("Sub-questions:")
            st.write(sub_questions)
            st.write("Reflection: check whether the answer is grounded, complete, and clear.")

    with c2:
        st.markdown("### Planning and reflection")
        st.code(
            "question = \"How does Agentic RAG work and when should it be used?\"\n\nsub_questions = [\n    \"How does Agentic RAG work?\",\n    \"When should Agentic RAG be used?\"\n]\n\n# retrieve evidence for each sub-question\n# reason over the evidence\n# reflect on completeness",
            language="text",
        )
        st.info("Agentic RAG breaks complex queries into smaller steps and can reflect before finalizing the answer.")

    show_code(
        "Lecture 146 agentic RAG snippet",
        """
def plan(question):
    if "and" in question.lower() or "when" in question.lower():
        return ["decompose", "retrieve", "reflect"]
    return ["retrieve", "answer"]
""",
    )

def lecture_147():
    lecture_header(
        147,
        "Production RAG: Corrective RAG & Adaptive RAG",
        "Detect weak retrieval, correct it, and adapt the retrieval strategy based on the query.",
    )

    c1, c2 = st.columns([1.05, 0.95])

    with c1:
        st.markdown("### CRAG and Adaptive RAG")
        st.code("Question → Retrieve → Check Quality → Correct / Adapt → Answer", language="text")
        show_flow("Corrective + Adaptive retrieval", ["Question", "Retrieve", "Check", "Correct/Adapt", "Answer"])

        q = st.text_input("Retrieval query", value="Explain how RAG improves answer quality.", key="l147_q")
        if st.button("Run correction demo", key="l147_run"):
            if len(q.strip()) < 10:
                quality = "weak"
                strategy = "expanded"
            elif "compare" in q.lower():
                quality = "good"
                strategy = "multi_source"
            else:
                quality = "good"
                strategy = "standard"
            st.success(f"Retrieval quality: {quality}")
            st.write(f"Adaptive strategy: {strategy}")

    with c2:
        st.markdown("### CRAG vs Adaptive RAG")
        st.table([
            {"Pattern": "CRAG", "Goal": "Correct weak retrieval", "When": "After retrieval"},
            {"Pattern": "Adaptive RAG", "Goal": "Change retrieval strategy", "When": "Before or during retrieval"},
        ])
        st.info("CRAG repairs weak context; Adaptive RAG chooses the right retrieval behavior for the query.")

    show_code(
        "Lecture 147 correction snippet",
        """
def is_retrieval_good(chunks):
    return len(chunks) > 0 and all(len(chunk.strip()) > 20 for chunk in chunks)

def choose_retrieval_strategy(question):
    if "compare" in question.lower():
        return "multi_source"
    if "why" in question.lower():
        return "expanded"
    return "standard"
""",
    )

def lecture_148():
    lecture_header(
        148,
        "Multi-Agent Systems: Protocols, Supervisors & Routing",
        "Coordinate specialized agents through protocols, a supervisor, and routing logic.",
    )

    c1, c2 = st.columns([1.05, 0.95])

    with c1:
        st.markdown("### Multi-agent architecture")
        st.code("User → Supervisor → Worker Agents → Reviewer → Final Answer", language="text")
        show_flow("Multi-agent coordination", ["User", "Supervisor", "Worker A", "Worker B", "Reviewer", "Answer"])

        task = st.text_input(
            "Task to route",
            value="Research and summarize recent RAG strategies.",
            key="l148_task",
        )
        if st.button("Run routing demo", key="l148_run"):
            t = task.lower()
            if "research" in t:
                route = "research_agent"
            elif "write" in t:
                route = "writer_agent"
            else:
                route = "review_agent"
            st.success(f"Supervisor routed the task to: {route}")
            st.write("Protocol: structured handoff between agents, then review before final response.")

    with c2:
        st.markdown("### Supervisor and routing")
        st.table([
            {"Component": "Protocol", "Role": "Defines message handoff rules"},
            {"Component": "Supervisor", "Role": "Chooses the next agent"},
            {"Component": "Routing", "Role": "Sends the task to the right specialist"},
        ])
        st.info("Multi-agent systems work best when each agent has a clear role and communication is structured.")

    show_code(
        "Lecture 148 supervisor snippet",
        """
def supervisor(task):
    if "research" in task.lower():
        return "research_agent"
    if "write" in task.lower():
        return "writer_agent"
    return "review_agent"
""",
    )

if lecture == "Lecture 145":
    lecture_145()
elif lecture == "Lecture 146":
    lecture_146()
elif lecture == "Lecture 147":
    lecture_147()
elif lecture == "Lecture 148":
    lecture_148()
