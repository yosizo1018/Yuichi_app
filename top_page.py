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
image = Image.open('./data/pub.png')
st.image(image, width=200)
st.text('')
#動画
st.text('イメージ動画')
video_file = open('./data/asahi_movie.mp4', 'rb')
video_bites = video_file.read()
st.video(video_bites)