import streamlit as st
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.write(f"(before) counter = {st.session_state.counter}")

if st.button("inc"):
    st.session_state.counter += 1

if st.button("reset"):
    st.session_state.counter = 0

st.write(f"(after) counter = {st.session_state.counter}")
