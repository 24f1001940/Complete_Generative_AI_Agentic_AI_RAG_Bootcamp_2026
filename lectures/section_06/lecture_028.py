"""
Lecture 28: Abstraction
Author: MOHD SAQIB
"""
from abc import ABC, abstractmethod

class BaseRetriever(ABC):
    """Abstract interface for RAG document retrievers."""

    @abstractmethod
    def retrieve_documents(self, query: str, top_k: int = 3) -> list:
        pass

class VectorStoreRetriever(BaseRetriever):
    def retrieve_documents(self, query: str, top_k: int = 3) -> list:
        return [f"Doc #{i+1} relevant to '{query}'" for i in range(top_k)]

if __name__ == "__main__":
    retriever = VectorStoreRetriever()
    print(retriever.retrieve_documents("RAG Architecture", top_k=2))