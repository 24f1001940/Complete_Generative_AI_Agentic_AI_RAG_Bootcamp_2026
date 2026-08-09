"""
Lecture 124: Reliable Schema Design, Fallbacks & Output Parsing Error Handling
"""

def parse_integer(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def main():
    examples = ["42", "not-a-number", None]

    for value in examples:
        result = parse_integer(value, default=-1)
        print(f"Input={value!r} -> Parsed={result}")


if __name__ == "__main__":
    main()
