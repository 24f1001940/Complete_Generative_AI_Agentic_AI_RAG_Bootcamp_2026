"""
Lecture 137: Advanced Retrieval: Semantic Chunking, Hybrid Search & RRF
"""

def reciprocal_rank_fusion(rankings, k=60):
    scores = {}

    for ranking in rankings:
        for rank, document in enumerate(ranking, 1):
            scores[document] = scores.get(document, 0) + 1 / (k + rank)

    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


def main():
    lexical = ["doc-A", "doc-B", "doc-C"]
    semantic = ["doc-B", "doc-A", "doc-D"]

    fused = reciprocal_rank_fusion([lexical, semantic])

    print("RRF ranking:")
    for document, score in fused:
        print(f"{document}: {score:.6f}")


if __name__ == "__main__":
    main()
