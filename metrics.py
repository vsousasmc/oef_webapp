import streamlit as st
import pandas as pd
import numpy as np

def write():
    st.title("Increment médio por cliente")
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['Distribuição', 'Controlo'])

    st.line_chart(chart_data)