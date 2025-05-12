import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib.ticker import FuncFormatter

# Fungsi untuk format rupiah
def format_rupiah(angka):
    return f"Rp{int(angka):,}".replace(",", ".")

# Load dan bersihkan data
@st.cache_data
def load_data():
    df = pd.read_csv('MINI_TIM_B.csv')
    df['UKT'] = df['UKT'].replace('[Rp.,]', '', regex=True).astype(float)
    df['DAYA TAMPUNG'] = pd.to_numeric(df['DAYA TAMPUNG'], errors='coerce')
    df['UKT_RUPIAH'] = df['UKT'].apply(format_rupiah)
    return df

# Load data
df = load_data()

st.title("Analisis Program IUP di PTN")

# 1. Jumlah PTN dan daftar jurusan per PTN
jumlah_ptn = df['PTN'].nunique()
st.subheader(f"Jumlah PTN yang mempunyai program IUP: {jumlah_ptn}")

st.subheader("Daftar PTN dan jumlah jurusan masing-masing:")
jurusan_per_ptn = df.groupby('PTN')['JURUSAN'].nunique()
st.write(jurusan_per_ptn.sort_index())

# 2. Visualisasi daya tampung per prodi dalam satu PTN
st.subheader("Distribusi Daya Tampung per Prodi dalam PTN Terpilih")

ptn_daya = st.selectbox("Pilih PTN untuk visualisasi daya tampung", sorted(df['PTN'].unique()), key='daya')
data_daya = df[df['PTN'] == ptn_daya][['JURUSAN', 'DAYA TAMPUNG']].dropna()

fig3 = px.pie(
    data_daya,
    values='DAYA TAMPUNG',
    names='JURUSAN',
    title=f'Distribusi Daya Tampung Prodi di {ptn_daya}',
    hole=0.3  # Untuk tampilan seperti donut chart 
)
fig3.update_traces(textinfo='label+value', hovertemplate='%{label}<br>Daya Tampung: %{value:,}')
st.plotly_chart(fig3)

# 3. Visualisasi UKT per prodi dalam satu PTN 
st.subheader("Distribusi UKT per Prodi dalam PTN Terpilih")

ptn_ukt = st.selectbox("Pilih PTN untuk visualisasi UKT", sorted(df['PTN'].unique()), key='ukt')
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
st.plotly_chart(fig4)

# 4. Memilih PTN dan lihat jurusan
st.subheader("Detail jurusan, daya tampung, dan UKT per PTN")
ptn_terpilih = st.selectbox("Pilih PTN", sorted(df['PTN'].unique()))
filtered = df[df['PTN'] == ptn_terpilih][['JURUSAN', 'DAYA TAMPUNG', 'UKT_RUPIAH']]
st.dataframe(filtered)

# 5. Visualisasi UKT tertinggi dari nilai tertinggi ke terendah 
st.subheader("7 Prodi dengan UKT Tertinggi dari PTN Berbeda")

ukt_termahal = df.loc[df.groupby('PTN')['UKT'].idxmax()][['PTN', 'JURUSAN', 'UKT']]
ukt_termahal_top = ukt_termahal.sort_values('UKT', ascending=False).head(7)

# Balik urutan agar tertinggi di atas
ukt_termahal_top = ukt_termahal_top[::-1]

fig1 = px.bar(
    ukt_termahal_top,
    x='UKT',
    y='PTN',
    color='JURUSAN',
    orientation='h',
    title='7 Prodi dengan UKT Termahal dari PTN',
    text='UKT'
)
fig1.update_traces(
    hovertemplate='%{y}<br>%{customdata[0]}<br>UKT: Rp %{x:,.0f}',
    customdata=ukt_termahal_top[['JURUSAN']],
    texttemplate='Rp %{x:,.0f}',
    textposition='outside'
)
fig1.update_layout(
    xaxis_tickformat=',',
    xaxis=dict(tickprefix='Rp ')
)
st.plotly_chart(fig1)

# 6. Visualisasi daya tampung tertinggi dari nilai tertinggi ke terendah
st.subheader("7 Prodi dengan Daya Tampung Terbanyak dari PTN Berbeda")

daya_terbanyak = df.loc[df.groupby('PTN')['DAYA TAMPUNG'].idxmax()][['PTN', 'JURUSAN', 'DAYA TAMPUNG']]
daya_terbanyak_top = daya_terbanyak.sort_values('DAYA TAMPUNG', ascending=False).head(7)

# Balik urutan agar tertinggi di atas
daya_terbanyak_top = daya_terbanyak_top[::-1]

fig2 = px.bar(
    daya_terbanyak_top,
    x='DAYA TAMPUNG',
    y='PTN',
    color='JURUSAN',
    orientation='h',
    title='7 Prodi dengan Daya Tampung Terbanyak dari PTN',
    text='DAYA TAMPUNG'
)
fig2.update_traces(
    hovertemplate='%{y}<br>%{customdata[0]}<br>Daya Tampung: %{x}',
    customdata=daya_terbanyak_top[['JURUSAN']],
    textposition='outside'
)
st.plotly_chart(fig2)
