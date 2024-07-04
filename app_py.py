import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image

st.title('機械学習 理論と応用')
st.text('小さな会社のひとり情シスによる機械学習のポートフォリオ的なページです。\n'
          '転職活動中、副業案件募集中です。')

st.subheader('機械学習の価値')
st.text('・自動化(Automation)')
st.text('　単純作業や繰り返し作業など、コンピュータにやらせた方が効率的え効果的なタスクを自動化する')
st.text('・拡張(Augmentation)')
st.text('　意思決定など、人間にしか行えないタスクをサポートする')

st.subheader('ビジネスでの活用の大パターン2つ')
st.text('・応用志向型モデル')
st.text('　手元にあるデータをもとに未知のデータに対して予測・制御を行ったり、\n'
        '　新しいデータを生成して利用することを目指す。\n'
        '　現象の理解のしやすさ、できたモデルが内部メカニズムでどう判定したかはどうでもよく、あくまで与えられたデータの生成ルールを再現することが目的')
st.text('・理解志向型モデル')
st.text('　データがどういうメカニズムで生成されているのかを理解することを目指す。\n'
        '　対象となる現象において、どの要因が強く影響を与えているかを特定したり、なぜそのような現象が起こるのかを明らかにすることが目的')
image = Image.open('機械学習の価値.png')
st.image(image, width=500)

st.subheader('ビジネスへの応用サイクル')
image = Image.open('CRISP-DM_Process_Diagram.png')
st.image(image, width=500)
st.text('引用：「Cross-industry standard process for data mining」')

st.text('ビジネス理解\n'
        'データ理解\n'
        'データ準備\n'
        'モデリング\n'
        '評価\n'
        '展開\n'
        'フェーズの順序は厳密ではなく、異なるフェーズの間を行ったり来たりすることが通常必要である。\n'
        'プロセスダイアグラムの矢印は、フェーズ間の最も重要で頻繁な依存関係を示している。\n')

st.subheader('機械学習を活用するために必要なこと')
image = Image.open('ml_all.png')
st.image(image, width=500)
st.text('引用：「Hidden Technical Debt in Machine Learning Systems」')

