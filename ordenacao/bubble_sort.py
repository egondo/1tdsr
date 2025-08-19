def subir(lista: list, pos: int):
    i = len(lista) - 1
    while i > pos:
        if lista[i] < lista[i-1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        i = i - 1

def sort(lista: list):
    for i in range(len(lista) - 1):
        subir(lista, i)

if __name__ == "__main__":
    lst = [3, 6, 9, -1, 5, 10, 34, 23, 18]
    #subir(lst, 0)
    sort(lst)
    print(lst)        