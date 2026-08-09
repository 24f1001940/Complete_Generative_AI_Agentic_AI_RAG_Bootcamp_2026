"""
Lecture 71: LSTM Intuition + Complete LSTM Architecture
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    lstm = nn.LSTM(
        input_size=32,
        hidden_size=64,
        num_layers=1,
        batch_first=True,
    )

    x = torch.randn(4, 10, 32)
    output, (hidden, cell) = lstm(x)

    print("Input:", x.shape)
    print("Output:", output.shape)
    print("Hidden state:", hidden.shape)
    print("Cell state:", cell.shape)


if __name__ == "__main__":
    main()
