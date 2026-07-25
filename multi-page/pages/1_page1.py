import streamlit as st


def page_a():
    st.set_page_config("page-1a")
    st.title("page-1a")
    st.write("page-1a")


def page_b():
    st.set_page_config("page-1b")
    st.title("page-1b")
    st.write("page-1b")


page_names_to_funcs = {
    "page-a": page_a,
    "page-b": page_b,
}

demo_name = st.sidebar.selectbox(
    "select a subpage", page_names_to_funcs.keys(), persist_state="session", key="page1"
)
page_names_to_funcs[demo_name]()
