import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('ML4B 2024')

#DataFrame
st.write("Here's my data:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

#Python Test + Line Chart
x_axis = [1.6,2,3,4]
y_axis = [10,15, 18,20]

plt.plot(x_axis, y_axis)
plt.title("Line Chart")
plt.xlabel("x_axis")
plt.ylabel("y_axis")
plt.show()
