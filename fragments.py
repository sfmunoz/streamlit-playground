import streamlit as st
import os
import sys
from time import time

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)


@st.fragment()
def fragment1():
    st.title("fragment-1")
    t = time()
    if st.button("button-1", help="just fragment-1 time gets updated"):
        t = time()
    st.write(f"t1 = {t:.3f}")


@st.fragment()
def fragment2():
    st.title("fragment-2")
    t = time()
    if st.button(
        "button-2",
        help="every time gets updated because of 'st.rerun(scope=app)' execution",
    ):
        t = time()
        st.rerun(scope="app")
    st.write(f"t2 = {t:.3f}")


fragment1()
fragment2()

t3 = time()
t4 = time()

if st.button("button-3", help="every time gets updated"):
    t3 = time()
if st.button("button-4", help="every time gets updated"):
    t4 = time()

st.write(f"t3 = {t3:.3f}")
st.write(f"t4 = {t4:.3f}")
