num = float(input("Numero: "))

#Não funciona quando tenho um intervalo de números.
if num < 0:
    num = -1
elif num > 0:
    num = 1

match num:
    case -1:
        print("É negativo")
    case 1:
        print("É positivo")
    case _:
        print("É 0")