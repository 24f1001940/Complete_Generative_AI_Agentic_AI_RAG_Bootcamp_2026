"""
Lecture 47: Displaying outputs
"""
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.header("Displaying Data Outputs")
    
    # 1. Displaying a DataFrame
    st.subheader("Interactive DataFrames")
    np.random.seed(42)
    data = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["Feature A", "Feature B", "Feature C"]
    )
    st.dataframe(data, use_container_width=True)

    # 2. Displaying Metrics
    st.subheader("KPI Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Accuracy", value="94.5%", delta="1.2%")
    col2.metric(label="Latency", value="120ms", delta="-15ms", delta_color="inverse")
    col3.metric(label="Active Users", value="1,245", delta="84")

    # 3. Native Charts
    st.subheader("Native Line Chart")
    st.line_chart(data)

if __name__ == "__main__":
    main()