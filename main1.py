import streamlit as st
import time as t
import pandas as pd

data1 = [11, 23, 57, 109, 87, 47, 33, 77, 79, 36]
data2 = [3, 4, 18, 26, 22, 13, 7, 28, 20, 12]
data3 = [80, 74, 77, 43, 70, 57, 71, 69, 68, 67]
data4 = [66.1, 62.4, 54.4, 48.4, 50.7, 55.1, 58.2, 48.9, 52.6, 56.3]

st.title('校次和班次:')
chart1 = st.line_chart(pd.DataFrame({'校次': [28], '班次': [12]}))
for i in range(len(data1)):
    chart1.add_rows(pd.DataFrame({'校次': [data1[i]], '班次': [data2[i]]}))
    t.sleep(.2)

st.title('总分和标准分:')
chart2 = st.line_chart(pd.DataFrame({'总分': [77], '标准分': [56.5]}))
for i in range(len(data3)):
    chart2.add_rows(pd.DataFrame({'总分': [data3[i]], '标准分': [data4[i]]}))
    t.sleep(.2)
