import Imagem

img = Imagem.getMatrizImagemCinza("wallpaper.png")
num_linhas = len(img)
num_colunas = len(img[0])

print(f"{num_linhas} X {num_colunas}")

for i in range(len(img)):
    for j in range(len(img[0])):
        img[i][j] = img[i][j] - 50

Imagem.salvaImagemCinza("folha_rosto.png", img)