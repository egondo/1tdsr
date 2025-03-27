#ler 2 números e uma string representando um operador

num1 = float(input("Digite o 1º numero"))
op = input("Digite a operacao (+-/*): ")
num2 = float(input("Digite o 2º numero: "))

if op == '+':
    resultado = num1 + num2

elif op == '-':
    resultado = num1 - num2

elif op == '*':
    resultado = num1 * num2

elif op == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Impossivel fazer divisao por 0")
        resultado = None

else:
    print("Operador invalido!")
    resultado = None

if resultado != None:
    print(f"Resposta: {num1} {op} {num2} = {resultado:.5f}")