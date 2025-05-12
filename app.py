import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# 2. Dropdown untuk memilih PTN dan lihat jurusan
st.subheader("Detail jurusan, daya tampung, dan UKT per PTN")
ptn_terpilih = st.selectbox("Pilih PTN", sorted(df['PTN'].unique()))
filtered = df[df['PTN'] == ptn_terpilih][['JURUSAN', 'DAYA TAMPUNG', 'UKT_RUPIAH']]
st.dataframe(filtered)

# 3. Visualisasi UKT tertinggi
st.subheader("7 Prodi dengan UKT Tertinggi dari PTN Berbeda")
ukt_termahal = df.loc[df.groupby('PTN')['UKT'].idxmax()][['PTN', 'JURUSAN', 'UKT']]
ukt_termahal_top = ukt_termahal.sort_values('UKT', ascending=False).head(7)

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=ukt_termahal_top.sort_values('UKT', ascending=True),
    x='UKT', y='PTN', hue='JURUSAN', dodge=False, ax=ax1, palette='tab10'
)
ax1.set_title('7 Prodi dengan UKT Termahal dari PTN')
ax1.set_xlabel('UKT (Rupiah)')
ax1.set_ylabel('PTN')
ax1.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'Rp {x:,.0f}'.replace(",", ".")))
ax1.grid(True, axis='x')
fig1.tight_layout()
st.pyplot(fig1)

# 4. Visualisasi daya tampung tertinggi
st.subheader("7 Prodi dengan Daya Tampung Terbanyak dari PTN Berbeda")
daya_terbanyak = df.loc[df.groupby('PTN')['DAYA TAMPUNG'].idxmax()][['PTN', 'JURUSAN', 'DAYA TAMPUNG']]
daya_terbanyak_top = daya_terbanyak.sort_values('DAYA TAMPUNG', ascending=False).head(7)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=daya_terbanyak_top.sort_values('DAYA TAMPUNG', ascending=True),
    x='DAYA TAMPUNG', y='PTN', hue='JURUSAN', dodge=False, ax=ax2, palette='Set2'
)
ax2.set_title('7 Prodi dengan Daya Tampung Terbanyak dari PTN')
ax2.set_xlabel('Daya Tampung')
ax2.set_ylabel('PTN')
ax2.grid(True, axis='x')
fig2.tight_layout()
st.pyplot(fig2)

st.markdown("---")
st.caption("Dibuat dengan Streamlit oleh Vicky Ardiansyah")
