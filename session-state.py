import streamlit as st
import os
import sys

MODE_CB = "callback"
MODE_RAW = "raw"

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)


def counter_inc(step):
    st.session_state.counter += step


def counter_reset():
    st.session_state.counter = 0


if "counter" not in st.session_state:
    st.session_state.counter = 0

st.title("Session State")

mode = st.radio(
    "mode",
    [MODE_CB, MODE_RAW],
    captions=["OK: 'before' and 'after' in sync", "KO: 'after' lags"],
    key="mode",
    persist_state="session",
    horizontal=True,
)

st.subheader("Before")
st.write(
    "\n".join(
        [
            f"- st.session_state.mode = {st.session_state.mode}",
            f"- mode = {mode}",
            f"- st.session_state.counter = {st.session_state.counter}",
        ]
    )
)

st.subheader("Control")

if mode == MODE_CB:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("inc+1", on_click=counter_inc, args=(1,))
    with col2:
        st.button("inc+2", on_click=counter_inc, args=(2,))
    with col3:
        st.button("reset", on_click=counter_reset)
elif mode == MODE_RAW:
    col1, col2 = st.columns(2)
    if col1.button("inc"):
        st.session_state.counter += 1
    if col2.button("reset"):
        st.session_state.counter = 0

st.subheader("After")
st.write(
    "\n".join(
        [
            f"- st.session_state.mode = {st.session_state.mode}",
            f"- mode = {mode}",
            f"- st.session_state.counter = {st.session_state.counter}",
        ]
    )
)

st.subheader("Session State")
st.write(st.session_state)
