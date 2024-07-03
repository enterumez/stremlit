import streamlit as st

st.title('サプーアプリ')
st.caption('これはサプーの動画用のテストアプリです')

name = st.text_input('名前')
print(name)

submit_btn = st.button('送信')
cancel_btn = st.button('キャンセル')

if submit_btn:
    st.write('送信しました')
elif cancel_btn:
    st.write('キャンセルしました')
