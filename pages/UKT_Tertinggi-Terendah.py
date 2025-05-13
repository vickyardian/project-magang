import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("MINI_TIM_B.csv")

# Bersihkan dan konversi kolom UKT ke numerik
df['UKT'] = df['UKT'].replace('[^0-9]', '', regex=True)  # Hapus karakter non-angka
df['UKT'] = pd.to_numeric(df['UKT'], errors='coerce')    # Konversi ke angka

st.title("UKT Tertinggi dan Terendah")
st.subheader("7 Prodi dengan UKT Tertinggi dari PTN Berbeda")

# Data UKT tertinggi
ukt_termahal = df.loc[df.groupby('PTN')['UKT'].idxmax()].dropna()
ukt_termahal_top = ukt_termahal.sort_values('UKT', ascending=False).head(7)
ukt_termahal_top['LABEL'] = ukt_termahal_top['PTN'] + " - " + ukt_termahal_top['JURUSAN']

# Grafik UKT tertinggi
fig1 = px.bar(ukt_termahal_top[::-1], x='UKT', y='LABEL', orientation='h', title='UKT Tertinggi', text='UKT')
fig1.update_traces(texttemplate='Rp %{x:,.0f}', textposition='outside')
fig1.update_layout(
    xaxis_tickformat=',',
    xaxis_title='UKT (Rp)',
    yaxis_title=None,
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig1)

st.subheader("7 Prodi dengan UKT Terendah dari PTN Berbeda")

# Data UKT terendah
ukt_termurah = df.loc[df.groupby('PTN')['UKT'].idxmin()].dropna()
ukt_termurah_top = ukt_termurah.sort_values('UKT').head(7)
ukt_termurah_top['LABEL'] = ukt_termurah_top['PTN'] + " - " + ukt_termurah_top['JURUSAN']

# Grafik UKT terendah
fig2 = px.bar(ukt_termurah_top, x='UKT', y='LABEL', orientation='h', title='UKT Terendah', text='UKT')
fig2.update_traces(texttemplate='Rp %{x:,.0f}', textposition='outside')
fig2.update_layout(
    xaxis_tickformat=',',
    xaxis_title='UKT (Rp)',
    yaxis_title=None,
    plot_bgcolor='rgba(0,0,0,0)'
)

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