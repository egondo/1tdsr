try:
    lista = [7, 3, 0, -1]
    salario = float(input("Digite o salario: "))

    x = int(input("Digite x: "))
    if x == 0:
        resultado = x + 1

    print(resultado)
    pos = int(input("Digite posicao da lista: "))
    print(lista[pos])
except Exception as erro:
    print(erro)