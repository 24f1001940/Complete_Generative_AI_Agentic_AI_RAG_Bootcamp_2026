"""
Lecture 27: Encapsulation
Author: MOHD SAQIB
"""

class SecureAPIClient:
    """Demonstrates private attributes and property getters/setters."""

    def __init__(self, api_key: str):
        self.__api_key = api_key  # Private attribute
        self._request_count = 0   # Protected attribute

    @property
    def api_key_masked(self) -> str:
        """Returns a masked version of the private key."""
        return f"{self.__api_key[:4]}...{self.__api_key[-4:]}" if len(self.__api_key) > 8 else "****"

    def make_request(self) -> str:
        self._request_count += 1
        return f"Request #{self._request_count} authorized using key: {self.api_key_masked}"

if __name__ == "__main__":
    client = SecureAPIClient("sk-proj-1234567890abcdef")
    print("Masked Key:", client.api_key_masked)
    print(client.make_request())