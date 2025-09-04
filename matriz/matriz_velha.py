#criando uma matriz 3x3
tab = []
for i in range(3):
    tab.append([' '] * 3)

tab[0][2] = 'X'
tab[1][0] = 'O'
tab[1][1] = 'X'
tab[2][0] = 'O'

#imprimindo a matriz
for lin in tab:
    print(lin)
