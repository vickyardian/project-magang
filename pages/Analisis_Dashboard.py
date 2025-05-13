import streamlit as st
import pandas as pd

df = pd.read_csv("MINI_TIM_B.csv")

st.set_page_config(
    page_title="Dashboard IUP PTN",
    page_icon="",
    layout="wide"
)

st.markdown("<h1 style='text-align: center;'>Dashboard Analisis Program IUP di PTN</h1>", unsafe_allow_html=True)

jumlah_ptn = df['PTN'].nunique()
st.subheader(f"Jumlah PTN yang mempunyai program IUP: {jumlah_ptn}")

st.subheader("Daftar PTN dan jumlah jurusan masing-masing:")
jurusan_per_ptn = df.groupby('PTN')['JURUSAN'].nunique()
st.write(jurusan_per_ptn.sort_index())

st.markdown("---")
st.info("Gunakan sidebar untuk menavigasi ke halaman visualisasi lainnya.")

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