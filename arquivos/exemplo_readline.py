with open('nomes.txt', mode='r') as arq:

    nome = arq.readline()
    while len(nome) > 0:
        nome = nome.replace('\n', '')
        print(f"INSERT INTO pessoa(nome) values('{nome}');")
        nome = arq.readline()


