from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from graph import build_agent_graph

st.set_page_config(page_title="Section 27: LangGraph Agentic Studio", layout="wide")

# Initialize Session State
if "graph" not in st.session_state:
    st.session_state.graph = build_agent_graph()
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "session_streamlit_demo"
if "messages" not in st.session_state:
    st.session_state.messages = []

config = {"configurable": {"thread_id": st.session_state.thread_id}}

# UI Sidebar - State Inspection
with st.sidebar:
    st.title("🔍 LangGraph State Inspector")
    st.markdown("---")
    
    # Fetch current graph state from checkpointer
    current_state = st.session_state.graph.get_state(config)
    
    st.subheader("Thread ID")
    st.code(st.session_state.thread_id)
    
    st.subheader("Next Node to Execute")
    st.info(current_state.next if current_state.next else "Graph Idle (END)")
    
    st.subheader("Raw State Payload")
    st.json(current_state.values if current_state.values else {})

# Main Chat Interface
st.title("🤖 LangGraph Agentic Assistant (Section 27)")
st.caption("Stateful Chatbot with Dynamic Tool Routing, Token Streaming & State Checkpointing")

# Display Chat History
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage) and msg.content:
        with st.chat_message("assistant"):
            st.write(msg.content)
    elif isinstance(msg, ToolMessage):
        with st.status(f"Tool Output ({msg.name if hasattr(msg, 'name') else 'Tool'})"):
            st.write(msg.content)

# Process User Input
if prompt := st.chat_input("Ask a question or request a search..."):
    # Append User Message to State
    user_msg = HumanMessage(content=prompt)
    st.session_state.messages.append(user_msg)
    
    with st.chat_message("user"):
        st.write(prompt)
        
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream events live from the compiled StateGraph
        inputs = {"messages": [user_msg], "action_approved": True}
        for event in st.session_state.graph.stream(inputs, config=config, stream_mode="values"):
            if "messages" in event:
                latest_msg = event["messages"][-1]
                if isinstance(latest_msg, AIMessage) and latest_msg.content:
                    full_response = latest_msg.content
                    message_placeholder.markdown(full_response + "▌")
                    
        message_placeholder.markdown(full_response)
        
    st.rerun()