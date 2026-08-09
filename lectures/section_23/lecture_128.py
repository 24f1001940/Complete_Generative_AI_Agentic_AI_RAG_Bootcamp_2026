"""
Lecture 128: Enterprise Infrastructure: AWS Lifecycle, Scaling Architecture & Reliability
"""

def main():
    deployment_checklist = [
        "Application entry point",
        "Dependencies / requirements",
        "Environment variables",
        "Secrets management",
        "Health checks",
        "Logging",
        "Scaling strategy",
        "Monitoring",
    ]

    print("Deployment checklist:")
    for item in deployment_checklist:
        print(" -", item)


if __name__ == "__main__":
    main()
