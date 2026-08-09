"""
Lecture 152: Fine-Tuning Mechanics: Quantization, LoRA & QLoRA
"""

def main():
    techniques = {
        "Quantization": "Reduce numerical precision to reduce memory usage.",
        "LoRA": "Train a small set of low-rank adapter parameters.",
        "QLoRA": "Combine quantized base weights with LoRA adapters.",
    }

    for name, description in techniques.items():
        print(f"{name}: {description}")


if __name__ == "__main__":
    main()
