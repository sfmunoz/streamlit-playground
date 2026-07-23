import streamlit as st
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

st.title("Hello world")
for k, v in sorted(os.environ.items()):
    st.markdown(f"- {k}: {v}")
