from pathlib import Path
from pypdf import PdfReader, PdfWriter


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(
    r"C:\Users\mohd saqib\OneDrive\Desktop\new gen ai course july 16 startijng\notes\notes all page from lec1 to lec 164\section_pdfs"
)

OUTPUT_FILE = BASE_DIR / "Complete_Generative_AI_Master_Notes.pdf"


# ============================================================
# FIND SECTION PDFs
# ============================================================

section_pdfs = []

for section_number in range(1, 34):

    section_folder = BASE_DIR / f"Section_{section_number:02d}"

    if not section_folder.exists():
        print(
            f"[ERROR] Missing folder: {section_folder.name}"
        )
        continue

    # Find PDFs directly inside the section folder
    pdfs = sorted(
        section_folder.glob("*.pdf"),
        key=lambda p: p.name.lower()
    )

    if not pdfs:
        print(
            f"[ERROR] No PDF found in {section_folder.name}"
        )
        continue

    if len(pdfs) > 1:
        print(
            f"[WARNING] Multiple PDFs found in "
            f"{section_folder.name}"
        )

    # Use the first PDF found
    pdf = pdfs[0]

    section_pdfs.append(
        (section_number, pdf)
    )


# ============================================================
# DISPLAY ORDER
# ============================================================

print()
print("=" * 70)
print("PDFs TO BE MERGED")
print("=" * 70)

for section_number, pdf in section_pdfs:

    print(
        f"Section {section_number:02d} "
        f"-> {pdf.name}"
    )


# ============================================================
# CHECK THAT ALL 33 SECTIONS EXIST
# ============================================================

found_sections = {
    section_number
    for section_number, _ in section_pdfs
}

missing_sections = [
    number
    for number in range(1, 34)
    if number not in found_sections
]

if missing_sections:

    print()
    print("=" * 70)
    print("ERROR: SOME SECTIONS ARE MISSING")
    print("=" * 70)

    for number in missing_sections:
        print(
            f"Section {number:02d}"
        )

    print()
    print("Merge cancelled.")
    raise SystemExit(1)


# ============================================================
# MERGE
# ============================================================

writer = PdfWriter()

total_pages = 0

print()
print("=" * 70)
print("MERGING PDFs")
print("=" * 70)

for section_number, pdf_path in section_pdfs:

    print(
        f"\n[{section_number:02d}/33] "
        f"Adding {pdf_path.name}"
    )

    reader = PdfReader(
        str(pdf_path)
    )

    page_count = len(reader.pages)

    print(
        f"       Pages: {page_count}"
    )

    for page in reader.pages:
        writer.add_page(page)

    total_pages += page_count


# ============================================================
# WRITE MASTER PDF
# ============================================================

print()
print("=" * 70)
print("CREATING MASTER PDF")
print("=" * 70)

with open(
    OUTPUT_FILE,
    "wb"
) as output:

    writer.write(output)


# ============================================================
# FINAL VALIDATION
# ============================================================

print()
print("=" * 70)
print("MASTER PDF CREATED")
print("=" * 70)

print()
print("File:")
print(OUTPUT_FILE)

print()
print("Total sections:")
print(len(section_pdfs))

print()
print("Total pages:")
print(total_pages)

print()
print(
    f"File size: "
    f"{OUTPUT_FILE.stat().st_size / (1024 * 1024):.2f} MB"
)

print()
print("=" * 70)
print("DONE")
print("=" * 70)