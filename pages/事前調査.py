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