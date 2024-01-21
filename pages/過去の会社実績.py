import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
# #matplotlibを使用したグラフ --うまくできない--
# fig, ax = plt.subplots()
# ax.plot(dff.index, dff['2023年(杯)'])
# ax.set_title('mat_dayo')
# st.pyplot(fig)