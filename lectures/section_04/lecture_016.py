"""
Lecture 16: Arguments, Lambdas, Map & Filter
Author: MOHD SAQIB
"""

def build_agent_config(model_name, *tools, **hyperparams):
    return {
        "model": model_name,
        "tools": list(tools),
        "parameters": hyperparams
    }

if __name__ == "__main__":
    config = build_agent_config(
        "gpt-4o",
        "calculator", "web_search",
        temperature=0.2, top_p=0.9
    )
    print("Agent Config:", config)

    scores = [0.45, 0.88, 0.92, 0.61, 0.79]
    high_confidence = list(filter(lambda x: x >= 0.75, scores))
    scaled_scores = list(map(lambda x: round(x * 100, 1), high_confidence))

    print("Filtered High Confidence Scores:", high_confidence)
    print("Scaled Scores (%):", scaled_scores)