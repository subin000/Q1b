import streamlit as st
import pandas as pd
import numpy as np

# Simple Streamlit app
st.title("My Streamlit Web App")
st.write("Hello, Streamlit!")
st.write("Here is a random DataFrame:")

st.write("Changes")

# Display a random dataframe
df = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
st.write(df)
