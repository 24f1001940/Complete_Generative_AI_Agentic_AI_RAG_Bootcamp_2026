"""
Lecture 67: Introduction to NLP in deep learning
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    class SimpleNLPModel(nn.Module):
        def __init__(self, vocab_size, embedding_dim, hidden_dim, num_classes):
            super().__init__()
            self.embedding = nn.Embedding(vocab_size, embedding_dim)
            self.fc1 = nn.Linear(embedding_dim, hidden_dim)
            self.fc2 = nn.Linear(hidden_dim, num_classes)

        def forward(self, x):
            x = self.embedding(x)
            x = x.mean(dim=1)
            x = torch.relu(self.fc1(x))
            return self.fc2(x)

    model = SimpleNLPModel(1000, 64, 32, 2)
    sample_input = torch.randint(0, 1000, (4, 10))
    output = model(sample_input)

    print("Input shape:", sample_input.shape)
    print("Output shape:", output.shape)


if __name__ == "__main__":
    main()
