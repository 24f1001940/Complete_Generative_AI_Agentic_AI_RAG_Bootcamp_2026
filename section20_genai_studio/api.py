from fastapi import FastAPI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langserve import add_routes

app = FastAPI(title="Section 20 GenAI Studio API", version="1.0")

prompt = PromptTemplate.from_template(
    "You are a helpful AI tutor. Explain {topic} in simple words."
)
llm = OllamaLLM(model="llama3.2:3b", num_ctx=2048)
chain = prompt | llm

add_routes(app, chain, path="/explain")
