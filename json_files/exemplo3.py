import json

colecao = [
    {"autor": ["Walter Leighton"], "titulo": 'Equações diferenciais ordinárias',
    "editora": "LTC", 'ano': 1963},

    {"autor": ["Pedro Morettin", "Wilton Bussab"], "titulo": "Estatística Básica", 
    "editora": "Atual", "ano": 1984},

    {"autor": ["Daniel Defoe"], "titulo": 'Robinson Crusoé', 
    "editora": "Círculo do Livro", "ano": 1719}
]   

with open("livros.json", mode="w") as file:
    json.dump(colecao, file)


with open("livros.json", mode="r") as arq:
    info = json.load(arq)

for livro in info:
    print(livro)