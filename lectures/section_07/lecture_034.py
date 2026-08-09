"""
Lecture 34: Yield and lazy evaluation
Author: MOHD SAQIB
"""
import time

def lazy_file_chunker(filepath: str, chunk_size: int = 100):
    """Lazy evaluation stream that yields file chunks without loading entire files into RAM."""
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

if __name__ == "__main__":
    # Create temp sample file
    temp_file = Path("temp_large_log.txt")
    temp_file.write_text("Line " * 200, encoding="utf-8")

    chunk_stream = lazy_file_chunker("temp_large_log.txt", chunk_size=50)
    print("First 2 Lazy Chunks:")
    print("Chunk 1:", next(chunk_stream))
    print("Chunk 2:", next(chunk_stream))

    # Clean up
    if temp_file.exists():
        temp_file.unlink()