#Calculo do INSS
salario = float(input("Salario: "))

if salario <= 1693.72:
    inss = salario * 0.08

if salario > 1693.72 and salario <= 2822.90:
    inss = salario * 0.09

if salario > 2822.90 and salario <= 5645.80:
    inss = salario * 0.11

if salario > 5645.80:
    inss = 5645.80 * 0.11

print(f"A contribuição do inss é de R$ {inss}")