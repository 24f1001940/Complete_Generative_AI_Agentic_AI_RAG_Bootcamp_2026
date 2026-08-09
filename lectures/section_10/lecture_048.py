"""
Lecture 48: Displaying with ML/AI apps
"""
import streamlit as st
import time

def simulate_llm_response(prompt: str) -> str:
    """Mock function to simulate an AI generating text."""
    time.sleep(1.5) # Simulate network latency
    return f"This is an AI-generated response to your prompt: '{prompt}'."

def main():
    st.header("AI Chat Interface")
    st.write("Using Streamlit's native chat elements to build LLM interfaces.")

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    prompt = st.chat_input("Send a message to the AI...")
    if prompt:
        # 1. Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 2. Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # 3. Display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = simulate_llm_response(prompt)
                st.markdown(response)
        
        # 4. Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()