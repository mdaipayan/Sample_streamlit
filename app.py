import streamlit as st

st.title("My First Web App")
name = st.text_input("What is your name?")
if name:
    st.success(f"Hello, {name}! Your app is live 🎉")
