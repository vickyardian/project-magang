import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("MINI_TIM_B.csv")

st.set_page_config(
    page_title="Jurusan Terpopuler",
    page_icon="",
    layout="wide"
)
st.title("Jurusan Terpopuler di Program IUP")

jurusan_populer = df['JURUSAN'].value_counts().head(10).reset_index()
jurusan_populer.columns = ['JURUSAN', 'JUMLAH_PTN']

fig = px.bar(jurusan_populer, x='JUMLAH_PTN', y='JURUSAN', orientation='h', text='JUMLAH_PTN')
fig.update_traces(textposition='outside', hovertemplate='%{y}<br>Ditawarkan oleh %{x} PTN')
fig.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig)

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