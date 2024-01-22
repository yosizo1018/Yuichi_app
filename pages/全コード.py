import streamlit as st

#コードを埋め込むことができる
code = '''
#トップページ
import streamlit as st
from PIL import Image

# テキスト関連
st.title('スケジュール調整アプリ')
st.title('飲酒産業株式会社　社員会')
st.caption('令和６年度新入社員歓迎会出欠(ご家族参加型)')
st.subheader('新入社員５名参加予定！！(中途入社含む)')
st.text('※変更は3/31までにお願いします。')

st.text('')
st.text('')
#画像
st.text('※店舗イメージ')
image = Image.open('./data/居酒屋.png')
st.image(image, width=200)
st.text('')
#動画
st.text('イメージ動画')
video_file = open('./data/asahi movie.mp4', 'rb')
video_bites = video_file.read()
st.video(video_bites)
'''
st.code(code, language='python')


code = '''
#過去の会社実績
import streamlit as st
import pandas as pd

#データ分析関連
df = pd.read_csv('./data/過去実績.csv', index_col='月')
dff = pd.read_csv('./data/ビール杯数過去実績.csv', index_col='月')
st.text('【過去の月ごとの飲み会回数実績】')
st.dataframe(df)
# st.table(df)
st.text('【過去の月ごとの生ビール飲酒実績】')
st.line_chart(dff)
st.text('【2023年の飲み会参加人数実績】')
st.bar_chart(df['2023年(人)'])

'''
st.code(code, language='python')


code = '''
#事前調査
import streamlit as st
import datetime

with st.form(key='comment_form'):
    #チェックボックス
    yes_no = st.checkbox('参加費は最低3,000円が必要である事に同意する')
    #スライダー
    price = st.slider('希望価格帯(スライダーを動かしてください)', min_value=3000, max_value=10000)
    name = st.text_input('【お名前(※フルネーム)】')
    family_num = st.text_input('【参加予定人数(※数字のみで可)】')
    #セレクトボックス
    choice_food = st.selectbox(
        '【希望コース】',('和食系', '洋食系', 'アジア系', '何でもよい', 'その他'))
    st.text_input("「その他」を選んだ方は希望コースがあればご記入ください")
    st.text('【ご希望日時】')
    #日付
    min_date = datetime.date(2024, 4, 20)
    max_date = datetime.date(2024, 4, 30)
    d = st.date_input('希望日(4/20~4/30)', datetime.date(2024, 4, 20), min_value=min_date, max_value=max_date)
    #ラジオボックス：時間   
    choice_day = st.radio(
        'スタート時間',('18:00', '18:30', '19:00', '19:30', '20:00'))
    #複数選択
    second_party = st.multiselect(
        '二次会の希望を確認します(※複数選択可)',
        ('居酒屋', 'バー', 'スナック', 'ラウンジ', '相席居酒屋', 'ラーメン', 'その他の夜の街', '参加しない')
    )
    #テキストボックス
    st.text('何かご意見がある方はこちらからどうぞ↓')
    comment = st.text_input('【コメント】')
    print(name)
    print(comment)
    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'{name}さんの参加を{family_num}名様で承りました。')
        st.text(f'希望日: {choice_day}')
        st.text(f'希望コース: {choice_food}')
        st.text(f'二次会: {second_party}')
    print(f"submit_btn: {submit_btn}")
    print(f"cancel_btn: {cancel_btn}")
'''
st.code(code, language='python')


code = '''
#csv　ビール杯数過去実績
月,2021年(杯),2022年(杯),2023年(杯)
4,333,332,345
5,323,354,366
6,450,400,433
7,543,525,501
8,623,650,631
9,540,520,499
10,330,350,360
11,300,280,250
12,450,420,450
1,350,333,412
2,222,267,287
3,330,400,388
'''
st.code(code, language='python')


code = '''
#csv　過去参加人数実績
月,2021年(人),2022年(人),2023年(人)
4,50,44,60
5,44,50,55
6,55,66,65
7,80,88,67
8,110,130,120
9,90,98,100
10,50,60,65
11,60,50,45
12,130,110,125
1,100,99,101
2,44,50,39
3,67,77,80
'''
st.code(code, language='python')