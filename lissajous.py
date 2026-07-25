import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import os
import sys
import math

st.set_page_config(
    page_title="Lissajous curves",
    layout="wide",
)

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
a = 2
b = 1
fa = 1
fb = 1.5
d = 0

x = a * np.sin(2 * math.pi * fa * t + d)
y = b * np.sin(2 * math.pi * fb * t)

chart_xy = (
    alt.Chart(pd.DataFrame({"x": x, "y": y}))
    .mark_circle()
    .encode(
        x=alt.X("x", title="x", scale=alt.Scale(domain=(-1.1 * a, 1.1 * a))),
        y=alt.Y("y", title="y", scale=alt.Scale(domain=(-1.1 * b, 1.1 * b))),
    )
)

chart_yx = (
    alt.Chart(pd.DataFrame({"x": y, "y": x}))
    .mark_circle()
    .encode(
        x=alt.X("x", title="y", scale=alt.Scale(domain=(-1.1 * b, 1.1 * b))),
        y=alt.Y("y", title="x", scale=alt.Scale(domain=(-1.1 * a, 1.1 * a))),
    )
)


col1, col2 = st.columns(2, border=True)

with col1:
    st.title("x → y")
    st.subheader("Altair")
    st.altair_chart(chart_xy)
    st.subheader("Scatter")
    st.scatter_chart(pd.DataFrame({"x": x, "y": y}), x="x", y="y", size=50)

with col2:
    st.title("y → x")
    st.subheader("Altair")
    st.altair_chart(chart_yx)
    st.subheader("Scatter")
    st.scatter_chart(pd.DataFrame({"x": x, "y": y}), x="y", y="x", size=50)
