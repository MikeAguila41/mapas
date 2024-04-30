import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [20.5544108, -100.3991748], 
    columns=['lat', 'lon']) 
#mil renglon es por dos columnas de numeros aleatorios
#al final son las coordenadas

st.dataframe(map_data)
st.map(map_data)