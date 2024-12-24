import streamlit as st

st.title("Welcome to Streamlit!")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("Streamlit is an awesome Python library for creating web apps.")

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.write(f"Hello, {name}!")


#st.title("Interactive Widgets Demo")
# Slider
age = st.slider("Select your age", 1, 100, 25)
st.write(f"Your age is: {age}")

# Select box
color = st.selectbox("Choose a color", ["Red", "Green", "Blue"])
st.write(f"You selected: {color}")

# Radio buttons
choice = st.radio("Choose an option:", ["Option A", "Option B", "Option C"])
st.write(f"You chose: {choice}")


import pandas as pd
import numpy as np

st.title("DataFrames and Charts")

# DataFrame
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)
st.write("Sample DataFrame:")
st.dataframe(data)

# Line chart
st.line_chart(data)
