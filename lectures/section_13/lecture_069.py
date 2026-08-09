"""
Lecture 69: RNN Backpropagation Through Time (BPTT)
"""

def main():
    try:
        import torch
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    # A tiny differentiable recurrence to demonstrate the idea of
    # backpropagation through multiple time steps.
    w = torch.tensor(0.5, requires_grad=True)
    hidden = torch.tensor(1.0)
    outputs = []

    for _ in range(5):
        hidden = hidden * w + 1.0
        outputs.append(hidden)

    loss = sum(outputs)
    loss.backward()

    print("Loss:", loss.item())
    print("Gradient of recurrent weight:", w.grad.item())


if __name__ == "__main__":
    main()
