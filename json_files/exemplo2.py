import json

with open('dados.json', mode="r") as arq:
    info = json.load(arq)

print(info)
print(type(info))
print(info['genero'])

