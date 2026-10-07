import streamlit as st

st.title("Addition Program")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

if st.button("Add"):
    result = num1 ++ str(num2)
    st.success(f"Addition = {result}")
