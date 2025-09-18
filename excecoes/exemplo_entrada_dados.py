digitou_numero = False

while not digitou_numero:
    try:
        num = int(input("Num: "))
    except ValueError as erro:
        print("Digite um numero correto!")
    else:
        digitou_numero = True

print(num)
