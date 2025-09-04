def produto_escalar(matA: list, lin, matB: list, col):
    qtd_num = len(matA[lin])
    soma = 0
    i = 0
    while i < qtd_num:
        soma = soma + matA[lin][i] * matB[i][col]
        i = i + 1
    return soma

def multiplicacao(matA, matB):
    linA = len(matA) #qtd de linhas da matriz A
    colB = len(matB[0]) #qtd de colunas da matriz B

    result = [] #matriz resultado
    #criando a matriz resultado com as 
    #dimensoes apropriadas
    for i in range(linA):
        result.append([0] * colB)

    for i in range(linA):
        for j in range(colB):
            result[i][j] = produto_escalar(matA, i, matB, j)
            
    return result



if __name__ == "__main__":
    matriz_a = [
        [3, 2, 1],
        [4, -1, 0]
    ]

    matriz_b = [
        [4, 0, 2, 1],
        [-1, 3, 1, -1],
        [1, 1, 7, 2]
    ]

    #x = produto_escalar(matriz_a, 0, matriz_b, 0)
    #print(x)
    prod = multiplicacao(matriz_a, matriz_b)
    for lin in prod:
        print(lin)