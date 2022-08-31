import os
import openpyxl
import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import AgGrid
from datetime import datetime
import streamlit.components.v1 as components
import altair as alt

def main_page():
    col1, mid, col2 = st.columns([1,2,20])
    with col1:
        st.image(os.path.abspath("images/LI Logo.png"), width=100)
    with col2:
        st.write("# LinkedIn Engagement")
#     the Sidebar
    st.sidebar.markdown("# LinkedIn Engagement")
    st.sidebar.markdown("** Created By Brian Byaruhanga **")
    st.sidebar.markdown("##")

    st.sidebar.markdown("**Start** by uploading your data on the next page.")

    st.sidebar.markdown("The process for obtaining your data can be found on the **Data Directions page**.")

    # header

    st.subheader("How engaging are your posts?")

    # welcome photo

    welcome_photo = "people excited.png"

    st.image(os.path.abspath("images/" + welcome_photo))

    st.markdown(
        "**Track your post performance** over time by analyzing engagements, impressions, and the percent engagement "
        "per impression.")
    st.markdown("**Click** on any data point and **you're brought to that post's link!**")


# page_names_to_func = {"LinkedIn Engangements":main_page,
#                       "Your Dashboard": page2,
#                       "Data Directions": page3}
#
# selected_page = st.sidebar.selectbox("Select a page", page_names_to_func.keys())
# page_names_to_func[selected_page]()
