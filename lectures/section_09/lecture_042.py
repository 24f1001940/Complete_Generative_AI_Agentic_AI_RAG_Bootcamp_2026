"""
Lecture 42: Data Analysis with Pandas
Author: MOHD SAQIB
"""
import pandas as pd

def clean_llm_benchmark_data(raw_data: list[dict]) -> pd.DataFrame:
    """Cleans and transforms raw benchmark log entries into a structured DataFrame."""
    df = pd.DataFrame(raw_data)
    
    # Handle missing values
    df["latency_ms"] = df["latency_ms"].fillna(df["latency_ms"].median())
    
    # Feature engineering
    df["tokens_per_sec"] = (df["completion_tokens"] / (df["latency_ms"] / 1000)).round(2)
    
    # Filtering outliers/invalid rows
    clean_df = df[df["status_code"] == 200].copy()
    
    return clean_df

if __name__ == "__main__":
    benchmark_logs = [
        {"model": "gpt-4o", "completion_tokens": 150, "latency_ms": 1200, "status_code": 200},
        {"model": "llama-3.3-70b", "completion_tokens": 300, "latency_ms": None, "status_code": 200},
        {"model": "gpt-4o", "completion_tokens": 80, "latency_ms": 600, "status_code": 500},
        {"model": "claude-3-5-sonnet", "completion_tokens": 220, "latency_ms": 950, "status_code": 200},
    ]

    processed_df = clean_llm_benchmark_data(benchmark_logs)
    print("Cleaned LLM Benchmark Data:")
    print(processed_df[["model", "completion_tokens", "latency_ms", "tokens_per_sec"]])