"""
Lecture 157: Model Context Protocol (MCP): Architecture & Custom Tools
"""

def main():
    tool = {
        "name": "search_documents",
        "description": "Search a document collection.",
        "input_schema": {
            "query": "string",
            "limit": "integer",
        },
    }

    print("Example tool definition:")
    for key, value in tool.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
