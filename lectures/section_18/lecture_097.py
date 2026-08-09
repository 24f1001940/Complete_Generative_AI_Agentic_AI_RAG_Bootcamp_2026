"""
Lecture 97: LangChain Core Building Blocks & Output Parsers
"""

def main():
    try:
        from langchain_core.output_parsers import StrOutputParser
    except ImportError:
        print("Missing dependency: langchain-core")
        print("Install with: pip install langchain-core")
        return

    parser = StrOutputParser()
    result = parser.parse("Hello from LangChain")

    print("Parsed output:")
    print(result)


if __name__ == "__main__":
    main()
