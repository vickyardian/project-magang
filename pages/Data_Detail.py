import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Detail",page_icon="", layout="wide")

# Fungsi bantu untuk format rupiah
def format_rupiah(angka):
    try:
        return f"Rp{int(angka):,}".replace(",", ".")
    except:
        return "Rp0"

# Load data dengan cache agar efisien
@st.cache_data
def load_data():
    df = pd.read_csv("MINI_TIM_B.csv")
    # Bersihkan dan konversi data
    df['UKT'] = df['UKT'].replace('[Rp.,]', '', regex=True)
    df['UKT'] = pd.to_numeric(df['UKT'], errors='coerce')
    df['DAYA TAMPUNG'] = pd.to_numeric(df['DAYA TAMPUNG'], errors='coerce')
    df['UKT_RUPIAH'] = df['UKT'].apply(format_rupiah)
    return df

# Load data
df = load_data()

# Judul halaman
st.markdown(
    "<h2 style='text-align: center;'>📊 Data Program IUP</h2>",
    unsafe_allow_html=True
)

# Dropdown pilih PTN
ptn_terpilih = st.selectbox("Pilih PTN", sorted(df['PTN'].unique()))

# Filter data berdasarkan PTN terpilih
filtered = df[df['PTN'] == ptn_terpilih][['JURUSAN', 'DAYA TAMPUNG', 'UKT_RUPIAH']]

# Tampilkan tabel
st.dataframe(filtered, use_container_width=True)

# Footer agar UI bersih
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
