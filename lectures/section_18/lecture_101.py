"""
Lecture 101: Building Your First LangChain App
"""

def main():
    try:
        from langchain_core.prompts import ChatPromptTemplate
    except ImportError:
        print("Missing dependency: langchain-core")
        print("Install with: pip install langchain-core")
        return

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} to a beginner."
    )

    formatted = prompt.invoke({
        "topic": "Retrieval Augmented Generation"
    })

    print(formatted)


if __name__ == "__main__":
    main()
