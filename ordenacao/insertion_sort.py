def organiza(lista: list, pos: int):
    aux = lista[pos]
    while pos > 0 and lista[pos-1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1
    
    lista[pos] = aux

def insertion_sort(lista: list):
    for i in range(1, len(lista)):
        organiza(lista, i)

#conj = [2, 6, 18, 22, 39, 48, 65, 89, 1]    
#conj = [6, 4]    
conj = [4, 6, -1, 5, 2, 3, 4, 10, 8, 20, 17]
insertion_sort(conj)
print(conj)