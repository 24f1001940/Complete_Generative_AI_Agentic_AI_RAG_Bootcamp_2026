from __future__ import annotations

from importlib import import_module

import streamlit as st


APP_TITLE = "Lecture 101 | Study Assistant"
APP_SUBTITLE = (
    "A polished LangChain + Streamlit demo that answers questions, keeps a small memory, "
    "and uses one reusable prompt template."
)

PROMPT_TEXT = (
    "You are a {tone} study assistant.\n"
    "Topic: {topic}\n"
    "Student question: {question}\n"
    "Conversation context: {memory}\n"
    "Answer depth: {depth}\n\n"
    "Write a structured response with these sections:\n"
    "1. Quick answer\n"
    "2. Explanation\n"
    "3. Example\n"
    "4. Checkpoint question\n"
    "5. Next step"
)


class LocalPromptTemplate:
    def __init__(self, *, input_variables: list[str], template: str) -> None:
        self.input_variables = input_variables
        self.template = template

    def format(self, **kwargs: str) -> str:
        return self.template.format(**kwargs)


class LocalStrOutputParser:
    def parse(self, text: str) -> str:
        return text


def build_prompt_objects() -> tuple[object, object]:
    try:
        prompt_module = import_module("langchain_core.prompts")
        parser_module = import_module("langchain_core.output_parsers")
        prompt_template = prompt_module.PromptTemplate(
            input_variables=["topic", "question", "memory", "tone", "depth"],
            template=PROMPT_TEXT,
        )
        return prompt_template, parser_module.StrOutputParser()
    except ModuleNotFoundError:
        prompt_template = LocalPromptTemplate(
            input_variables=["topic", "question", "memory", "tone", "depth"],
            template=PROMPT_TEXT,
        )
        return prompt_template, LocalStrOutputParser()


PROMPT_TEMPLATE, OUTPUT_PARSER = build_prompt_objects()


def init_state() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Ask me about the topic in the sidebar. I will keep a short memory and "
                    "return a structured study answer."
                ),
            }
        ]

    if "topic" not in st.session_state:
        st.session_state.topic = "LangChain basics"

    if "tone" not in st.session_state:
        st.session_state.tone = "clear and supportive"

    if "depth" not in st.session_state:
        st.session_state.depth = "balanced"


def detect_intent(question: str) -> str:
    lowered = question.lower()

    if any(word in lowered for word in ["what", "define", "meaning"]):
        return "definition"
    if any(word in lowered for word in ["how", "build", "create", "make"]):
        return "build"
    if any(word in lowered for word in ["why", "reason", "benefit"]):
        return "why"
    if any(word in lowered for word in ["example", "show", "sample"]):
        return "example"

    return "overview"


def compose_response(topic: str, question: str, memory: str, tone: str, depth: str) -> str:
    prompt_text = PROMPT_TEMPLATE.format(
        topic=topic,
        question=question,
        memory=memory or "No previous context yet.",
        tone=tone,
        depth=depth,
    )

    intent = detect_intent(question)

    quick_answer_map = {
        "definition": f"{topic} is the core concept you are asking about, and it can be understood as the main idea behind the topic.",
        "build": f"To build with {topic}, start with the smallest working example, then add data flow, memory, and formatting step by step.",
        "why": f"{topic} matters because it helps you turn raw input into a repeatable learning workflow.",
        "example": f"A simple example of {topic} is asking a question, keeping context from the last turn, and returning an organized answer.",
        "overview": f"{topic} works best when you combine a clear prompt, a bit of memory, and a structured response format.",
    }

    explanation_map = {
        "definition": (
            f"For this lecture, treat {topic} as the thing you want the assistant to help explain. "
            "The app uses the same prompt template every time, so the response style stays consistent."
        ),
        "build": (
            "The app follows a simple loop: collect the user's question, load the recent conversation, "
            "format a prompt, and render the answer in a clean UI."
        ),
        "why": (
            "This pattern is useful because it separates presentation from prompt design. "
            "That makes the app easier to teach, debug, and extend later with a real model."
        ),
        "example": (
            "If the topic is prompt templates, the assistant can explain how placeholders become a reusable instruction, "
            "then show a sample input and answer format."
        ),
        "overview": (
            "Using a reusable template keeps the app predictable. The memory buffer gives the assistant a little context, "
            "and the structured output helps the learner see the shape of a good answer."
        ),
    }

    example_map = {
        "definition": (
            f"Example: 'Explain {topic} to a beginner' can become a short answer with a definition, a tiny example, and one practice question."
        ),
        "build": (
            "Example: a learner asks a follow-up question, and the app includes the last few turns so the answer does not restart from zero."
        ),
        "why": (
            "Example: instead of dumping a paragraph, the assistant can split the answer into quick answer, explanation, and next step."
        ),
        "example": (
            f"Example: if you ask about {topic}, the assistant can respond with a one-line summary, a practical analogy, and a small exercise."
        ),
        "overview": (
            "Example: a prompt template with placeholders for topic, question, and memory can be reused across many lessons."
        ),
    }

    next_step_map = {
        "definition": "Try asking the same idea in your own words.",
        "build": "Try adding one more feature, such as a reset button or a model selector.",
        "why": "Try comparing this layout with a plain text demo to see the difference in usability.",
        "example": "Try changing the topic in the sidebar and ask a different type of question.",
        "overview": "Try asking a follow-up question so the memory block becomes visible in the response.",
    }

    rendered_answer = (
        f"Quick answer:\n{quick_answer_map[intent]}\n\n"
        f"Explanation:\n{explanation_map[intent]}\n\n"
        f"Example:\n{example_map[intent]}\n\n"
        f"Checkpoint question:\nWhat would you change if the topic were for an intermediate learner?\n\n"
        f"Next step:\n{next_step_map[intent]}"
    )

    final_answer = OUTPUT_PARSER.parse(rendered_answer)
    return final_answer + "\n\nPrompt used:\n" + prompt_text


def render_message(message: dict[str, str]) -> None:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="📘", layout="wide")
    init_state()

    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(224, 242, 241, 0.95), transparent 38%),
                    radial-gradient(circle at top right, rgba(255, 243, 224, 0.9), transparent 34%),
                    linear-gradient(180deg, #f8fafc 0%, #eef5f4 100%);
            }
            .hero {
                padding: 1.25rem 1.4rem;
                border-radius: 1.25rem;
                background: linear-gradient(135deg, rgba(10, 38, 64, 0.96), rgba(20, 94, 116, 0.92));
                color: white;
                box-shadow: 0 18px 50px rgba(15, 23, 42, 0.18);
                margin-bottom: 1rem;
            }
            .hero h1 {
                margin: 0;
                font-size: 2.1rem;
            }
            .hero p {
                margin: 0.4rem 0 0;
                font-size: 1rem;
                opacity: 0.92;
            }
            .metric-card {
                border-radius: 1rem;
                padding: 0.9rem 1rem;
                background: rgba(255, 255, 255, 0.75);
                border: 1px solid rgba(148, 163, 184, 0.25);
                box-shadow: 0 10px 28px rgba(15, 23, 42, 0.06);
            }
            .hint {
                border-left: 4px solid #0f766e;
                background: rgba(255, 255, 255, 0.8);
                padding: 0.9rem 1rem;
                border-radius: 0.8rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="hero">
            <h1>{APP_TITLE}</h1>
            <p>{APP_SUBTITLE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.header("Assistant Settings")
        st.session_state.topic = st.text_input("Topic", value=st.session_state.topic)
        st.session_state.tone = st.selectbox(
            "Tone",
            ["clear and supportive", "concise and direct", "friendly and detailed"],
            index=["clear and supportive", "concise and direct", "friendly and detailed"].index(st.session_state.tone),
        )
        st.session_state.depth = st.select_slider(
            "Depth",
            options=["short", "balanced", "detailed"],
            value=st.session_state.depth,
        )

        st.divider()
        st.subheader("Quick Topics")
        if st.button("LangChain basics", use_container_width=True):
            st.session_state.topic = "LangChain basics"
        if st.button("Prompt templates", use_container_width=True):
            st.session_state.topic = "Prompt templates"
        if st.button("Conversation memory", use_container_width=True):
            st.session_state.topic = "Conversation memory"

        st.divider()
        if st.button("Clear chat", use_container_width=True):
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": (
                        "Ask me about the topic in the sidebar. I will keep a short memory and "
                        "return a structured study answer."
                    ),
                }
            ]
            st.rerun()

    left, middle, right = st.columns(3)
    with left:
        st.markdown(
            f"<div class='metric-card'><strong>Current topic</strong><br>{st.session_state.topic}</div>",
            unsafe_allow_html=True,
        )
    with middle:
        st.markdown(
            f"<div class='metric-card'><strong>Turns remembered</strong><br>{max(len(st.session_state.messages) - 1, 0)}</div>",
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            f"<div class='metric-card'><strong>Answer style</strong><br>{st.session_state.tone}</div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        "<div class='hint'>Ask a question, then open the prompt preview to see how the reusable template is built.</div>",
        unsafe_allow_html=True,
    )

    for message in st.session_state.messages:
        render_message(message)

    question = st.chat_input(f"Ask about {st.session_state.topic}")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})

        recent_context = st.session_state.messages[-6:]
        memory_text = "\n".join(f"{item['role']}: {item['content']}" for item in recent_context)
        assistant_reply = compose_response(
            topic=st.session_state.topic,
            question=question,
            memory=memory_text,
            tone=st.session_state.tone,
            depth=st.session_state.depth,
        )
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        st.rerun()

    with st.expander("Prompt template preview"):
        st.code(
            PROMPT_TEMPLATE.format(
                topic=st.session_state.topic,
                question="How does this work?",
                memory="assistant: previous topic summary",
                tone=st.session_state.tone,
                depth=st.session_state.depth,
            ),
            language="text",
        )

    with st.expander("Conversation memory"):
        st.write(st.session_state.messages[-6:])


if __name__ == "__main__":
    main()