

from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import streamlit as st


# ============================================================
# CONFIG
# ============================================================

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "section_data" / "sections.json"
LECTURES_DIR = ROOT / "lectures"
PROJECTS_DIR = ROOT / "projects"
RESOURCES_DIR = ROOT / "resources"
SECTION_PDFS_DIR = RESOURCES_DIR / "section_pdfs"
EBOOKS_DIR = RESOURCES_DIR / "ebooks"

COURSE_NAME = "Complete Generative AI, Agentic AI & RAG Bootcamp"
AUTHOR = "MOHD SAQIB"
GITHUB_URL = "https://github.com/24f1001940/Complete_Generative_AI_Agentic_AI_RAG_Bootcamp_2026"


st.set_page_config(
    page_title=COURSE_NAME,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #06121f 0%, #0b1020 45%, #111827 100%);
            color: #f8fafc;
        }
        [data-testid="stHeader"] { display: none !important; }
        footer { display: none !important; }

        .hero {
            padding: 1.5rem 1.5rem 1rem 1.5rem;
            border-radius: 24px;
            background: rgba(15, 23, 42, 0.62);
            border: 1px solid rgba(148, 163, 184, 0.2);
            box-shadow: 0 20px 60px rgba(0,0,0,0.35);
            margin-bottom: 1rem;
        }
        .hero h1 {
            font-size: 3rem;
            line-height: 1.05;
            margin: 0;
            background: linear-gradient(90deg, #22d3ee, #8b5cf6, #f472b6);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .hero p {
            color: #cbd5e1;
            font-size: 1rem;
            margin-top: 0.75rem;
        }
        .card {
            padding: 1rem 1rem 0.9rem 1rem;
            border-radius: 18px;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(148, 163, 184, 0.18);
            box-shadow: 0 12px 30px rgba(0,0,0,0.2);
            margin-bottom: 0.9rem;
        }
        .muted {
            color: #94a3b8;
        }
        .small {
            font-size: 0.92rem;
        }

        .pill {
            display: inline-block;
            padding: 0.25rem 0.7rem;
            margin-right: 0.35rem;
            margin-bottom: 0.35rem;
            border-radius: 999px;
            background: rgba(59, 130, 246, 0.15);
            border: 1px solid rgba(59, 130, 246, 0.35);
            color: #dbeafe;
            font-size: 0.82rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# DATA HELPERS
# ============================================================

@st.cache_data(show_spinner=False)
def load_course_data() -> Dict[str, Any]:
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass

    # Minimal fallback if sections.json is absent.
    return {
        "course_name": COURSE_NAME,
        "author": AUTHOR,
        "github_url": GITHUB_URL,
        "sections": [],
    }


@st.cache_data(show_spinner=False)
def read_text_file(path_str: str) -> Optional[str]:
    path = Path(path_str)
    if not path.exists():
        return None
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return None


def get_lecture_file(section_number: int, lecture_number: int) -> Path:
    return LECTURES_DIR / f"section_{section_number:02d}" / f"lecture_{lecture_number:03d}.py"


def get_lecture_notes(section_number: int, lecture_number: int) -> Path:
    return LECTURES_DIR / f"section_{section_number:02d}" / f"lecture_{lecture_number:03d}.md"


def get_related_pdf_for_section(section_number: int) -> Optional[Path]:
    """
    Looks for any PDF inside resources/section_pdfs/Section_XX.
    Returns the first PDF found for that section.
    """
    candidates = []
    for folder_name in [
        f"Section_{section_number:02d}",
        f"section_{section_number:02d}",
        f"SECTION_{section_number:02d}",
    ]:
        folder = SECTION_PDFS_DIR / folder_name
        if folder.exists():
            candidates.extend(sorted(folder.rglob("*.pdf")))
    return candidates[0] if candidates else None


def discover_pdf_files() -> List[Path]:
    pdfs: List[Path] = []
    for folder in [SECTION_PDFS_DIR, EBOOKS_DIR]:
        if folder.exists():
            pdfs.extend(sorted(folder.rglob("*.pdf")))
    # de-duplicate while preserving order
    seen = set()
    unique = []
    for p in pdfs:
        key = str(p.resolve())
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


def group_pdfs_by_folder(pdf_paths: List[Path]) -> Dict[str, List[Path]]:
    grouped: Dict[str, List[Path]] = {}
    for p in pdf_paths:
        label = p.parent.name
        grouped.setdefault(label, []).append(p)
    return grouped


def embed_pdf(path: Path, height: int = 850) -> None:
    if not path.exists():
        st.warning("PDF file not found.")
        return

    try:
        pdf_bytes = path.read_bytes()

        # Check that the file is actually a PDF
        if not pdf_bytes.startswith(b"%PDF"):
            st.error("This file is not a valid PDF.")
            return

        st.pdf(pdf_bytes, height=height)

    except Exception as e:
        st.error(f"Unable to display PDF: {e}")


def render_stats(sections: List[Dict[str, Any]]) -> None:
    section_count = len(sections)
    lecture_count = sum(len(s.get("lectures", [])) for s in sections)
    project_count = len(list(PROJECTS_DIR.glob("project_*"))) if PROJECTS_DIR.exists() else 0
    pdf_count = len(discover_pdf_files())

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Sections", section_count or "33", "Curriculum")
    c2.metric("Lectures", lecture_count or "164", "Deep dives")
    c3.metric("Projects", project_count or "3", "Project folders")
    c4.metric("PDFs", pdf_count, "Resources")


def section_label(section: Dict[str, Any]) -> str:
    return f"Section {section['section_number']:02d} — {section['section_title']}"


def lecture_label(lecture: Dict[str, Any]) -> str:
    return f"Lecture {lecture['lecture_number']:03d}: {lecture['lecture_title']}"


# ============================================================
# LOAD DATA
# ============================================================

data = load_course_data()
sections = data.get("sections", [])
course_name = data.get("course_name", COURSE_NAME)
author = data.get("author", AUTHOR)
github_url = data.get("github_url", GITHUB_URL)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    f"""
    <div class="hero">
        <h1>{course_name}</h1>
        <p>
            Official course resource hub with lecture code, lecture notes, projects,
            and PDF study material in one place.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(f"## {author}")
    st.caption("Course Resource Hub")
    st.divider()

    navigation = st.radio(
        "Navigation",
        [
            "Home",
            "Section Explorer",
            "Lecture Search",
            "PDF Library",
            "Projects",
            "About Course",
        ],
    )

    st.divider()
    st.markdown("### Repository")
    st.link_button("Open GitHub ↗", github_url, use_container_width=True)

    st.divider()
    st.markdown("### Quick Info")
    st.caption(f"Lecture code: {LECTURES_DIR.name}/")
    st.caption(f"PDFs: {SECTION_PDFS_DIR.name}/ and {EBOOKS_DIR.name}/")
    st.caption("Main resource types: .py, .md, .pdf")


# ============================================================
# HOME
# ============================================================

if navigation == "Home":
    st.markdown("## Welcome to the Course Resource Hub 🚀")
    st.info(
        "Use Section Explorer for lecture code and notes, "
        "PDF Library for the PDF study material, and Projects for the capstone work."
    )

    render_stats(sections)

    st.markdown("### Learning Journey")
    journey = [
        "Python", "NLP", "Deep Learning", "Transformers",
        "Generative AI", "Prompting", "Hugging Face", "LangChain",
        "RAG", "Agents", "MCP", "Cloud Deployment"
    ]
    cols = st.columns(4)
    for i, item in enumerate(journey):
        cols[i % 4].write(f"• {item}")

    st.markdown("### What is inside")
    st.markdown(
        """
        <div class="card">
        <span class="pill">Lecture code</span>
        <span class="pill">Lecture notes</span>
        <span class="pill">PDF resources</span>
        <span class="pill">Projects</span>
        <span class="pill">Capstone material</span>
        <p class="small muted" style="margin-top: 0.8rem;">
            Everything is organized for browsing, reading, and downloading from the same app.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if sections:
        with st.expander("Preview curriculum structure", expanded=False):
            for s in sections[:5]:
                st.write(f"{s.get('section_number', '')}. {s.get('section_title', '')}")


# ============================================================
# SECTION EXPLORER
# ============================================================

elif navigation == "Section Explorer":
    st.header("Section Explorer")

    if not sections:
        st.warning("No curriculum data found. Please check `section_data/sections.json`.")
    else:
        sec_labels = [section_label(s) for s in sections]
        selected_sec_label = st.selectbox("Select a section", sec_labels)
        selected_section = sections[sec_labels.index(selected_sec_label)]

        st.subheader(selected_sec_label)
        if selected_section.get("summary"):
            st.info(selected_section["summary"])

        lecture_options = selected_section.get("lectures", [])
        if not lecture_options:
            st.warning("No lectures found in this section.")
        else:
            lec_labels = [lecture_label(lec) for lec in lecture_options]
            selected_lec_label = st.selectbox("Select a lecture", lec_labels)
            selected_lecture = lecture_options[lec_labels.index(selected_lec_label)]

            sec_num = selected_section["section_number"]
            lec_num = selected_lecture["lecture_number"]

            code_path = get_lecture_file(sec_num, lec_num)
            notes_path = get_lecture_notes(sec_num, lec_num)
            pdf_path = get_related_pdf_for_section(sec_num)

            tab_code, tab_notes, tab_pdf = st.tabs(["Code (.py)", "Notes (.md)", "Section PDF"])

            with tab_code:
                code_content = read_text_file(str(code_path))
                if code_content:
                    st.code(code_content, language="python")
                    st.download_button(
                        "Download Python file",
                        data=code_content.encode("utf-8"),
                        file_name=code_path.name,
                        mime="text/x-python",
                    )
                else:
                    st.warning(f"Code file not found: {code_path}")

            with tab_notes:
                notes_content = read_text_file(str(notes_path))
                if notes_content:
                    st.markdown(notes_content)
                    st.download_button(
                        "Download Markdown notes",
                        data=notes_content.encode("utf-8"),
                        file_name=notes_path.name,
                        mime="text/markdown",
                    )
                else:
                    st.warning(f"Notes file not found: {notes_path}")

            with tab_pdf:
                if pdf_path:
                    st.success(f"PDF found: {pdf_path.name}")
                    st.download_button(
                        "Download section PDF",
                        data=pdf_path.read_bytes(),
                        file_name=pdf_path.name,
                        mime="application/pdf",
                    )
                    embed_pdf(pdf_path)
                else:
                    st.info("No PDF found for this section yet.")

        st.divider()
        st.markdown("### Section summary")
        st.write(
            "This page links the selected lecture to its Python file, Markdown notes, "
            "and any matching section PDF."
        )


# ============================================================
# LECTURE SEARCH
# ============================================================

elif navigation == "Lecture Search":
    st.header("Lecture Search")

    if not sections:
        st.warning("No curriculum data found.")
    else:
        query = st.text_input("Search by lecture title or section title", placeholder="e.g. RAG, Streamlit, Transformers")
        results = []

        if query.strip():
            q = query.strip().lower()
            for sec in sections:
                sec_title = sec.get("section_title", "")
                if q in sec_title.lower():
                    results.append({
                        "section": sec,
                        "lecture": None,
                        "match_type": "section",
                    })
                for lec in sec.get("lectures", []):
                    if q in lec.get("lecture_title", "").lower():
                        results.append({
                            "section": sec,
                            "lecture": lec,
                            "match_type": "lecture",
                        })

        if query.strip() and not results:
            st.warning("No matches found.")
        elif query.strip():
            st.success(f"Found {len(results)} match(es).")
            for item in results:
                sec = item["section"]
                lec = item["lecture"]

                if lec is None:
                    st.markdown(f"**{section_label(sec)}**")
                else:
                    st.markdown(
                        f"**{section_label(sec)}**  \n"
                        f"{lecture_label(lec)}"
                    )

                cols = st.columns([1, 1, 1, 2])
                sec_num = sec["section_number"]
                if lec is not None:
                    lec_num = lec["lecture_number"]
                    code_path = get_lecture_file(sec_num, lec_num)
                    notes_path = get_lecture_notes(sec_num, lec_num)

                    with cols[0]:
                        if code_path.exists():
                            st.download_button(
                                "Py",
                                data=code_path.read_bytes(),
                                file_name=code_path.name,
                                mime="text/x-python",
                                key=f"py_{sec_num}_{lec_num}",
                            )
                    with cols[1]:
                        if notes_path.exists():
                            st.download_button(
                                "Md",
                                data=notes_path.read_bytes(),
                                file_name=notes_path.name,
                                mime="text/markdown",
                                key=f"md_{sec_num}_{lec_num}",
                            )
                    with cols[2]:
                        pdf_path = get_related_pdf_for_section(sec_num)
                        if pdf_path:
                            st.download_button(
                                "PDF",
                                data=pdf_path.read_bytes(),
                                file_name=pdf_path.name,
                                mime="application/pdf",
                                key=f"pdf_{sec_num}_{lec_num}",
                            )
                    with cols[3]:
                        st.caption("Open the matching section from Section Explorer for full view.")
                else:
                    with cols[3]:
                        st.caption("This is a section-level match. Open it in Section Explorer.")
                st.divider()
        else:
            st.info("Type a topic to search across lecture and section titles.")


# ============================================================
# PDF LIBRARY
# ============================================================

elif navigation == "PDF Library":
    st.header("PDF Library")

    pdf_files = discover_pdf_files()
    if not pdf_files:
        st.warning("No PDF files found in `resources/section_pdfs` or `resources/ebooks`.")
    else:
        st.info(
            "These PDFs are discovered from your resources folders and shown directly inside Streamlit."
        )

        grouped = group_pdfs_by_folder(pdf_files)
        group_names = sorted(grouped.keys())
        selected_group = st.selectbox("Choose a folder", group_names)

        selected_pdfs = grouped[selected_group]
        pdf_labels = [p.name for p in selected_pdfs]
        selected_pdf_label = st.selectbox("Choose a PDF", pdf_labels)

        selected_pdf = selected_pdfs[pdf_labels.index(selected_pdf_label)]

        st.subheader(selected_pdf.name)
        st.caption(str(selected_pdf))

        col1, col2 = st.columns([1, 1])
        with col1:
            st.download_button(
                "Download PDF",
                data=selected_pdf.read_bytes(),
                file_name=selected_pdf.name,
                mime="application/pdf",
                use_container_width=True,
            )
        with col2:
            st.write(f"File size: {selected_pdf.stat().st_size / (1024 * 1024):.2f} MB")

        embed_pdf(selected_pdf)

        st.divider()
        st.markdown("### All discovered PDFs")
        for pdf in pdf_files:
            st.write(f"• {pdf.relative_to(ROOT)}")


# ============================================================
# PROJECTS
# ============================================================

elif navigation == "Projects":
    st.header("Projects")

    if not PROJECTS_DIR.exists():
        st.warning("Projects folder not found.")
    else:
        project_dirs = sorted([p for p in PROJECTS_DIR.iterdir() if p.is_dir()])

        if not project_dirs:
            st.warning("No project folders found.")
        else:
            for project_dir in project_dirs:
                with st.expander(project_dir.name.replace("_", " ").title(), expanded=False):
                    files = sorted([p for p in project_dir.rglob("*") if p.is_file()])
                    if not files:
                        st.info("No files inside this project yet.")
                    else:
                        for file_path in files:
                            cols = st.columns([5, 1])
                            with cols[0]:
                                st.write(file_path.relative_to(ROOT))
                            with cols[1]:
                                mime = "text/plain"
                                if file_path.suffix.lower() == ".py":
                                    mime = "text/x-python"
                                elif file_path.suffix.lower() == ".md":
                                    mime = "text/markdown"
                                elif file_path.suffix.lower() == ".pdf":
                                    mime = "application/pdf"
                                st.download_button(
                                    "Download",
                                    data=file_path.read_bytes(),
                                    file_name=file_path.name,
                                    mime=mime,
                                    key=f"download_{project_dir.name}_{file_path.name}",
                                )


# ============================================================
# ABOUT
# ============================================================

elif navigation == "About Course":
    st.header("About Course")

    st.markdown(
        f"""
        <div class="card">
        <p><b>Course:</b> {course_name}</p>
        <p><b>Author:</b> {author}</p>
        <p><b>GitHub:</b> {github_url}</p>
        <p><b>Repository root:</b> {ROOT}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Included resources")
    st.write("• Lecture code in `lectures/`")
    st.write("• Section notes in `lectures/`")
    st.write("• PDFs in `resources/section_pdfs/` and `resources/ebooks/`")
    st.write("• Projects in `projects/`")

    if sections:
        st.markdown("### Curriculum snapshot")
        snapshot = {
            "sections": len(sections),
            "lectures": sum(len(s.get('lectures', [])) for s in sections),
        }
        st.json(snapshot)

    st.caption("This app is designed to keep your course material organized in one place.")
