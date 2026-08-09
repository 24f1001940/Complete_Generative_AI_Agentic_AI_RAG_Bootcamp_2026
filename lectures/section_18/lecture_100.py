"""
Lecture 100: Memory Basics
"""

def main():
    chat_history = []

    chat_history.append({
        "role": "user",
        "content": "My name is Alex.",
    })

    chat_history.append({
        "role": "assistant",
        "content": "Nice to meet you, Alex!",
    })

    for message in chat_history:
        print(f"{message['role']}: {message['content']}")


if __name__ == "__main__":
    main()
