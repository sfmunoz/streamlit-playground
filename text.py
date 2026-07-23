import streamlit as st
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.markdown("**Markdown**")
st.caption("caption")
st.divider()

with open(sys.argv[0]) as fp:
    st.code(fp.read(), "python")
