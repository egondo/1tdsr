#Problema da validação
#   nota apenas com valores entre 0 <= nota <= 10

nota1 = float(input("Nota 1: "))
while nota1 < 0 or nota1 > 10:
    print("Nota inválida! Digite novamente")
    nota1 = float(input("Nota 1: "))

nota2 = float(input("Nota 2: "))
while nota2 < 0 or nota2 > 10:
    print("Nota inválida! Digite novamente")
    nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2
print(f"A media foi {media}") 