import streamlit as st
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

st.title("Forms")

with st.form(key="my_form"):
    e1 = st.text_input("st.text_input()")
    e2 = st.text_area("st.text_area()")
    e3 = st.date_input("st.date_input()")
    e4 = st.time_input("st.time_input()")
    e5 = st.radio("st.radio()", ["opt-1", "opt-2", "opt-3"])
    e6 = st.selectbox("st.selectbox()", ["opt-1", "opt-2", "opt-3"])
    e7 = st.select_slider("st.select_slider()", [1, 2, 3, 4, 5, 10, 20])
    e8 = st.checkbox("st.checkbox()", value=False)
    e9 = st.form_submit_button("st.form_submit_button()")
    if e9:
        st.write(e1, e2, e3, e4, e5, e6, e7, e8, e9)
