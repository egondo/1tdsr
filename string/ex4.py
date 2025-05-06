frase = input("Digite um texto: ")
letras = input("Informe um conjunto de letras: ")

resultado = ""
for caracter in frase:
    #print(caracter)
    if caracter in letras or caracter in letras.upper():
        resultado = resultado + '*'
    else:
        resultado = resultado + caracter
print(resultado)
