# 📚 AppLivros_Python

Aplicação web interativa desenvolvida com Streamlit para visualização e análise de livros e avaliações.

## 🚀 Sobre o Projeto

O **AppLivros_Python** é um sistema que permite:

- Visualizar os 100 livros mais populares
- Filtrar livros por preço
- Analisar dados com gráficos interativos
- Consultar detalhes de um livro específico
- Ler avaliações de usuários

Tudo isso através de uma interface web simples e intuitiva.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Streamlit
- Pandas
- Plotly

---

## 📊 Funcionalidades

### 📈 Dashboard de Livros (`top100.py`)

- Filtro de livros por preço (slider)
- Tabela dinâmica dos livros
- Gráfico de:
  - 📅 Ano de publicação
  - 💰 Preço dos livros

### 📖 Página de Detalhes (`book_reviews.py`)

- Seleção de livro via sidebar
- Exibição de:
  - Autor
  - Gênero
  - Nota (rating)
  - Ano de publicação
- Lista de avaliações dos usuários em formato de chat

---

## 📁 Estrutura do Projeto

AppLivros_Python/
- │
- ├── DataBase/
- │ ├── customer reviews.csv
- │ └── Top-100 Trending Books.csv
- │
- ├── top100.py
- ├── book_reviews.py
- ├── requirements.txt
- └── README.md


---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/PauloSantos2002/AppLivros_Python.git
cd AppLivros_Python

2. Instale as dependências
pip install -r requirements.txt

3. Execute o projeto
streamlit run top100.py
