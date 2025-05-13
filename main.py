import streamlit as st

st.set_page_config(
    page_title="Beranda",
    page_icon="🏠",
    layout="wide"
)

# Sembunyikan menu default Streamlit (opsional)
hide_menu = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# Konten utama beranda
st.markdown("<h1 style='text-align: center;'>🎓 Selamat Datang di Dashboard Analisis Program IUP di PTN</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Temukan informasi UKT, Daya Tampung, dan Jurusan dari berbagai Perguruan Tinggi Negeri di Indonesia.</h4>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=300)
with col2:
    st.markdown("""
        ### 👋 Fitur yang tersedia:
        - Visualisasi UKT per jurusan di setiap PTN
        - Distribusi daya tampung
        - Tampilan detail data dari Jurusan, UKT, dan Daya Tampung
        - Antarmuka interaktif dengan Streamlit + Plotly

        ---
        📁 Akses fitur-fitur di sidebar kiri.
    """)

