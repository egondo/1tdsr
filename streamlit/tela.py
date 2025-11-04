import streamlit as st


st.header('Cadastro de série:')

titulo = st.text_input("Título")

escolhas = st.radio("Gênero", ['ação', 'aventura', 'comédia', 'drama', 'guerra', 'suspense', 'terror', 'ficção científica', 'fantasia', 'outros'])

atores = st.text_area("atores: ")

temporadas = st.selectbox("Temporadas: ", [1, 2, 3, 4, 5, 6, '7 em diante'])

if st.button('cadastra'):
    registro = {
        "titulo": titulo,
        "generos": escolhas,
        "atores": atores,
        "temporadas": temporadas
    }
    st.write(registro)



