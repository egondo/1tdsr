rm = int(input("Informe o RM: "))
soma = 0

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

resto = rm % 10
soma = soma + resto
rm = rm // 10

print(soma)