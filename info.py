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

    c29, c30, c31 = st.columns([1, 6, 1])

    with c30:

        st.subheader("📅 Update Calendar")
        calendar_file = st.file_uploader(
            "",
            key="1",
            help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
        )

        if calendar_file is not None:
            file_container = st.expander("Check your uploaded .csv")
            shows = pd.read_csv(calendar_file)
            calendar_file.seek(0)
            file_container.write(shows)
        st.info(
            f"""
                ⬇️  Get the template [calenda.csv](calendar)
                """
        )
        st.markdown('<hr style="height:3px;border-width:0;color:gray;background-color:gray">', unsafe_allow_html=True)

        st.subheader("📍 Update Parishs Info")
        parish_file = st.file_uploader(
            "",
            key="2",
            help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
        )

        if parish_file is not None:
            file_container = st.expander("Check your uploaded .csv")
            shows = pd.read_csv(parish_file)
            parish_file.seek(0)
            file_container.write(shows)
        st.info(
            f"""
                ⬇️  Get the template [parish.csv](calendar)
                """
        )
