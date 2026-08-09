"""
Lecture 76: Encoder Architecture + Positional Encoding
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    encoder_layer = nn.TransformerEncoderLayer(
        d_model=64,
        nhead=4,
        batch_first=True,
    )

    encoder = nn.TransformerEncoder(encoder_layer, num_layers=2)

    x = torch.randn(2, 10, 64)
    output = encoder(x)

    print("Input:", x.shape)
    print("Encoder output:", output.shape)


if __name__ == "__main__":
    main()
