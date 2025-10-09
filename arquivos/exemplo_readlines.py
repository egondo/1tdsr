with open('index.html', mode='r') as arq:
    lista = arq.readlines()


for i, registro in enumerate(lista, start=1):
    print(f"linha {i} -> {registro}")    

with open('nomes.txt', mode='r') as file:
    nomes = file.readlines()

print(nomes)