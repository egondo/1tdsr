def insereOrdenado(x: int, lista: list):
    i = 0
    while i < len(lista) and lista[i] < x:
        i = i + 1
    lista.insert(i, x)


#programa principal
conjunto = [-5, 0, 10, 12, 22, 47]
valor = 60
insereOrdenado(valor, conjunto)
print(conjunto)
