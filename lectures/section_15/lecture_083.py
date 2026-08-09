"""
Lecture 83: Open-Source vs Closed-Source Models & Choosing the Right Model
"""

def main():
    comparison = {
        "Open / open-weight models": [
            "More deployment control",
            "Potential local deployment",
            "More customization options",
        ],
        "Closed-source models": [
            "Provider-managed infrastructure",
            "Convenient API access",
            "Often quick to integrate",
        ],
    }

    for category, points in comparison.items():
        print(f"\n{category}")
        for point in points:
            print(" -", point)


if __name__ == "__main__":
    main()
