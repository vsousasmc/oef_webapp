import streamlit as st
import pandas as pd
import datetime

## Create week options
pd_calendar = pd.read_csv("data/calendar.csv")
pd_calendar = pd_calendar[(pd_calendar["WEEKKEY_FOLHETO"]>=2021031) & (pd_calendar["WEEKKEY_FOLHETO"]<=2022053)]
options = []
for a,s in  pd_calendar.iterrows():
    week = s['WEEKKEY_FOLHETO']
    time_i = datetime.datetime.strptime(str(s['TIME_I']), '%Y%m%d').strftime('%m/%d/%y')
    time_f = datetime.datetime.strptime(str(s['TIME_I']), '%Y%m%d').strftime('%m/%d/%y')
    option = str(f"{week} ({time_i} - {time_f})")
    options.append(option)


def write():
    c29, c30, c31 = st.columns([1, 3, 1])

    with c30:

        st.title("🚚 Obter/Consultar Sugestão de Distribuição")
        option = st.selectbox('Semana para previsão', options)
        option = st.selectbox('Tipo de Semana', ("AMC","15%","10%-5€"))


        st.number_input('Orçamento', value=84000, step=1000)
        st.write("##")

    col1, col2, col3 = st.columns(3)
    with col3:
        st.button('Obter sugestão')