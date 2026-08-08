from typing import TypeDict, Annotated, Literal
imprt operator
class GraphState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    action_approved: bool



def chatbot_node(state: GraphState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}


from langgraph.graph import StateGraph, START, END


workflow = StateGraph(GraphState)
workflow.add_node("chatbot", chatbot_node)


workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)

app=wokflow.compile()








def should_continute(state:GraphState):
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        return "tools"
    return END



workflow.add_conditional_edge("chatbot", should_continue, "tools")

for event in app.stream({messages: [HumanMessage(content="What is LangGraph?")]}):

    if event.type == "state_update":
        print("State updated:", event.state)
    elif event.type == "node_output":
        print("Node output:", event.output)
    elif event.type == "workflow_complete":
        print("Workflow completed.")











# Parallel Fan-Out: Run web search and DB lookup simultaneously
workflow.add_edge("planner", "web_search_node")
workflow.add_edge("planner", "db_lookup_node")

# Fan-In: Both parallel nodes stream their outputs into the aggregator node
workflow.add_edge("web_search_node", "aggregator_node")
workflow.add_edge("db_lookup_node", "aggregator_node")



from langgrpah.checkpoint import MemorySaver
memory = MemorySaver()
app = workflow.compile(checkpointer=memory,interrupt_before=["execute_transaction_node"])


config ={"configurable":{"Threaid_id": 12345, "User_ID": "user_001",session_id }}
app.invoke(None,config)