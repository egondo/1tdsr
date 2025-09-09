import velha

mat = velha.criaTabuleiro()
jogador = 'X'

while velha.temEspaco(mat) and not velha.haGanhador(mat):
    velha.imprime(mat)
    print(f'Vez do jogador {jogador}')
    lin = int(input("Linha: "))
    col = int(input("Coluna: "))

    if velha.joga(mat, lin, col, jogador) == True:
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'


velha.imprime(mat)
if velha.haGanhador(mat):
    print("Teve um ganhador, parabéns!")
else:
    print("Deu empate!")