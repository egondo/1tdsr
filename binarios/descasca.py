#Vamos descascar os dígitos de um número


numero = int(input("Digite um número: "))
backup = numero

while numero != 0:
    resto = numero % 10
    numero = numero // 10
    print(resto)