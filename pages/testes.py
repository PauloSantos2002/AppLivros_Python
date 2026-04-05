import streamlit as st
import numpy as np
import pandas as pd

"# Calculadora Streamlit"

num1 = st.number_input(
    "Digite o primeiro valor",
    placeholder="1º",
    format="%0f"    
)
num2 = st.number_input(
    "Digite o segundo valor",
    placeholder="2º",
    format="%0f"    
)

col = st.columns(4)

with col[0]:
    if st.button("Soma", use_container_width=True):
        resultado = num1 + num2
        st.write(f"{resultado}") 
with col[1]:
    if st.button("Subtração", use_container_width=True):
        resultado = num1 - num2
        st.write(f"{resultado}") 
with col[2]:
    if st.button("divisão", use_container_width=True):
        resultado = num1 / num2
        st.write(f"{resultado}") 
with col[3]:
    if st.button("Multiplicação", use_container_width=True):
        resultado = num1 * num2
        st.write(f"{resultado}") 
        
"-"*30
"# Dados e graficos"
"## Gereando e exibindo dados aleatorios"
#-- gerando o DataFrame
df = pd.DataFrame(
    np.random.randn(10,3),
    columns=["a","b","c"]
)

"### Dataframe aleatório"
st.dataframe(df)

col = st.columns(2)
col[0].bar_chart(df)
col[1].line_chart(df)

"-"*30

st.subheader("Carregar arquivo CSV")
upload = st.file_uploader(
    "Escolha um arquivo CSV",
    "CSV"
)


if upload is not None:
    try:
        # -- Mostrar um pedaço do arquivo -- #
        df_upload = pd.read_csv(upload)
        st.success("Arquivo carregado com sucesso")
        df_upload
    except Exception as e:
        st.error(f"Falha ao carregar o arquivo, erro{e}")