
num = int(input('Informe o número: '))
soma = 0
while num != 0:
    #print(num)
    if num % 2 == 0:
        soma = soma + num
    num = int(input('Informe o número: '))

print(f"A soma dos pares vale {soma}")

#while num != 0:
#    num = int(input("Informe o número: "))
#    print(num)
