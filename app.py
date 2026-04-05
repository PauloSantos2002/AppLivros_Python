import streamlit as st
import pandas as pd
import plotly.express as px

col = st.columns(3)
with col[1]:
    st.markdown("<h2 style='text-align: center;'>Dashboard Livros</h2>", unsafe_allow_html=True)
    st.image("assets/pilha_de_livros.png", use_container_width=True)