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