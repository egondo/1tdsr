frase = input("Digite um texto: ")
letra = input("Informe um único caracter: ")
#faça a validação da letra para que seja apenas um único caracter

#resultado = frase.replace(letra, '*')

resultado = ""
for caracter in frase:
    #print(caracter)
    if caracter == letra or caracter == letra.capitalize():
        resultado = resultado + '*'
    else:
        resultado = resultado + caracter

print(resultado)
