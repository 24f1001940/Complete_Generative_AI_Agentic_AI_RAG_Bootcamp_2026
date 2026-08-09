"""
Lecture 60: One-hot encoding
"""

import numpy as np


def main():
    words = ["cat", "dog", "apple"]
    vocabulary = {word: index for index, word in enumerate(words)}

    print("Vocabulary:", vocabulary)

    for word in words:
        vector = np.zeros(len(words), dtype=int)
        vector[vocabulary[word]] = 1
        print(f"{word}: {vector}")


if __name__ == "__main__":
    main()
