def busca(lista, valor, posicao) -> int:
    while posicao < len(lista) and lista[posicao] != valor:
        posicao = posicao + 1
    
    if posicao == len(lista):
        return -1
    else:
        return posicao
    

def busca_par(lista: list, soma: int):
    i = 0
    while i < len(lista):
        comp = soma - lista[i]
        resp = busca(lista, comp, i)
        if resp != -1:
            print(f"({lista[i]}, {lista[resp]})")
        i = i + 1

if __name__ == "__main__":
    lista = [2, 5, -7, 9, 3, 10, 15, 6]
    busca_par(lista, 11)
    