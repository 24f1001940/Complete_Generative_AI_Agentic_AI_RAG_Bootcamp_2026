"""
Lecture 21: Reading structured data files
Author: MOHD SAQIB
"""
import csv
import json
from pathlib import Path

def handle_structured_files():
    json_path = Path("config.json")
    csv_path = Path("data.csv")

    # Handling JSON Files
    sample_json = {
        "app_name": "RAG Assistant",
        "version": "1.0",
        "settings": {"max_tokens": 1024, "temperature": 0.2}
    }
    json_path.write_text(json.dumps(sample_json, indent=2), encoding="utf-8")
    
    with open(json_path, "r", encoding="utf-8") as f:
        loaded_json = json.load(f)

    # Handling CSV Files
    rows = [
        ["id", "model", "latency_ms"],
        [1, "gpt-4o", 250],
        [2, "claude-3-5-sonnet", 210]
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        loaded_csv = list(reader)

    return loaded_json, loaded_csv

if __name__ == "__main__":
    json_data, csv_data = handle_structured_files()
    print("Parsed JSON Content:", json_data)
    print("Parsed CSV Content:", csv_data)