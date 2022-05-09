import pandas as pd
import numpy as np
import datetime as dt
import streamlit as st

st.title('Stock Chart Simulator')

today = dt.datetime.now()
periods = st.slider('How many days back from today?', 1, 1000, value=500)
simuls = st.slider('How many simulations?', 1, 20, value=1)

idx = pd.date_range(end=today, periods=periods, freq='D')
df = pd.DataFrame(np.random.normal(loc=0,scale=5,size=(periods,simuls)), index=idx)
df = df.cumsum()

st.line_chart(df)
st.write('Do you see trends or patterns in randomly generated data?')