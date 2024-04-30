import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')
DATE_COLUMN = 'Date/Time'
DATA_URL = ('uber-raw-data-sep14.csv')

#ponemos una función para tomar una parte de los datos porque son muchos
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower
    data.rename(lowercase, axis = 'columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done! (using st.cache)')

st.dataframe(data)
