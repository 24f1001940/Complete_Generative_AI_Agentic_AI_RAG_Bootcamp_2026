"""
Lecture 75: Why transformers changed AI
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    attention = nn.MultiheadAttention(
        embed_dim=64,
        num_heads=4,
        batch_first=True,
    )

    x = torch.randn(2, 10, 64)
    output, weights = attention(x, x, x)

    print("Input:", x.shape)
    print("Attention output:", output.shape)
    print("Attention weights:", weights.shape)


if __name__ == "__main__":
    main()
