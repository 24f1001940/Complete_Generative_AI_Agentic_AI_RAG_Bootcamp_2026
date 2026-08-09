"""
Lecture 43: Data manipulation with Pandas
Author: MOHD SAQIB
"""
import pandas as pd

def aggregate_model_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregates model performance metrics across distinct experiment groups."""
    grouped = df.groupby("model_name").agg(
        avg_latency=("latency_ms", "mean"),
        total_tokens=("total_tokens", "sum"),
        success_rate=("success", "mean"),
        sample_count=("model_name", "count")
    ).reset_index()
    
    return grouped

if __name__ == "__main__":
    runs_data = pd.DataFrame([
        {"model_name": "gpt-4o", "latency_ms": 850, "total_tokens": 400, "success": True},
        {"model_name": "gpt-4o", "latency_ms": 910, "total_tokens": 450, "success": True},
        {"model_name": "claude-3-5-sonnet", "latency_ms": 1100, "total_tokens": 520, "success": True},
        {"model_name": "claude-3-5-sonnet", "latency_ms": 1250, "total_tokens": 610, "success": False},
    ])

    cost_data = pd.DataFrame([
        {"model_name": "gpt-4o", "cost_per_1k_tokens": 0.005},
        {"model_name": "claude-3-5-sonnet", "cost_per_1k_tokens": 0.003},
    ])

    # Grouping and aggregations
    metrics_df = aggregate_model_metrics(runs_data)

    # Merging datasets
    merged_df = pd.merge(metrics_df, cost_data, on="model_name", how="inner")
    merged_df["estimated_cost"] = (merged_df["total_tokens"] / 1000) * merged_df["cost_per_1k_tokens"]

    print("Aggregated and Merged Performance Report:")
    print(merged_df)