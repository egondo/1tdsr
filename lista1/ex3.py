nome = input("Digite o nome: ")
aux = input("Digite o ano de nascimento: ")

#convertendo aux para número inteiro
ano = int(aux)

idade = 2025 - ano

print(nome, "tem ou terá", idade, "anos")