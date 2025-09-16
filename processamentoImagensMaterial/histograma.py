import Imagem

#Gere uma borda mais escura nos retangulos que representam
#os valores do histograma.

def cria_retangulo(imagem: list, altura: int, col: int):
    cor = 150
    for i in range(altura):
        for j in range(50):
            imagem[i + 20][j + col] = cor


imagem = []
for i in range(500):
    imagem.append([255] * 700)
valores = [13, 33, 84, 76, 147, 231, 95, 73, 23, 27]
inicio = 40
delta = 60
for valor in valores:
    cria_retangulo(imagem, valor * 2, inicio)
    inicio = inicio + delta

lin_ini = 0
lin_fin = len(imagem) - 1
while lin_ini < lin_fin:
    aux = imagem[lin_ini]
    imagem[lin_ini] = imagem[lin_fin]
    imagem[lin_fin] = aux
    lin_ini = lin_ini + 1
    lin_fin = lin_fin - 1


Imagem.salvaImagemCinza("histograma.png", imagem)        

