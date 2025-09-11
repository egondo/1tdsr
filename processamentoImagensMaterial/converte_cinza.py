import Imagem

def converte(red, green, blue) -> list:
    lin = len(red)
    col = len(red[0])

    #criando a matriz zerada com as mesmas dimensoes da imagem original
    resp = []
    for i in range(lin):
        resp.append([0] * col)

    for i in range(lin):
        for j in range(col):
            resp[i][j] = int(0.3 * red[i][j] + 0.59 * green[i][j] + 0.11 * blue[i][j])

    return resp

def converte_preto_branco(matriz):
    lin = len(matriz)
    col = len(matriz[0])
    resp = []
    for i in range(lin):
        resp.append([0] * col)

    threshold = 110
    for i in range(lin):
        for j in range(col):
            if matriz[i][j] < threshold:
                resp[i][j] = 0
            else:
                resp[i][j] = 255

    return resp


if __name__ == "__main__":
    img = Imagem.getMatrizImagemColorida("naturezaMorta.jpg")
    resp = converte(img[0], img[1], img[2])
    Imagem.salvaImagemCinza("naturezaCinza2.jpg", resp)

    preto_branco = converte_preto_branco(resp)
    Imagem.salvaImagemCinza("naturezaPretoBranco.jpg", preto_branco)