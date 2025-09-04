def criaTabuleiro():
    resp = []
    for i in range(3):
        resp.append([' '] * 3)
    return resp

def temEspaco(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == ' '
                return True
    return False