import streamlit as st
import os
import sys
from time import time

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

with st.sidebar:
    st.title("sidebar")
    st.write("sidebar")
    i = st.text_input("st.text_input()")
    st.write("your input: " + i)

tab1, tab2, tab3 = st.tabs(["tab-1", "tab-2", "tab-3"])

with tab1:
    st.write("tab-1 content")

with tab2:
    st.write("tab-2 content")

with tab3:
    st.write("tab-3 content")

col1, col2 = st.columns(2, border=True)

with col1:
    st.header("col-1")
    st.write("col-1 content")

with col2:
    st.header("col-2")
    st.write("col-2 content")

with st.container(border=True):
    st.write("this is within a container")
    st.write("it's useful to group elements")

placeholder = st.empty()
placeholder.write("placeholder: EMPTY")

if st.button("update placeholder"):
    placeholder.write(f"placeholder: {time()}")

with st.expander("st.expander()"):
    st.write("- one\n- two\n- three")

st.button("hover to see details", help="this is the help of the button")
