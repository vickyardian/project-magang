import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("MINI_TIM_B.csv")
df_sorted = df.sort_values("DAYA TAMPUNG", ascending=False)

st.set_page_config(
    page_title="Daya Tampung",
    page_icon="",
    layout="wide"
)
st.title("Daya Tampung Tertinggi dan Terendah")

st.subheader("7 Prodi dengan Daya Tampung Terbanyak dari PTN Berbeda")
daya_terbanyak = df_sorted.loc[df_sorted.groupby("PTN")["DAYA TAMPUNG"].idxmax()].drop_duplicates("PTN")
fig = px.bar(daya_terbanyak.head(7), x="DAYA TAMPUNG", y="PTN", color="JURUSAN", orientation="h")
fig.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig)

st.subheader("7 Prodi dengan Daya Tampung Terkecil dari PTN Berbeda")
daya_terkecil = df_sorted.loc[df_sorted.groupby("PTN")["DAYA TAMPUNG"].idxmin()].drop_duplicates("PTN")
fig2 = px.bar(daya_terkecil.head(7), x="DAYA TAMPUNG", y="PTN", color="JURUSAN", orientation="h")
fig2.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig2)

# ----------------------------
# Footer agar UI bersih
# ----------------------------
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)