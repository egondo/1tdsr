import streamlit as st


st.header('Cadastro de série:')

titulo = st.text_input("Título")

st.subheader("Gêneros: ")
valor = st.checkbox('ação', key="acao")
av = st.checkbox("aventura", key="aventura")
com = st.checkbox("comédia", key="comédia")
drama = st.checkbox("drama", key="drama")
guerra = st.checkbox("guerra", key="guerra")

#, 'aventura', 'comédia', 'drama', 'guerra', 'suspense', 'terror', 'ficção científica', 'fantasia', 'outros'])

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
    with open("dados.txt", mode="a") as arq:
        json.dump(registro, input, indent=4)



