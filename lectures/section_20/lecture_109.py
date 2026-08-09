"""
Lecture 109: LCEL basics
"""

def main():
    try:
        from langchain_core.runnables import RunnableLambda
    except ImportError:
        print("Missing dependency: langchain-core")
        print("Install with: pip install langchain-core")
        return

    clean = RunnableLambda(lambda x: x.strip())
    upper = RunnableLambda(lambda x: x.upper())

    chain = clean | upper

    result = chain.invoke("  hello from LCEL  ")

    print("Input : '  hello from LCEL  '")
    print("Output:", result)


if __name__ == "__main__":
    main()
