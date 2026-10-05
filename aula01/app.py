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

livro_mais_caro, maior_preco = dados.encontrar_livro_mais_caro(livros)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de livros", qtd_livros)
col2.metric("Preço médio", f"£ {preco_medio:.2f}")
col3.metric("Qntd livros 5 estrelas", cinco_estrelas)
col4.metric(
    "Livro mais caro",
    f"£ {maior_preco:.2f}",
    livro_mais_caro["titulo"],
    delta_color="off",
    delta_arrow="off",
)

st.dataframe(livros)
