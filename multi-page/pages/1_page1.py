import streamlit as st


def page1(p):
    st.set_page_config(f"page-1{p}")
    st.title(f"page-1{p}")
    st.write(f"page-1{p}")


def page_1a():
    page1("a")


def page_1b():
    page1("b")


def page_1c():
    page1("c")


def page_1d():
    page1("d")


pages = {"page-1a": page_1a, "page-1b": page_1b, "page-1c": page_1c, "page-1d": page_1d}

page_name = st.sidebar.selectbox(
    "select a subpage", pages.keys(), persist_state="session", key="page1"
)
pages[page_name]()
