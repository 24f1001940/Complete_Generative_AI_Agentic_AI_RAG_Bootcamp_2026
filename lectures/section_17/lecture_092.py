"""
Lecture 92: Understanding Pretrained Models
"""

def main():
    try:
        from transformers import AutoTokenizer, AutoModel
    except ImportError:
        print("Missing dependency: transformers torch")
        print("Install with: pip install transformers torch")
        return

    model_name = "distilbert-base-uncased"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    text = "Transformers are powerful."
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)

    print("Token IDs shape:", inputs["input_ids"].shape)
    print("Last hidden state shape:", outputs.last_hidden_state.shape)


if __name__ == "__main__":
    main()
