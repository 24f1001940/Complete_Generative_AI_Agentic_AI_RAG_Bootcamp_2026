import json
from pathlib import Path

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Complete Generative AI, Agentic AI & RAG Bootcamp",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PATHS
# ============================================================

ROOT_DIR = Path(__file__).resolve().parent
SECTION_DATA_FILE = ROOT_DIR / "section_data" / "sections.json"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main application */

    .main {
        padding-top: 1rem;
    }

    /* Course title */

    .course-title {
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
        color: #172033;
    }

    .course-subtitle {
        font-size: 1rem;
        color: #64748b;
        margin-bottom: 2rem;
    }

    /* Section card */

    .section-card {
        padding: 1.4rem;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        background: linear-gradient(
            135deg,
            #ffffff 0%,
            #f8fbff 100%
        );
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.06);
        margin-bottom: 1.5rem;
    }

    .section-number {
        color: #2563eb;
        font-weight: 700;
        font-size: 0.95rem;
    }

    .section-title {
        color: #172033;
        font-size: 1.7rem;
        font-weight: 750;
        margin-top: 0.2rem;
    }

    .section-summary {
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
    }

    /* Lecture cards */

    .lecture-info {
        padding: 0.5rem 0;
    }

    .lecture-objective {
        color: #475569;
        line-height: 1.6;
    }

    /* Sidebar */

    [data-testid="stSidebar"] {
        border-right: 1px solid #e2e8f0;
    }

    .sidebar-brand {
        text-align: center;
        padding: 0.8rem 0 1.2rem 0;
    }

    .sidebar-brand-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #172033;
    }

    .sidebar-brand-author {
        color: #2563eb;
        font-weight: 700;
        margin-top: 0.2rem;
    }

    /* Footer */

    .course-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: rgba(15, 23, 42, 0.97);
        color: white;
        text-align: center;
        padding: 9px;
        font-size: 13px;
        z-index: 999999;
    }

    /* Hide Streamlit menu */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LOAD COURSE DATA
# ============================================================

@st.cache_data
def load_course_data():

    if not SECTION_DATA_FILE.exists():
        return {
            "course_name": "Complete Generative AI, Agentic AI & RAG Bootcamp",
            "author": "MOHD SAQIB",
            "sections": [],
        }

    with open(SECTION_DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


course = load_course_data()

sections = course.get("sections", [])

course_name = course.get(
    "course_name",
    "Complete Generative AI, Agentic AI & RAG Bootcamp"
)

author = course.get(
    "author",
    "MOHD SAQIB"
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    f"""
    <div class="course-title">
        {course_name}
    </div>

    <div class="course-subtitle">
        Complete course code, lecture resources, notes and project hub
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        f"""
        <div class="sidebar-brand">

            <div class="sidebar-brand-title">
                {course_name}
            </div>

            <div class="sidebar-brand-author">
                {author}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.subheader("Course Navigation")

    if sections:

        section_labels = [
            f"Section {section['section_number']}: "
            f"{section['section_title']}"
            for section in sections
        ]

        selected_label = st.radio(
            "Select a section",
            section_labels,
            index=0,
        )

        selected_index = section_labels.index(selected_label)

        current_section = sections[selected_index]

    else:

        current_section = None

        st.warning(
            "No section data found. "
            "Add sections to section_data/sections.json."
        )

    st.divider()

    st.caption("Course Author")
    st.markdown(f"**{author}**")

    st.caption("Course")
    st.markdown(
        "*Complete Generative AI, Agentic AI & RAG Bootcamp*"
    )


# ============================================================
# MAIN CONTENT
# ============================================================

if current_section:

    section_number = current_section["section_number"]
    section_title = current_section["section_title"]
    section_summary = current_section.get("summary", "")

    st.markdown(
        f"""
        <div class="section-card">

            <div class="section-number">
                SECTION {section_number}
            </div>

            <div class="section-title">
                {section_title}
            </div>

            <div class="section-summary">
                {section_summary}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # ========================================================
    # QUICK STATISTICS
    # ========================================================

    lectures = current_section.get("lectures", [])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Lectures",
            len(lectures)
        )

    with col2:
        st.metric(
            "Section",
            section_number
        )

    with col3:
        st.metric(
            "Course",
            "GenAI + RAG"
        )


    st.divider()


    # ========================================================
    # LECTURES
    # ========================================================

    st.subheader("Lecture Resources")

    if not lectures:

        st.info(
            "Lecture resources for this section "
            "will be added soon."
        )

    else:

        for lecture in lectures:

            lecture_number = lecture.get(
                "lecture_number",
                ""
            )

            lecture_title = lecture.get(
                "lecture_title",
                "Untitled Lecture"
            )

            objective = lecture.get(
                "objective",
                "Lecture objective will be added."
            )

            resources = lecture.get(
                "resources",
                []
            )

            code = lecture.get(
                "code",
                ""
            )

            with st.expander(
                f"Lecture {lecture_number}: {lecture_title}",
                expanded=False,
            ):

                st.markdown(
                    "### Learning Objective"
                )

                st.markdown(
                    f"""
                    <div class="lecture-objective">
                        {objective}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


                st.markdown(
                    "### Resources"
                )

                if resources:

                    for resource in resources:

                        st.markdown(
                            f"- `{resource}`"
                        )

                else:

                    st.caption(
                        "No additional resources added yet."
                    )


                if code:

                    st.markdown(
                        "### Code"
                    )

                    st.code(
                        code,
                        language="python"
                    )


# ============================================================
# COURSE INFORMATION
# ============================================================

st.divider()

st.subheader("About This Repository")

info_col1, info_col2 = st.columns(2)

with info_col1:

    st.markdown(
        """
        This repository is the official code and
        resource companion for the course.

        Students can use it to access:

        - Lecture code
        - Section resources
        - Notes
        - Diagrams
        - Project files
        - Additional learning materials
        """
    )

with info_col2:

    st.markdown(
        """
        ### Learning Workflow

        **Watch → Read → Code → Practice → Build**

        Each section will gradually connect concepts
        into practical Generative AI, RAG and Agentic
        AI applications.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
    <div class="course-footer">
        {author}
        &nbsp; • &nbsp;
        {course_name}
    </div>
    """,
    unsafe_allow_html=True,
)