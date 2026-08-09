"""
Lecture 162: AWS Cloud Deployment: Bedrock, Lambda & SageMaker
"""

def main():
    services = {
        "Amazon Bedrock": "Managed access to foundation models.",
        "AWS Lambda": "Serverless function execution.",
        "Amazon SageMaker": "Machine learning development and deployment.",
    }

    print("AWS services in the lecture:")
    for name, description in services.items():
        print(f"{name}: {description}")


if __name__ == "__main__":
    main()
