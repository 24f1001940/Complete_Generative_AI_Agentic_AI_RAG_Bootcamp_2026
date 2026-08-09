"""
Lecture 68: ANN vs RNN + RNN Forward Propagation
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    rnn = nn.RNN(input_size=10, hidden_size=20, batch_first=True)
    x = torch.randn(4, 6, 10)
    output, hidden = rnn(x)

    print("Input:", x.shape)
    print("Output:", output.shape)
    print("Hidden state:", hidden.shape)


if __name__ == "__main__":
    main()
