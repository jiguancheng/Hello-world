import streamlit as st


def video_translation(filetype: str):
    ...


st.markdown('')
st.title('快捷应用')
c1 = st.expander('视频工具')
c2 = st.expander('音频工具')
button = []
with c1:
    video_file = st.file_uploader('视频文件', ('mp4', 'avy', 'ts'))
    video_selectbox = st.selectbox('视频格式', ('mp4', 'avy', 'ts'))
    button.append(st.button('转换'))
    if video_file is not None:
        if button[0]:
            video_translation(filetype=video_selectbox)