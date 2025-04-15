#Resolver o problema 4.5 e mostrar todos os números que são somados.

n = int(input("Digite n: "))
soma = 0

i = 1
texto = ""

while i <= n:
    soma = soma + i
    if i < n:
        texto = texto + str(i) + " + "
    else:
        texto = texto + str(i)
    i = i + 1

print(f"{texto} = {soma}")
