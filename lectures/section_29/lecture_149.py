"""
Knowledge graph demonstration
"""

def main():
    graph = {
        "Python": [("used_for", "AI")],
        "AI": [("includes", "Machine Learning")],
        "Machine Learning": [("includes", "Deep Learning")],
    }

    for source, edges in graph.items():
        for relation, target in edges:
            print(f"{source} --{relation}--> {target}")


if __name__ == "__main__":
    main()
