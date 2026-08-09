"""
Lecture 26: Polymorphism
Author: MOHD SAQIB
"""

class CalculatorTool:
    def execute(self, query: str) -> str:
        return f"[Calculator] Executed math expression: {query}"

class SearchTool:
    def execute(self, query: str) -> str:
        return f"[WebSearch] Fetched real-time results for: {query}"

def process_agent_action(tool, query: str):
    # Polymorphic execution: standard call regardless of underlying class type
    return tool.execute(query)

if __name__ == "__main__":
    tools = [CalculatorTool(), SearchTool()]
    for tool in tools:
        print(process_agent_action(tool, "2 + 2"))