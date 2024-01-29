import streamlit as st
import pandas as pd

#データ分析関連
df = pd.read_csv('./data/achievement.csv', index_col='月')
dff = pd.read_csv('./data/number_of_beers.csv', index_col='月')
st.text('【過去の月ごとの飲み会回数実績】')
st.dataframe(df)
# st.table(df)
st.text('【過去の月ごとの生ビール飲酒実績】')
st.line_chart(dff)
st.text('【2023年の飲み会参加人数実績】')
st.bar_chart(df['2023年(回)'])
