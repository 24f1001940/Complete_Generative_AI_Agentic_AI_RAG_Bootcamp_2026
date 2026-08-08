import json
from pathlib import Path

import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

ROOT = Path(__file__).resolve().parent

DATA_FILE = (
    ROOT
    / "section_data"
    / "sections.json"
)


st.set_page_config(
    page_title="Complete Generative AI Bootcamp",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# LOAD COURSE DATA
# ============================================================

@st.cache_data
def load_course_data():

    with open(
        DATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


data = load_course_data()

sections = data["sections"]

course_name = data.get(
    "course_name",
    "Complete Generative AI, Agentic AI & RAG Bootcamp"
)

author = data.get(
    "author",
    "MOHD SAQIB"
)

github_url = data.get(
    "github_url",
    "https://github.com/24f1001940/Complete_Generative_AI_Agentic_AI_RAG_Bootcamp_2026"
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_lecture_file(
    section_number,
    lecture_number
):

    return (
        ROOT
        / "lectures"
        / f"section_{section_number:02d}"
        / f"lecture_{lecture_number:03d}.py"
    )


def get_lecture_notes(
    section_number,
    lecture_number
):

    return (
        ROOT
        / "lectures"
        / f"section_{section_number:02d}"
        / f"lecture_{lecture_number:03d}.md"
    )


def read_text_file(path):

    if not path.exists():

        return None

    return path.read_text(
        encoding="utf-8",
        errors="ignore"
    )


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

.main-title {

    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 0.2rem;

}

.subtitle {

    color: #64748b;
    font-size: 1.05rem;
    margin-bottom: 1.5rem;

}

.course-card {

    padding: 1.2rem;

    border-radius: 18px;

    border: 1px solid #e2e8f0;

    background: white;

    margin-bottom: 1rem;

}

.footer {

    margin-top: 4rem;

    padding: 1rem;

    text-align: center;

    color: #64748b;

    border-top: 1px solid #e2e8f0;

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    f"""
<div class="main-title">
Complete Generative AI, Agentic AI & RAG Bootcamp
</div>

<div class="subtitle">
Official Course Resource Hub • 33 Sections • 164 Lectures
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        f"## {author}"
    )

    st.caption(
        "Course Resource Hub"
    )

    st.divider()

    navigation = st.radio(
        "Navigation",
        [
            "Home",
            "Section Explorer",
            "Lecture Search",
            "Projects",
            "Resources",
            "About Course"
        ]
    )

    st.divider()

    st.markdown(
        "### Repository"
    )

    st.link_button(
        "Open GitHub",
        github_url,
        use_container_width=True
    )


# ============================================================
# HOME
# ============================================================

if navigation == "Home":

    st.markdown(
        "## Welcome to the Course Resource Hub"
    )

    st.write(
        """
        This repository contains the programming resources,
        lecture code, notes, projects and supporting material
        for the Complete Generative AI, Agentic AI & RAG Bootcamp.
        """
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Sections",
        "33"
    )

    col2.metric(
        "Lectures",
        "164"
    )

    col3.metric(
        "Projects",
        "3"
    )

    col4.metric(
        "Author",
        "MOHD SAQIB"
    )

    st.divider()

    st.markdown(
        "### Learning Journey"
    )

    journey = [
        "Python",
        "NLP",
        "Deep Learning",
        "Transformers",
        "Generative AI",
        "RAG",
        "Agentic AI",
        "Multi-Agent Systems",
        "Enterprise AI",
        "Cloud Deployment"
    ]

    cols = st.columns(5)

    for index, item in enumerate(journey):

        cols[index % 5].info(
            item
        )

    st.divider()

    st.markdown(
        "### How to use this hub"
    )

    st.markdown(
        """
        1. Select a section from the sidebar.
        2. Select a lecture.
        3. Read the lecture notes.
        4. Study the source code.
        5. Download the code.
        6. Complete the associated exercises.
        7. Build the projects.
        """
    )


# ============================================================
# SECTION EXPLORER
# ============================================================

elif navigation == "Section Explorer":

    st.header(
        "Section Explorer"
    )

    section_labels = [
        f"Section {s['section_number']:02d} — {s['section_title']}"
        for s in sections
    ]

    selected_label = st.selectbox(
        "Select a section",
        section_labels
    )

    selected_index = (
        section_labels.index(
            selected_label
        )
    )

    section = sections[
        selected_index
    ]

    st.subheader(
        f"Section {section['section_number']}: "
        f"{section['section_title']}"
    )

    if section.get("summary"):

        st.write(
            section["summary"]
        )

    st.divider()

    st.markdown(
        "### Lectures"
    )

    for lecture in section["lectures"]:

        st.markdown(
            f"**Lecture {lecture['lecture_number']}**  \n"
            f"{lecture['lecture_title']}"
        )

        st.divider()


# ============================================================
# LECTURE SEARCH
# ============================================================

elif navigation == "Lecture Search":

    st.header(
        "Search Across All 164 Lectures"
    )

    query = st.text_input(
        "Search",
        placeholder="Try: RAG, LangGraph, Python, Neo4j, MCP..."
    )

    if query:

        query = query.lower()

        results = []

        for section in sections:

            for lecture in section["lectures"]:

                searchable_text = (
                    f"{section['section_title']} "
                    f"{lecture['lecture_title']}"
                ).lower()

                if query in searchable_text:

                    results.append(
                        (
                            section,
                            lecture
                        )
                    )

        st.write(
            f"Found {len(results)} lecture(s)."
        )

        for section, lecture in results:

            with st.expander(
                f"Lecture {lecture['lecture_number']}: "
                f"{lecture['lecture_title']}"
            ):

                st.caption(
                    f"Section {section['section_number']}: "
                    f"{section['section_title']}"
                )


# ============================================================
# PROJECTS
# ============================================================

elif navigation == "Projects":

    st.header(
        "Enterprise Capstone Projects"
    )

    projects = [

        (
            "Project 1",
            "Multi-Document RAG Q&A Engine",
            "Build a document-grounded question answering system with citations."
        ),

        (
            "Project 2",
            "Autonomous Web Research & Real-Time News Agent",
            "Build an autonomous research workflow that searches, processes and synthesizes information."
        ),

        (
            "Project 3",
            "Autonomous Code Engineering Agent",
            "Build a multi-agent system capable of planning, coding, testing and debugging."
        )

    ]

    for name, title, description in projects:

        with st.container(border=True):

            st.subheader(
                f"{name}: {title}"
            )

            st.write(
                description
            )


# ============================================================
# RESOURCES
# ============================================================

elif navigation == "Resources":

    st.header(
        "Course Resources"
    )

    resource_groups = {

        "Ebooks":
            ROOT / "resources" / "ebooks",

        "Section Notes":
            ROOT / "resources" / "section_notes",

        "Assignments":
            ROOT / "resources" / "assignments",

        "Quizzes":
            ROOT / "resources" / "quizzes",

        "Coding Exercises":
            ROOT / "resources" / "coding_exercises",

        "Role Plays":
            ROOT / "resources" / "role_plays",

        "Projects":
            ROOT / "resources" / "projects",

    }

    for title, folder in resource_groups.items():

        st.subheader(
            title
        )

        if folder.exists():

            files = list(
                folder.iterdir()
            )

            if not files:

                st.caption(
                    "Resources will be added here."
                )

            else:

                for file in files:

                    st.write(
                        f"• {file.name}"
                    )


# ============================================================
# ABOUT
# ============================================================

elif navigation == "About Course":

    st.header(
        "About the Course"
    )

    st.markdown(
        """
        ## Complete Generative AI, Agentic AI & RAG Bootcamp

        This course takes learners from Python foundations
        through modern enterprise Generative AI systems.

        ### Major learning areas

        - Python engineering
        - NLP
        - Deep Learning
        - Transformers
        - Large Language Models
        - Prompt Engineering
        - Hugging Face
        - LangChain
        - Embeddings
        - Vector Databases
        - Retrieval-Augmented Generation
        - Advanced RAG
        - LangGraph
        - Agentic AI
        - Multi-Agent Systems
        - Knowledge Graphs
        - GraphRAG
        - Fine-Tuning
        - MCP
        - Enterprise AI
        - Cloud Deployment
        """
    )

    st.divider()

    st.markdown(
        f"""
        **Course:** {course_name}

        **Author:** {author}

        **Sections:** 33

        **Lectures:** 164
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
<div class="footer">

<strong>{author}</strong>

<br>

{course_name}

<br>

33 Sections • 164 Lectures

</div>
""",
    unsafe_allow_html=True
)