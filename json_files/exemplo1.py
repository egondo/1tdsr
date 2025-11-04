import json

serie = {
    "titulo": "O Tunel do Tempo", "ano": 1966, 
    "titulo_original": "The Time Tunnel",
    "genero": ["ação", "aventura", "ficção científica"],
    "atores": ["James Darren", "Robert Colbert"],
    "criador": "Irwin Allen"
}

with open('dados.json', mode="w", encoding="latin1") as arquivo:
    json.dump(serie, arquivo, indent=4)

