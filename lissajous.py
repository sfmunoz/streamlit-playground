import streamlit as st
import os
import sys

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)

DESC = r"""Ref: [https://en.wikipedia.org/wiki/Lissajous_curve](https://en.wikipedia.org/wiki/Lissajous_curve)

A Lissajous curve is the graph of a system of parametric equations

- $x = A sin(2 \pi f_a t + δ)$
- $y = B sin(2 \pi f_b t)$

which describe the superposition of two perpendicular oscillations in x and y directions of different angular frequency (a and b).
"""

st.title("Lissajous curves")
st.write(DESC)
