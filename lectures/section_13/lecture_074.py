"""
Lecture 74: Seq2Seq Architecture + Attention Mechanism
"""

def attention(query, keys, values):
    import torch
    import torch.nn.functional as F

    scores = torch.matmul(query, keys.transpose(-2, -1))
    weights = F.softmax(scores, dim=-1)
    context = torch.matmul(weights, values)

    return context, weights


def main():
    try:
        import torch
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    query = torch.randn(2, 1, 16)
    keys = torch.randn(2, 5, 16)
    values = torch.randn(2, 5, 16)

    context, weights = attention(query, keys, values)

    print("Context:", context.shape)
    print("Attention weights:", weights.shape)


if __name__ == "__main__":
    main()
