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
    chart_library = st.radio(
        "Chart library",
        [CHART_SCATTER, CHART_ALTAIR],
        help=f"Choose between {CHART_SCATTER} and {CHART_ALTAIR}",
        horizontal=True,
    )
    a = st.slider(
        "A", help="x amplitude", min_value=0.1, max_value=5.0, step=0.1, value=2.0
    )
    b = st.slider(
        "B", help="y amplitude", min_value=0.1, max_value=5.0, step=0.1, value=1.0
    )
    fa = st.slider(
        "$f_a$", help="x frequency", min_value=0.1, max_value=10.0, step=0.1, value=1.0
    )
    fb = st.slider(
        "$f_b$", help="y frequency", min_value=0.1, max_value=10.0, step=0.1, value=3.0
    )
    d = st.slider(
        "$d$ (multiplied by $\pi$)",
        help="x delta (will be multiplied by $\pi$ when used)",
        min_value=0.0,
        max_value=2.0,
        step=0.01,
        value=0.25,
    )
    segments = st.slider(
        "segments",
        help=r"number of segments to draw within [0,2$\pi$) range",
        min_value=20,
        max_value=2000,
        step=1,
        value=500,
    )
    st.divider()
    st.title("Lissajous curves")
    st.write(DESC)

t = time_points(segments)

x = a * np.sin(2 * math.pi * fa * t + d * math.pi)
y = b * np.sin(2 * math.pi * fb * t)

col1, col2 = st.columns(2, border=True)

with col1:
    st.title(f"x → y ({chart_library} chart)")
    if chart_library == CHART_SCATTER:
        st.scatter_chart(
            pd.DataFrame({"x": x, "y": y, "t": t}),
            x="x",
            y="y",
            color="t",
            size=50,
        )
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
        st.scatter_chart(
            pd.DataFrame({"x": x, "y": y, "t": t}),
            x="y",
            y="x",
            color="t",
            size=50,
        )
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
