import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Distribusi UKT dan Daya Tampung",page_icon="", layout="wide")

# Fungsi bantu format rupiah
def format_rupiah(angka):
    try:
        return f"Rp{int(angka):,}".replace(",", ".")
    except:
        return "Rp0"

# Fungsi untuk load dan bersihkan data
@st.cache_data
def load_data():
    df = pd.read_csv("MINI_TIM_B.csv")

    # Bersihkan dan ubah tipe data
    df['UKT'] = df['UKT'].replace('[Rp.,]', '', regex=True)
    df['UKT'] = pd.to_numeric(df['UKT'], errors='coerce')
    df['DAYA TAMPUNG'] = pd.to_numeric(df['DAYA TAMPUNG'], errors='coerce')
    df['UKT_RUPIAH'] = df['UKT'].apply(format_rupiah)

    return df

# Load data
df = load_data()

# Judul halaman
st.markdown("<h2 style='text-align: center;'>📈 Analisis Distribusi UKT dan Daya Tampung per Prodi</h2>", unsafe_allow_html=True)

# ----------------------------
# Visualisasi UKT per PTN
# ----------------------------
st.subheader("Distribusi UKT per Prodi dalam PTN")

ptn_ukt = st.selectbox("Pilih PTN untuk UKT", sorted(df['PTN'].unique()), key='ukt')
data_ukt = df[df['PTN'] == ptn_ukt][['JURUSAN', 'UKT']].dropna().sort_values('UKT', ascending=False)

fig4 = px.bar(
    data_ukt,
    x='UKT',
    y='JURUSAN',
    orientation='h',
    title=f'UKT Tiap Prodi di {ptn_ukt}',
    labels={'UKT': 'UKT (Rupiah)', 'JURUSAN': 'Prodi'},
    text='UKT'
)
fig4.update_traces(
    hovertemplate='%{y}<br>UKT: Rp %{x:,.0f}',
    texttemplate='Rp %{x:,.0f}',
    textposition='outside'
)
fig4.update_layout(
    xaxis_tickformat=',',
    xaxis=dict(tickprefix='Rp ')
)
st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# Visualisasi Daya Tampung per PTN
# ----------------------------
st.subheader("Distribusi Daya Tampung per Prodi dalam PTN")

ptn_daya = st.selectbox("Pilih PTN untuk Daya Tampung", sorted(df['PTN'].unique()), key='daya')
data_daya = df[df['PTN'] == ptn_daya][['JURUSAN', 'DAYA TAMPUNG']].dropna().sort_values('DAYA TAMPUNG', ascending=False)

fig3 = px.pie(
    data_daya,
    values='DAYA TAMPUNG',
    names='JURUSAN',
    title=f'Distribusi Daya Tampung Prodi di {ptn_daya}',
    hole=0.3
)
fig3.update_traces(
    textinfo='label+value',
    hovertemplate='%{label}<br>Daya Tampung: %{value:,}'
)
st.plotly_chart(fig3, use_container_width=True)

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
