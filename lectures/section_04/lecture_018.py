"""
Lecture 18: Writing Reusable Python Code
Author: MOHD SAQIB
"""

class TextCleaner:
    """Reusable utility class for pre-processing raw prompt inputs."""

    @staticmethod
    def sanitize(text: str) -> str:
        if not text:
            return ""
        return text.strip().replace("\n", " ").replace("  ", " ")

    @staticmethod
    def truncate(text: str, max_chars: int = 100) -> str:
        clean = TextCleaner.sanitize(text)
        return clean[:max_chars] + ("..." if len(clean) > max_chars else "")

if __name__ == "__main__":
    raw_input = "   Hello Generative AI World! \n\n This is a test prompt.   "
    clean_text = TextCleaner.sanitize(raw_input)
    print("Cleaned Text:", clean_text)