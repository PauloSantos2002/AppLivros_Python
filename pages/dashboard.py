import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
df_reviws = pd.read_csv("DataBase/customer reviews.csv")
df_top100_books = pd.read_csv("DataBase/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

number = st.sidebar.slider("Valor", price_min, price_max, price_max)

"# Dashboard"
"Tabela dos top 100 livros"
df_books = df_top100_books[(df_top100_books["book price"] < number)]
df_books

"# Graficos"
col1, col2 = st.columns(2)
col1.bar_chart(df_books["year of publication"])
col2.line_chart(df_books["book price"])

