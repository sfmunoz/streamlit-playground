import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

data1 = pd.DataFrame(
    np.random.randn(12, 4),
    columns=["One", "Two", "Three", "Four"],
)

data2 = pd.DataFrame(
    {
        "x": np.random.randn(50),
        "y": np.random.randn(50),
    }
)

st.title("Charts")

st.subheader("Data")
st.write(data1)

st.subheader("st.area_chart()")
st.area_chart(data1)

st.subheader("st.line_chart()")
st.line_chart(data1)

st.subheader("st.scatter_chart()")
st.scatter_chart(data2)
st.scatter_chart(data2, x="x", y="y")
