# from pathlib import Path
# import re
# import subprocess
# import sys
# import tempfile
# import shutil

# import img2pdf

# # Update this to your real folder
# INPUT_DIR = Path(r"C:\Users\mohd saqib\OneDrive\Desktop\new gen ai course july 16 startijng\notes\notes all page from lec1 to lec 164")
# OUTPUT_DIR = Path(r"C:\Users\mohd saqib\OneDrive\Desktop\section_pdfs")

# # Section name + lecture range
# SECTION_RANGES = {
#     1:  ("Course Onboarding & Enterprise Environment Setup", 1, 6),
#     2:  ("Python Development Environment Setup", 7, 12),
#     3:  ("Python Core Fundamentals", 13, 14),
#     4:  ("Python Functions and Modular Programming", 15, 18),
#     5:  ("File Handling and Exception Handling", 19, 22),
#     6:  ("Object-Oriented Programming", 23, 31),
#     7:  ("Iterators, Generators, Closures, and Decorators", 32, 37),
#     8:  ("Production Python: Logging & Pydantic", 38, 40),
#     9:  ("Data Analysis with NumPy, Pandas & Matplotlib", 41, 44),
#     10: ("Building AI Apps with Streamlit", 45, 49),
#     11: ("NLP Foundations", 50, 59),
#     12: ("Classical NLP Features", 60, 66),
#     13: ("Deep Learning for NLP", 67, 74),
#     14: ("Transformers", 75, 79),
#     15: ("Generative AI Fundamentals", 80, 84),
#     16: ("Prompt Engineering", 85, 90),
#     17: ("Hugging Face Ecosystem", 91, 95),
#     18: ("LangChain Foundations", 96, 101),
#     19: ("Embeddings with Vector Search", 102, 106),
#     20: ("First GenAI Applications", 107, 114),
#     21: ("Open-Source LLM Workflows", 115, 120),
#     22: ("Structured Outputs and Tool Use", 121, 124),
#     23: ("Production GenAI: Middleware, Observability & Deployment", 125, 128),
#     24: ("Core GenAI Applications & Tool-Driven Assistants", 129, 132),
#     25: ("RAG Infrastructure: Ingestion, Vector Stores & Retrieval", 133, 136),
#     26: ("Advanced RAG Strategies & Evaluation", 137, 140),
#     27: ("LangGraph & Agentic Workflow Patterns", 141, 144),
#     28: ("Agentic RAG & Multi-Agent Systems", 145, 148),
#     29: ("Knowledge Graphs & Graph RAG", 149, 151),
#     30: ("Fine-Tuning & System Optimization", 152, 154),
#     31: ("Claude Ecosystem, Deep Agents & MCP", 155, 158),
#     32: ("Enterprise Capstone Projects — Building & Deploying Real-World AI Apps", 159, 161),
#     33: ("Enterprise Cloud & Multi-Agent Systems", 162, 164),
# }

# lecture_re = re.compile(r"^lec(\d+)(?:-(\d+))?\.(png|jpg|jpeg|webp)$", re.IGNORECASE)

# def parse_lecture_file(path: Path):
#     m = lecture_re.match(path.name)
#     if not m:
#         return None
#     lecture_no = int(m.group(1))
#     part_no = int(m.group(2)) if m.group(2) else 0
#     return lecture_no, part_no

# def collect_images_for_section(folder: Path, start_lecture: int, end_lecture: int):
#     items = []
#     for p in folder.iterdir():
#         if not p.is_file():
#             continue
#         parsed = parse_lecture_file(p)
#         if not parsed:
#             continue
#         lecture_no, part_no = parsed
#         if start_lecture <= lecture_no <= end_lecture:
#             items.append((lecture_no, part_no, p))
#     items.sort(key=lambda x: (x[0], x[1], x[2].name.lower()))
#     return [p for _, _, p in items]

# def make_pdf_from_images(image_paths, pdf_path: Path):
#     if not image_paths:
#         raise RuntimeError("No images found for this section.")
#     pdf_path.parent.mkdir(parents=True, exist_ok=True)
#     with open(pdf_path, "wb") as f:
#         f.write(img2pdf.convert([str(p) for p in image_paths]))

# def ocr_pdf(input_pdf: Path, output_pdf: Path):
#     # OCRmyPDF makes the PDF searchable while preserving the images
#     cmd = [
#         "ocrmypdf",
#         "--force-ocr",
#         "--deskew",
#         "--rotate-pages",
#         "--clean",
#         "--optimize", "1",
#         "--output-type", "pdf",
#         str(input_pdf),
#         str(output_pdf),
#     ]
#     subprocess.run(cmd, check=True)

# def main():
#     if not INPUT_DIR.exists():
#         print(f"Input folder not found: {INPUT_DIR}")
#         sys.exit(1)

#     OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

#     for sec_no, (sec_title, start_lec, end_lec) in SECTION_RANGES.items():
#         section_folder = OUTPUT_DIR / f"Section_{sec_no:02d}"
#         section_folder.mkdir(parents=True, exist_ok=True)

#         images = collect_images_for_section(INPUT_DIR, start_lec, end_lec)
#         if not images:
#             print(f"[SKIP] Section {sec_no:02d} - no images found.")
#             continue

#         raw_pdf = section_folder / f"Section_{sec_no:02d}_{sec_title}.pdf"
#         ocr_pdf_path = section_folder / f"Section_{sec_no:02d}_{sec_title}_OCR.pdf"

#         print(f"[BUILD] Section {sec_no:02d}: {sec_title}")
#         print(f"        Lectures {start_lec} to {end_lec}")
#         print(f"        Images: {len(images)}")

#         make_pdf_from_images(images, raw_pdf)
#         ocr_pdf(raw_pdf, ocr_pdf_path)

#         # remove raw pdf if OCR PDF is created successfully
#         try:
#             raw_pdf.unlink()
#         except Exception:
#             pass

#         print(f"[DONE]  {ocr_pdf_path}")

# if __name__ == "__main__":
#     main()
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

import img2pdf


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_DIR = Path(
    r"C:\Users\mohd saqib\OneDrive\Desktop\new gen ai course july 16 startijng\notes\notes all page from lec1 to lec 164"
)

OUTPUT_DIR = INPUT_DIR / "section_pdfs"


# ============================================================
# EXACT COURSE CURRICULUM
# Source: user's 33-section / 164-lecture curriculum
# ============================================================

SECTIONS = {
    1: ("Course Onboarding & Enterprise Environment Setup", 1, 6),
    2: ("Python Development Environment Setup", 7, 12),
    3: ("Python Core Fundamentals", 13, 14),
    4: ("Python Functions and Modular Programming", 15, 18),
    5: ("File Handling and Exception Handling", 19, 22),
    6: ("Object-Oriented Programming", 23, 31),
    7: ("Iterators, Generators, Closures, and Decorators", 32, 37),
    8: ("Production Python - Logging & Pydantic", 38, 40),
    9: ("Data Analysis with NumPy, Pandas & Matplotlib", 41, 44),
    10: ("Building AI Apps with Streamlit", 45, 49),
    11: ("NLP Foundations", 50, 59),
    12: ("Classical NLP Features", 60, 66),
    13: ("Deep Learning for NLP", 67, 74),
    14: ("Transformers", 75, 79),
    15: ("Generative AI Fundamentals", 80, 84),
    16: ("Prompt Engineering", 85, 90),
    17: ("Hugging Face Ecosystem", 91, 95),
    18: ("LangChain Foundations", 96, 101),
    19: ("Embeddings with Vector Search", 102, 106),
    20: ("First GenAI Applications", 107, 114),
    21: ("Open-Source LLM Workflows", 115, 120),
    22: ("Structured Outputs and Tool Use", 121, 124),
    23: ("Production GenAI - Middleware, Observability & Deployment", 125, 128),
    24: ("Core GenAI Applications & Tool-Driven Assistants", 129, 132),
    25: ("RAG Infrastructure - Ingestion, Vector Stores & Retrieval", 133, 136),
    26: ("Advanced RAG Strategies & Evaluation", 137, 140),
    27: ("LangGraph & Agentic Workflow Patterns", 141, 144),
    28: ("Agentic RAG & Multi-Agent Systems", 145, 148),
    29: ("Knowledge Graphs & Graph RAG", 149, 151),
    30: ("Fine-Tuning & System Optimization", 152, 154),
    31: ("Claude Ecosystem, Deep Agents & MCP", 155, 158),
    32: ("Enterprise Capstone Projects - Building & Deploying Real-World AI Apps", 159, 161),
    33: ("Enterprise Cloud & Multi-Agent Systems", 162, 164),
}


# Supports:
# lec1.png
# lec13-1.png
# lec13-2.png
# lec20.png
# lec20-2.png
IMAGE_RE = re.compile(
    r"^lec(?P<lecture>\d+)(?:-(?P<part>\d+))?\.(?P<ext>png|jpg|jpeg|webp)$",
    re.IGNORECASE,
)


# ============================================================
# HELPERS
# ============================================================

def safe_filename(text: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "-", text).strip()


def parse_image(path: Path):
    match = IMAGE_RE.match(path.name)
    if not match:
        return None

    lecture = int(match.group("lecture"))
    part = int(match.group("part") or 0)

    return lecture, part


def collect_images(start_lecture: int, end_lecture: int):
    items = []

    for path in INPUT_DIR.iterdir():
        if not path.is_file():
            continue

        parsed = parse_image(path)
        if parsed is None:
            continue

        lecture, part = parsed

        if start_lecture <= lecture <= end_lecture:
            items.append((lecture, part, path))

    # Numeric lecture order, then numeric part order.
    items.sort(key=lambda x: (x[0], x[1], x[2].name.lower()))

    return items


def check_required_tools():
    print("\n" + "=" * 78)
    print("CHECKING OCR ENVIRONMENT")
    print("=" * 78)

    # Python modules
    try:
        import img2pdf as _img2pdf
        import ocrmypdf as _ocrmypdf
        import PIL as _pil
        import reportlab as _reportlab
        import pypdf as _pypdf
        print("[OK] Python libraries")
    except Exception as exc:
        print("[ERROR] Python libraries:", exc)
        print("Run:")
        print("py -m pip install --upgrade img2pdf ocrmypdf Pillow reportlab pypdf")
        sys.exit(1)

    # OCRmyPDF through the same Python interpreter.
    result = subprocess.run(
        [sys.executable, "-m", "ocrmypdf", "--version"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print("[OK] OCRmyPDF:", result.stdout.strip())
    else:
        print("[ERROR] OCRmyPDF cannot start.")
        print(result.stderr)
        sys.exit(1)

    # Tesseract
    tesseract = shutil.which("tesseract")

    if tesseract:
        print("[OK] Tesseract:", tesseract)
    else:
        print("[ERROR] Tesseract was not found in PATH.")
        print()
        print("Install Tesseract and add its installation folder to PATH.")
        print("Typical folder:")
        print(r"C:\Program Files\Tesseract-OCR")
        print()
        print("Then close and reopen PowerShell and run:")
        print("tesseract --version")
        sys.exit(1)

    # Ghostscript
    ghostscript = shutil.which("gswin64c")

    if ghostscript:
        print("[OK] Ghostscript:", ghostscript)
    else:
        print("[ERROR] Ghostscript was not found in PATH.")
        print()
        print("Install 64-bit Ghostscript and make sure its bin folder is in PATH.")
        print("Typical folder:")
        print(r"C:\Program Files\gs\<version>\bin")
        print()
        print("Then close and reopen PowerShell and run:")
        print("gswin64c --version")
        sys.exit(1)


def build_raw_pdf(image_paths: list[Path], raw_pdf: Path):
    raw_pdf.parent.mkdir(parents=True, exist_ok=True)

    with raw_pdf.open("wb") as output:
        output.write(
            img2pdf.convert([str(path) for path in image_paths])
        )


def run_ocr(raw_pdf: Path, final_pdf: Path):
    # Launch OCRmyPDF through the exact Python environment.
    # This avoids the previous WinError 2 caused by calling
    # "ocrmypdf" directly as a Windows executable.
    command = [
        sys.executable,
        "-m",
        "ocrmypdf",

        # Preserve the original infographic pages while adding OCR.
        "--force-ocr",

        # Helpful for page orientation / slight scan skew.
        "--rotate-pages",
        "--deskew",

        # Keep a good balance between size and quality.
        "--optimize",
        "1",

        "--output-type",
        "pdf",

        str(raw_pdf),
        str(final_pdf),
    ]

    print("\n[OCR] Starting OCRmyPDF...")
    subprocess.run(command, check=True)


def verify_pdf(pdf_path: Path, expected_pages: int):
    try:
        from pypdf import PdfReader

        reader = PdfReader(str(pdf_path))
        actual_pages = len(reader.pages)

        if actual_pages != expected_pages:
            print(
                f"[WARNING] Page count mismatch: "
                f"expected {expected_pages}, got {actual_pages}"
            )
            return False

        print(f"[OK] PDF verified: {actual_pages} pages")
        return True

    except Exception as exc:
        print("[WARNING] Could not validate PDF:", exc)
        return False


def check_ocr_text(pdf_path: Path):
    """
    Quick validation that the final PDF contains an OCR text layer.
    We don't require every page to contain text because a page can
    legitimately contain diagrams, code screenshots, or decorative
    elements.
    """
    try:
        from pypdf import PdfReader

        reader = PdfReader(str(pdf_path))

        pages_with_text = 0
        total_chars = 0

        for page in reader.pages:
            text = page.extract_text() or ""
            if text.strip():
                pages_with_text += 1
                total_chars += len(text)

        print(
            f"[OCR CHECK] {pages_with_text}/{len(reader.pages)} pages "
            f"contain extracted text; {total_chars:,} characters."
        )

        return pages_with_text > 0

    except Exception as exc:
        print("[WARNING] OCR text validation failed:", exc)
        return False


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 78)
    print("33-SECTION PDF + OCR BUILDER")
    print("=" * 78)

    print("\nInput folder:")
    print(INPUT_DIR)

    print("\nOutput folder:")
    print(OUTPUT_DIR)

    if not INPUT_DIR.exists():
        print("\n[ERROR] Input folder does not exist.")
        sys.exit(1)

    # Verify environment before processing anything.
    check_required_tools()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    successful = []
    failed = []
    warnings = []

    start_time = time.time()

    for section_number in range(1, 34):
        title, start_lecture, end_lecture = SECTIONS[section_number]

        print("\n")
        print("#" * 78)
        print(f"SECTION {section_number:02d}")
        print(title)
        print(f"Lectures {start_lecture} -> {end_lecture}")
        print("#" * 78)

        items = collect_images(start_lecture, end_lecture)

        if not items:
            print("[ERROR] No lecture images found.")
            failed.append(section_number)
            continue

        # ----------------------------------------------------
        # Detect missing lecture numbers.
        # ----------------------------------------------------
        found_lectures = sorted(set(item[0] for item in items))
        expected_lectures = list(range(start_lecture, end_lecture + 1))
        missing = [
            lecture
            for lecture in expected_lectures
            if lecture not in found_lectures
        ]

        if missing:
            message = (
                f"Section {section_number:02d}: "
                f"missing image files for lecture(s): {missing}"
            )
            print("[WARNING]", message)
            warnings.append(message)

        # ----------------------------------------------------
        # Display exact page order.
        # ----------------------------------------------------
        print(f"\nImages found: {len(items)}")
        print("Page order:")

        for index, (lecture, part, path) in enumerate(items, start=1):
            part_label = f"-{part}" if part else ""
            print(
                f"  {index:03d}. "
                f"Lecture {lecture}{part_label}: "
                f"{path.name}"
            )

        image_paths = [item[2] for item in items]

        section_dir = OUTPUT_DIR / f"Section_{section_number:02d}"
        section_dir.mkdir(parents=True, exist_ok=True)

        safe_title = safe_filename(title)

        raw_pdf = (
            section_dir
            / f"Section_{section_number:02d}_{safe_title}_RAW.pdf"
        )

        final_pdf = (
            section_dir
            / f"Section_{section_number:02d}_{safe_title}.pdf"
        )

        try:
            # ------------------------------------------------
            # Step 1: images -> PDF
            # ------------------------------------------------
            print("\n[1/3] Creating image PDF...")
            build_raw_pdf(image_paths, raw_pdf)

            print(
                f"[OK] Raw PDF: {raw_pdf.name}"
            )

            # ------------------------------------------------
            # Step 2: PDF -> searchable OCR PDF
            # ------------------------------------------------
            print("\n[2/3] Adding OCR text layer...")
            run_ocr(raw_pdf, final_pdf)

            if not final_pdf.exists():
                raise RuntimeError(
                    "OCRmyPDF finished but final PDF was not created."
                )

            # ------------------------------------------------
            # Step 3: validate
            # ------------------------------------------------
            print("\n[3/3] Validating final PDF...")

            verify_pdf(
                final_pdf,
                expected_pages=len(image_paths),
            )

            check_ocr_text(final_pdf)

            # Raw PDF is only temporary.
            try:
                raw_pdf.unlink()
            except OSError:
                pass

            size_mb = final_pdf.stat().st_size / (1024 * 1024)

            print("\n" + "-" * 78)
            print(f"[SUCCESS] Section {section_number:02d}")
            print(f"File: {final_pdf}")
            print(f"Size: {size_mb:.2f} MB")
            print("-" * 78)

            successful.append(section_number)

        except subprocess.CalledProcessError as exc:
            print(
                f"\n[FAILED] OCR process failed for Section "
                f"{section_number:02d}"
            )
            print("Exit code:", exc.returncode)

            failed.append(section_number)

            # Keep raw PDF so it can be inspected/reprocessed.
            print("Raw PDF kept at:")
            print(raw_pdf)

        except Exception as exc:
            print(
                f"\n[FAILED] Section {section_number:02d}: {exc}"
            )
            failed.append(section_number)

    elapsed = time.time() - start_time

    # ========================================================
    # FINAL REPORT
    # ========================================================

    print("\n\n")
    print("=" * 78)
    print("FINAL REPORT")
    print("=" * 78)

    print(f"Successful sections : {len(successful)}/33")
    print(f"Failed sections     : {len(failed)}/33")
    print(f"Warnings             : {len(warnings)}")
    print(f"Time elapsed         : {elapsed / 60:.1f} minutes")

    if successful:
        print("\nSuccessful:")
        print(
            ", ".join(f"Section {x:02d}" for x in successful)
        )

    if failed:
        print("\nFailed:")
        print(
            ", ".join(f"Section {x:02d}" for x in failed)
        )

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(" -", warning)

    print("\nOutput folder:")
    print(OUTPUT_DIR)

    print("\n" + "=" * 78)
    print("DONE")
    print("=" * 78)


if __name__ == "__main__":
    main()
