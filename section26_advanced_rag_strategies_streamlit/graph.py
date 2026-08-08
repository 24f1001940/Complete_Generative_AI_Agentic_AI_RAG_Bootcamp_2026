from typing import TypedDict, Annotated, Literal
import operator
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

# 1. Define State Schema
class GraphState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    action_approved: bool

# 2. Define Mock Tool Function
def mock_search_tool(query: str) -> str:
    return f"Search result for '{query}': High-throughput LangGraph streaming verified."

# 3. Define Nodes
def chatbot_node(state: GraphState):
    # Replace ChatOpenAI with ChatGroq
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

    tools = [{
        "type": "function",
        "function": {
            "name": "mock_search_tool",
            "description": "Searches real-time documentation.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"]
            }
        }
    }]
    llm_with_tools = llm.bind_tools(tools)
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

def tool_execution_node(state: GraphState):
    last_message = state["messages"][-1]
    tool_outputs = []
    
    for tool_call in last_message.tool_calls:
        if tool_call["name"] == "mock_search_tool":
            result = mock_search_tool(tool_call["args"]["query"])
            tool_outputs.append(
                ToolMessage(content=result, tool_call_id=tool_call["id"])
            )
            
    return {"messages": tool_outputs}

# 4. Router Function
def route_next(state: GraphState) -> Literal["tools", "human_approval", END]:
    last_message = state["messages"][-1]
    
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        # Route to tool execution if a tool call was requested
        return "tools"
    return END

# 5. Build Graph
def build_agent_graph():
    workflow = StateGraph(GraphState)
    
    workflow.add_node("chatbot", chatbot_node)
    workflow.add_node("tools", tool_execution_node)
    
    workflow.add_edge(START, "chatbot")
    workflow.add_conditional_edges(
        "chatbot",
        route_next,
        {
            "tools": "tools",
            END: END
        }
    )
    workflow.add_edge("tools", "chatbot")
    
    # In-memory checkpointing for state persistence
    memory = MemorySaver()
    return workflow.compile(checkpointer=memory)