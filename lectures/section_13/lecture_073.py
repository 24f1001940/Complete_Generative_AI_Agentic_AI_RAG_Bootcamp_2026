"""
Lecture 73: Bidirectional RNN
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    model = nn.RNN(
        input_size=32,
        hidden_size=64,
        batch_first=True,
        bidirectional=True,
    )

    x = torch.randn(4, 10, 32)
    output, hidden = model(x)

    print("Input:", x.shape)
    print("Output:", output.shape)
    print("Hidden state:", hidden.shape)


if __name__ == "__main__":
    main()
