"""
Lecture 77: Self-Attention + Multi-Head Attention
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    x = torch.randn(2, 8, 64)

    attention = nn.MultiheadAttention(
        embed_dim=64,
        num_heads=8,
        batch_first=True,
    )

    output, weights = attention(x, x, x)

    print("Input:", x.shape)
    print("Output:", output.shape)
    print("Attention weights:", weights.shape)


if __name__ == "__main__":
    main()
