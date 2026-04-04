import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviws = pd.read_csv("DataBase/customer reviews.csv")
df_top100_books = pd.read_csv("DataBase/Top-100 Trending Books.csv")

book = st.sidebar.selectbox("Livro", df_reviws["book name"].unique())

# livos
df_book = df_top100_books[df_top100_books["book title"] == book]
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_author = df_book["author"].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1,col2,col3 = st.columns(3)
col1.metric("Author", book_author)
col2.metric("Rating", book_rating)
col3.metric("Year", book_year)

st.divider()
# reviws
df_reviws_f = df_reviws [df_reviws ["book name"] == book]

for row in df_reviws_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[3])
    message.write(row[5])
    message.write(row[7])
    
    st.divider()
    