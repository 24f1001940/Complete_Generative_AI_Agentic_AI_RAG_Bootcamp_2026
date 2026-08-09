"""
Lecture 78: Feed Forward Network + LayerNorm + Residual Connections
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    d_model = 64
    x = torch.randn(2, 10, d_model)

    layer_norm = nn.LayerNorm(d_model)

    feed_forward = nn.Sequential(
        nn.Linear(d_model, 256),
        nn.ReLU(),
        nn.Linear(256, d_model),
    )

    normalized = layer_norm(x)
    transformed = feed_forward(normalized)
    output = x + transformed

    print("Input:", x.shape)
    print("Output:", output.shape)


if __name__ == "__main__":
    main()
