"""
Lecture 70: Limitations of RNN + Simple RNN with Word Embeddings
"""

def main():
    try:
        import torch
        import torch.nn as nn
    except ImportError:
        print("Missing dependency: torch")
        print("Install from: https://pytorch.org/")
        return

    vocab_size = 5000
    embedding_dim = 64
    hidden_dim = 32

    embedding = nn.Embedding(vocab_size, embedding_dim)
    rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)

    tokens = torch.randint(0, vocab_size, (2, 8))
    embeddings = embedding(tokens)
    output, hidden = rnn(embeddings)

    print("Tokens:", tokens.shape)
    print("Embeddings:", embeddings.shape)
    print("RNN output:", output.shape)
    print("Hidden state:", hidden.shape)


if __name__ == "__main__":
    main()
