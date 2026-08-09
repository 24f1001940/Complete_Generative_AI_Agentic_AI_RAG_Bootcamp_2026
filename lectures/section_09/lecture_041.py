"""
Lecture 41: NumPy Fundamentals for AI and Data Science
Author: MOHD SAQIB
"""
import numpy as np

def compute_cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """Computes cosine similarity between two vector embeddings."""
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot_product / (norm_a * norm_b))

if __name__ == "__main__":
    # Simulate high-dimensional embedding vectors
    np.random.seed(42)
    embedding_dim = 8
    
    query_vector = np.random.randn(embedding_dim)
    doc_vector_1 = query_vector + np.random.normal(0, 0.1, embedding_dim)
    doc_vector_2 = np.random.randn(embedding_dim)

    # Vectorized operations
    sim1 = compute_cosine_similarity(query_vector, doc_vector_1)
    sim2 = compute_cosine_similarity(query_vector, doc_vector_2)

    print(f"Query Vector Shape: {query_vector.shape}")
    print(f"Similarity with Relevant Doc: {sim1:.4f}")
    print(f"Similarity with Random Doc:   {sim2:.4f}")

    # Matrix batch operations
    doc_matrix = np.vstack([doc_vector_1, doc_vector_2])
    batch_similarities = np.dot(doc_matrix, query_vector) / (
        np.linalg.norm(doc_matrix, axis=1) * np.linalg.norm(query_vector)
    )
    print(f"Batch Similarities Matrix Operation: {batch_similarities}")