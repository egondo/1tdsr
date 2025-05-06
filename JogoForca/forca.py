#incializa o jogo
erros = 0
letras_chutadas = " "
#sorteia a palavra
palavra = "The Shawshank Redemption"
segredo = ''

for c in palavra:
    if c == ' ':
        segredo = segredo + '  '
    else:
        segredo = segredo + '_ '

while erros < 6 and "_" in segredo:
    print(segredo)
    segredo = ""
    print(f"Erros: {erros}")
    print(f'Letras chutadas: {letras_chutadas}')
    letra = input("Letra: ")
    letras_chutadas = letras_chutadas + letra.lower()

    if not letra.lower() in palavra.lower():
        erros = erros + 1

    for c in palavra.lower():
        if c in letras_chutadas:
            segredo = segredo + c + " "
        else:
            segredo = segredo + "_ "

if erros >= 6:
    print(f"Voce perdeu, a palavra era {palavra}")
else:
    print(f"Parabéns, você descobriu a palavra {palavra}")

