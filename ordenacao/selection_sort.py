def menor(v: list, i: int) -> int:
    ind_menor = i
    while i < len(v):
        if v[ind_menor] > v[i]:
            ind_menor = i
        i = i + 1

    return ind_menor    

def sort(lista: list):

    ind = menor(lista, 0)
    aux = lista[0]
    lista[0] = lista[ind]
    lista[ind] = aux

    ind = menor(lista, 1)
    aux = lista[1]
    lista[1] = lista[ind]
    lista[ind] = aux

if __name__ == "__main__":
    lst = [5, 4, -2, 10, 7, 40]
    sort(lst)
    print(lst)