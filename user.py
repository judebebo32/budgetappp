import streamlit as st

# Title of the app
st.title("Hello, Streamlit Cloud!")

# Simple user input
name = st.text_input("What's your name?")

# Display a message based on input
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")
else:
    st.write("Please enter your name above.")
