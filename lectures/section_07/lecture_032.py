"""
Lecture 32: Iterators
Author: MOHD SAQIB
"""

class DocumentBatchIterator:
    """Custom iterator to traverse documents in controlled batch sizes."""

    def __init__(self, documents: list[str], batch_size: int = 2):
        self.documents = documents
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> list[str]:
        if self.index >= len(self.documents):
            raise StopIteration
        
        batch = self.documents[self.index : self.index + self.batch_size]
        self.index += self.batch_size
        return batch

if __name__ == "__main__":
    docs = [f"Document_{i}.txt" for i in range(1, 6)]
    batch_iterator = DocumentBatchIterator(docs, batch_size=2)

    for batch in batch_iterator:
        print("Processing Batch:", batch)