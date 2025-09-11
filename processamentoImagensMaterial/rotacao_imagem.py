import Imagem

def gira90(matriz: list) -> list:
    lin = len(matriz)
    col = len(matriz[0])

    #criando a matriz rotacionada vazia
    rotacao = []
    for i in range(col):
        rotacao.append([0] * lin)    
    
    for i in range(lin):
        for j in range(col):
            rotacao[j][lin - i - 1] = matriz[i][j]

    return rotacao


if __name__ == "__main__":
    imagem = Imagem.getMatrizImagemCinza("domino.png")
    resp = gira90(imagem)
    Imagem.salvaImagemCinza("domino_girado.png", resp)
    