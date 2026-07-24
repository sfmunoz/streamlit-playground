import streamlit as st
import os
import sys
import time

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)


@st.cache_data(ttl=5)
def fetch_data():
    time.sleep(2)
    return {"data": round(time.time(), 3)}


st.write(">> " + str(round(time.time(), 3)))
data = fetch_data()
st.write(">> " + str(data))
