"""
Lecture 139: Multimodal RAG, Contextual Memory & Next-Gen Patterns
"""

from pathlib import Path


def main():
    sample_items = [
        {"type": "text", "content": "A document about AI"},
        {"type": "image", "content": "diagram.png"},
        {"type": "table", "content": "sales.csv"},
    ]

    print("Multimodal knowledge items:")
    for item in sample_items:
        print(f"{item['type']}: {item['content']}")

    memory_file = Path("context_memory.txt")
    memory_file.write_text(
        "User prefers concise technical explanations.",
        encoding="utf-8",
    )

    print("
Stored contextual memory:")
    print(memory_file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
