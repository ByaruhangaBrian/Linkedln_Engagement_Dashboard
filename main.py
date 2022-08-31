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
        st.image(os.path.abspath(("images/LI Logo.png")))

page_names_to_func = {"LinkedIn Engangements":main_page,
                      "Your Dashboard": page2,
                      "Data Directions": page3}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_func.keys())
page_names_to_func[selected_page]()


