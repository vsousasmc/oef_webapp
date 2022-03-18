import streamlit as st
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import io
import home, info, metrics, submission

def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon=":newspaper:", page_title="Optimização de Entrega de Folhetos", layout="wide")


col1, mid, col2 = st.columns([1,1,20])
with col1:
    st.image('mc_logo.png', width=150)
with col2:
    st.title("Optimização de Entrega de Folhetos" )

st.markdown(
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
    unsafe_allow_html=True,
)



query_params = st.experimental_get_query_params()

tabs = {'home': 'Sugestão de Entrega',
        'submission': "Submissão de Inconformidade",
           'info': 'Adicionar/Alterar Info',
           'metrics': 'Consultar Métricas'
        }
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "home"

if active_tab not in tabs:
    st.experimental_set_query_params(tab="home")
    active_tab = "home"

li_items = "".join(
    f"""
    <li class="nav-item">
        <a target= "_self" class="nav-link{' active' if k==active_tab else ''}" href="/?tab={k}">{v}</a>
    </li>
    """
    for k, v in tabs.items()
)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>
"""

st.markdown(tabs_html, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if active_tab == "home":
    home.write()
elif active_tab == "submission":
    submission.write()
elif active_tab == "info":
    info.write()
elif active_tab == "metrics":
    metrics.write()
else:
    st.error("Something has gone terribly wrong.")
