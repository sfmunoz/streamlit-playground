import streamlit as st
import pandas as pd
import numpy as np
import os
import sys
import math


DESC = r"""Ref: [https://en.wikipedia.org/wiki/Lissajous_curve](https://en.wikipedia.org/wiki/Lissajous_curve)

A Lissajous curve is the graph of a system of parametric equations

- $x = A sin(2 \pi f_a t + δ)$
- $y = B sin(2 \pi f_b t)$

which describe the superposition of two perpendicular oscillations in x and y directions of different angular frequency (a and b).
"""

if not st.runtime.exists():
    cmd = ["bash", "run.sh", *sys.argv]
    os.execvp(cmd[0], cmd)


def time_points(segments):
    step = 2.0 * math.pi / segments
    return np.arange(segments) * step


with st.sidebar:
    st.title("Lissajous curves")
    st.write(DESC)


t = time_points(100)
a = 1
b = 1
fa = 1
fb = 1.5
d = 0

x = a * np.sin(2 * math.pi * fa * t + d)
y = b * np.sin(2 * math.pi * fb * t)


data_xy = pd.DataFrame({"x": x, "y": y})
data_yx = pd.DataFrame({"x": y, "y": x})

col1, col2 = st.columns(2, border=True)

with col1:
    st.title("x → y")
    st.scatter_chart(data_xy, x="x", y="y")

with col2:
    st.title("y → x")
    st.scatter_chart(data_yx, x="y", y="x")
