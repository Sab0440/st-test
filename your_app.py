import pandas as pd
import streamlit as st
import numpy as np

st.title('ML4B 2024')

#DataFrame
st.write("Here's my data:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

