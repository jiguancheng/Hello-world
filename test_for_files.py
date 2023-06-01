import streamlit as st

st.markdown('A test for file operations.')
a = open('main.py', 'r')
st.code(a.read(), 'python', line_numbers=True)
b = open('main2.py', 'w')
b.write('A test.')
b.close()
st.text('Success.')
