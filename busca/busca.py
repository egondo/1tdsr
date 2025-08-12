def busca(lista: list, valor: float) -> int:
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    
    return -1

def busca_binaria(lista: list, valor: float) -> int:
    ini = 0
    fim = len(lista) - 1
    while ini <= fim: #há elementos na lista nao verificados
        meio = (ini + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio - 1

    return -1 
