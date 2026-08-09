"""
Lecture 19: File operations
Author: MOHD SAQIB
"""
from pathlib import Path

def explore_file_operations():
    base_dir = Path("data_demo")
    base_dir.mkdir(exist_ok=True)
    
    sample_file = base_dir / "sample.txt"
    sample_file.write_text("Initializing file operations demo.", encoding="utf-8")
    
    stats = {
        "exists": sample_file.exists(),
        "is_file": sample_file.is_file(),
        "size_bytes": sample_file.stat().st_size,
        "absolute_path": str(sample_file.resolve())
    }
    return stats

if __name__ == "__main__":
    print("File Operations Metadata:", explore_file_operations())