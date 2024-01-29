import streamlit as st
import datetime

t1 = '参加費は最低3,000円が必要である事に同意する'
t2 = '希望価格帯(スライダーを動かしてください)'
t3 = '【お名前(※フルネーム)】'
t4 = '【参加予定人数(※数字のみで可)】'
t5 = ('和食系', '洋食系', 'アジア系', '何でもよい', 'その他')
t6 = "「その他」を選んだ方は希望コースがあればご記入ください"
t7 = '【ご希望日時】'
t8 = '希望日(4/20~4/30)'
t9 = ('18:00', '18:30', '19:00', '19:30', '20:00')
t10 = ('居酒屋', 'バー', 'スナック', 'ラウンジ', '相席居酒屋', 'ラーメン', 'その他の夜の街', '参加しない')
t11 = '何かご意見がある方はこちらからどうぞ↓'

with st.form(key='comment_form'):
    #チェックボックス
    yes_no = st.checkbox(t1)
    #スライダー
    price = st.slider(t2, min_value=3000, max_value=10000)
    name = st.text_input(t3)
    family_num = st.text_input(t4)
    #セレクトボックス
    choice_food = st.selectbox('【希望コース】',t5)
    st.text_input(t6)
    st.text(t7)
    #日付
    min_date = datetime.date(2024, 4, 20)
    max_date = datetime.date(2024, 4, 30)
    d = st.date_input(t8, datetime.date(2024, 4, 20), min_value=min_date, max_value=max_date)
    #ラジオボックス：時間   
    choice_day = st.radio('スタート時間',t9)
    #複数選択
    second_party = st.multiselect( '二次会の希望を確認します(※複数選択可)',t10)
    #テキストボックス
    st.text(t11)
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