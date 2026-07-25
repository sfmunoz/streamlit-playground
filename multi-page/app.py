import streamlit as st
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

st.set_page_config("the main page")
st.title("Multipage")
st.write("ref: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app")
