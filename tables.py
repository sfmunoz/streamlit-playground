import streamlit as st
import pandas as pd
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

df = pd.DataFrame(
    dict(
        Name=["One", "Two", "Three", "Four"],
        Double=[2, 4, 6, 8],
        Translation=["Uno", "Dos", "Tres", "Cuatro"],
    )
)

st.title("Tables")

st.subheader(("st.dataframe()"))
st.dataframe(df)

st.subheader("st.data_editor()")
df_edit = st.data_editor(df)

st.subheader("st.table()")
st.table(df)

st.subheader("st.metric()")
st.metric("Degrees", value=25.1, delta=2.3)
