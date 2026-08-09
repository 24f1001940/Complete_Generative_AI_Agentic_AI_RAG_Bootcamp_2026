"""
Lecture 23: Classes and objects
Author: MOHD SAQIB
"""

class SimpleBot:
    """Basic representation of a chat assistant object."""
    bot_type = "Conversational Assistant"

    def greet(self, user_name: str) -> str:
        return f"Hello {user_name}! I am your {self.bot_type}."

if __name__ == "__main__":
    bot_instance = SimpleBot()
    print("Bot Class Type:", bot_instance.bot_type)
    print("Greeting:", bot_instance.greet("Saqib"))