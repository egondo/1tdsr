notas = {}

#RM de um aluno
notas[462843] = 7.0
notas[643453] = 8.0
notas[23422] = 6.8

notas['Alexandre Cruz'] = 9.5

if 'Carla Soares' in notas:
    print("Sim, ela esta")
    print(notas['Carla Soares'])
else:
    print("Carla Soares nao esta no dicionario")

for chave in notas.keys():
    print(f'{chave} -> {notas[chave]}')