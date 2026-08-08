import streamlit as st
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Simple GenAI App", page_icon="🤖")

st.title("Simple GenAI App Using Ollama")
st.write("Type your prompt below and generate a response from a local model.")

user_input = st.text_area("Enter your prompt here:")

if st.button("Generate Response"):
    if user_input.strip():
        try:
            llm = OllamaLLM(model="gemma4:12b")
            response = llm.invoke(user_input)
            st.subheader("Response")
            st.write(response)
        except Exception:
            # Fallback to calling local Ollama CLI directly
            try:
                import subprocess
                ollama_exe = r"C:\Users\mohd saqib\AppData\Local\Programs\Ollama\ollama.exe"
                cmd = [ollama_exe, "generate", "gemma4:12b", user_input]
                proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                if proc.returncode == 0:
                    st.subheader("Response (from ollama CLI)")
                    st.text(proc.stdout.strip())
                else:
                    st.error(f"Ollama CLI failed: {proc.stderr.strip()}")
            except Exception as e2:
                st.error(f"Generation failed: {e2}")
    else:
        st.warning("Please enter a prompt first.")