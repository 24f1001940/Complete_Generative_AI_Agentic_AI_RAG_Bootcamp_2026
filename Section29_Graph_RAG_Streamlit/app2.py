raw_examples = [
    {"input_text": "Explain QLoRA.", "output_text": "QLoRA combines quantization and LoRA to reduce memory use during fine-tuning."},
    {"input_text": "Write a short study tip.", "output_text": "Break your revision into small sessions and test yourself often."}
]



def clean_example(example):
    """
    Cleans a single example by stripping whitespace and ensuring proper formatting.
    
    Args:
        example (dict): A dictionary containing 'input_text' and 'output_text'.
        
    Returns:
        dict: A cleaned version of the input example.
    """
    cleaned_example = {
        "input_text": example["input_text"].strip(),
        "output_text": example["output_text"].strip()
    }
    return cleaned_example


train_set = cleaned_examples[:]
validation_set = cleaned_examples[:]



def format_for_gemma(input_text, output_text):
    return f"""
<start_of_turn>user
{input_text}
<end_of_turn>
<start_of_turn>model
{output_text}
<end_of_turn>
"""

# evaluate the result 

def evaluuate_examples(dataset):
    return len(dataset)




user_question = "Explain RAG in simple words."
chat_history = [
    "User: What is vector search?",
    "Assistant: Vector search finds similar meaning in embeddings.",
    "User: What is RAG?"
]



def trim_history(history,max_turns=2):
    return history[-max_turns:]


# def summarize_history(history):
#     return " ".join(history)

def summarize_history(history):
    return "The user is learning about vector search and RAG."


optimized_prompt = f"""
You are a helpful AI tutor.

Conversation summary:
{summarize_history(chat_history)}

User question:
{user_question}

Answer briefly and clearly.
"""

