"""
Lecture 108: LLM prompt and output chain
"""

def main():
    try:
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser
        from langchain_core.runnables import RunnableLambda
    except ImportError:
        print("Missing dependency: langchain-core")
        print("Install with: pip install langchain-core")
        return

    prompt = ChatPromptTemplate.from_template(
        "Answer this question in one sentence: {question}"
    )

    # A local deterministic stand-in keeps this lecture runnable
    # without requiring an API key.
    fake_model = RunnableLambda(
        lambda value: f"Demo response for: {value['question']}"
    )

    parser = StrOutputParser()
    chain = prompt | fake_model | parser

    result = chain.invoke({"question": "What is generative AI?"})
    print(result)


if __name__ == "__main__":
    main()
