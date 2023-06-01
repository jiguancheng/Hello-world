import streamlit as st

st.markdown('A test for file operations.')
a = open('main.py', 'r')
st.code(a.read(), 'python', line_numbers=True)
try:
    b = open('main2.py', 'a+')
except:
    b = open('main2.py', 'w')
b.write('A test.')
b.close()
st.text('Success.')
b = open('main2.py', 'r')
st.text(b.read())
b.close()
