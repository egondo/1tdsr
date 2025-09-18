try:
    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    c = a / b

except ValueError as erro:
    print(erro)
    print("Valor inválido de numeros")

except ZeroDivisionError as erro2:
    print(erro2)
    print("Vc tentou dividir por zero")

else:
    print(f"Resultado: {c}")

