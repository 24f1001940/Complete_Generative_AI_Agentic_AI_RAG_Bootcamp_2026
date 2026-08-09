"""
Lecture 79: Transformer Decoder, Complete Architecture & Text Generation
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    decoder_layer = nn.TransformerDecoderLayer(
        d_model=64,
        nhead=4,
        batch_first=True,
    )

    decoder = nn.TransformerDecoder(decoder_layer, num_layers=2)

    target = torch.randn(2, 5, 64)
    memory = torch.randn(2, 10, 64)

    output = decoder(target, memory)

    print("Target:", target.shape)
    print("Memory:", memory.shape)
    print("Decoder output:", output.shape)


if __name__ == "__main__":
    main()
