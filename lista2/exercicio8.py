idade = int(input("Informe a idade do atleta: "))

if idade >= 5 and idade <= 7:
    print("Categoria infantil")

if idade >= 8 and idade <= 10:
    print("Categoria juvenil")

if idade >= 11 and idade <=15:
    print("Categoria adolescente")

if idade >= 16 and idade <= 30:
    print("Categoria adulto")

if idade > 30:
    print("Categoria senior")
    