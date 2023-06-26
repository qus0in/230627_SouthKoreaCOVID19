import streamlit as st
import pandas as pd

@st.cache_data
def get_sales():
    return pd.read_csv("./Case.csv")

def page_config():
    st.set_page_config(
        page_title="South Korea COVID-19",
        page_icon="🏥",
    )