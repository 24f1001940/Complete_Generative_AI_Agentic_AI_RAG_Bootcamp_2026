"""
Lecture 98: Document Loaders & Text Splitting
"""

def main():
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter
    except ImportError:
        print("Missing dependency: langchain-text-splitters")
        print("Install with: pip install langchain-text-splitters")
        return

    text = """
    LangChain helps developers build applications around language models.
    Documents often need to be divided into smaller chunks before retrieval.
    Chunking helps retrieval systems work with manageable pieces of content.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=80,
        chunk_overlap=20,
    )

    chunks = splitter.split_text(text)

    for index, chunk in enumerate(chunks, 1):
        print(f"\nChunk {index}:")
        print(chunk)


if __name__ == "__main__":
    main()
