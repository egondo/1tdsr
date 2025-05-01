n = float(input("Digite o valor de n: "))

x = 0.00001
while x * x < n:
    x = x + 0.0000001


print(f"Raiz quadrade de {n} é {x}")