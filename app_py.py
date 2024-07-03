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

<iframe class="speakerdeck-iframe" frameborder="0" src="https://speakerdeck.com/player/8eaed11763ea4d0d901a4bf870ac52c7" title="プライシングについて" allowfullscreen="true" style="border: 0px; background: padding-box padding-box rgba(0, 0, 0, 0.1); margin: 0px; padding: 0px; border-radius: 6px; box-shadow: rgba(0, 0, 0, 0.2) 0px 5px 40px; width: 100%; height: auto; aspect-ratio: 560 / 315;" data-ratio="1.7777777777777777"></iframe>
