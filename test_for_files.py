import streamlit as st

st.markdown('A test for file operations.')
a = open('main.py', 'r')
st.code(a.read(), 'python', line_numbers=True)
