import streamlit as st
import pandas as pd
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
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.header("❌ Submeter inconformidade")
        option = st.selectbox('Semana de distribuição', options)
        option = st.selectbox('Tipo de Semana', ("AMC","15%","10%-5€"))
        st.text("Gasto: 78.121 €")
        st.text("Total de Freguesias: 500")
        st.text("Total de Caixas Postais: 128913")
        agree = st.checkbox('Distruibuição diferente da sugestão')

    c4, c5, c6 = st.columns([1, 2, 1])
    with c6:
        st.button('Submeter')

