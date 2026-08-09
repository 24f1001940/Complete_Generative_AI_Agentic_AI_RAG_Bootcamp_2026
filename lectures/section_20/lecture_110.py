"""
Lecture 110: LangServe API deployment
"""

def main():
    try:
        from fastapi import FastAPI
        from langserve import add_routes
    except ImportError:
        print("Missing dependency: fastapi langserve")
        print("Install with: pip install fastapi langserve uvicorn")
        return

    from langchain_core.runnables import RunnableLambda

    app = FastAPI(title="LangServe Demo")

    chain = RunnableLambda(
        lambda x: {"answer": f"Demo answer for: {x.get('question', '')}"}
    )

    add_routes(app, chain, path="/demo")

    print("FastAPI + LangServe app created.")
    print("Run with:")
    print("uvicorn lecture_110:app --reload")


if __name__ == "__main__":
    main()
