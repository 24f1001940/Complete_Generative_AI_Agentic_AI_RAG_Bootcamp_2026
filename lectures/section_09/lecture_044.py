"""
Lecture 44: Data Visualization with Matplotlib
Author: MOHD SAQIB
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_llm_latency_distribution(latencies: np.ndarray, output_path: str = "latency_dist.png"):
    """Plots and saves a distribution histogram of LLM inference latency."""
    plt.figure(figsize=(8, 5))
    plt.hist(latencies, bins=15, color="skyblue", edgecolor="black", alpha=0.7)
    
    plt.title("LLM Request Latency Distribution", fontsize=14, fontweight="bold")
    plt.xlabel("Latency (ms)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.axvline(np.mean(latencies), color="red", linestyle="dashed", linewidth=1.5, label=f"Mean: {np.mean(latencies):.1f}ms")
    
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Plot saved successfully to {output_path}")

if __name__ == "__main__":
    np.random.seed(42)
    # Generate mock latency dataset
    mock_latencies = np.random.normal(loc=800, scale=150, size=200)
    
    plot_llm_latency_distribution(mock_latencies, "lectures/section_09/latency_dist.png")