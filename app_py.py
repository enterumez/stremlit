import streamlit as st
import streamlit.components.v1 as stc

st.title('機械学習 理論と応用')

name = st.text_input('名前')
print(name)

submit_btn = st.button('送信')
cancel_btn = st.button('キャンセル')

if submit_btn:
    st.write('送信しました')
elif cancel_btn:
    st.write('キャンセルしました')
