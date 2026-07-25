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

CHART_SCATTER = "scatter"
CHART_ALTAIR = "altair"

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
    chart_library = st.radio("Chart library", [CHART_SCATTER, CHART_ALTAIR])
    st.divider()
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

col1, col2 = st.columns(2, border=True)

with col1:
    st.title(f"x → y ({chart_library} chart)")
    if chart_library == CHART_SCATTER:
        st.scatter_chart(pd.DataFrame({"x": x, "y": y}), x="x", y="y", size=50)
    elif chart_library == CHART_ALTAIR:
        chart_xy = (
            alt.Chart(pd.DataFrame({"x": x, "y": y}))
            .mark_circle()
            .encode(
                x=alt.X("x", title="x", scale=alt.Scale(domain=(-1.1 * a, 1.1 * a))),
                y=alt.Y("y", title="y", scale=alt.Scale(domain=(-1.1 * b, 1.1 * b))),
            )
        )
        st.altair_chart(chart_xy)

with col2:
    st.title(f"y → x ({chart_library} chart)")
    if chart_library == CHART_SCATTER:
        st.scatter_chart(pd.DataFrame({"x": x, "y": y}), x="y", y="x", size=50)
    elif chart_library == CHART_ALTAIR:
        chart_yx = (
            alt.Chart(pd.DataFrame({"x": y, "y": x}))
            .mark_circle()
            .encode(
                x=alt.X("x", title="y", scale=alt.Scale(domain=(-1.1 * b, 1.1 * b))),
                y=alt.Y("y", title="x", scale=alt.Scale(domain=(-1.1 * a, 1.1 * a))),
            )
        )
        st.altair_chart(chart_yx)
