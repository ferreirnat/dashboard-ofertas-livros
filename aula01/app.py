"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")

livros = dados.ler_livros_v4()

qtd_livros = len(livros)

preco_medio = dados.calcular_preco_medio(livros)

cinco_estrelas = dados.contar_cinco_estrelas(livros)

col1, col2, col3 = st.columns(3)
col1.metric("Total de livros", qtd_livros)
col2.metric("Preço médio", f"£ {preco_medio:.2f}")
col3.metric("Qntd livros 5 estrelas", cinco_estrelas)

st.dataframe(livros)
