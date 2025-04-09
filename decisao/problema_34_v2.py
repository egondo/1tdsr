#Calculo do INSS
salario = float(input("Salario: "))

if salario <= 1693.72:
    inss = salario * 0.08
elif salario <= 2822.90:
    inss = salario * 0.09
elif salario <= 5645.80:
    inss = salario * 0.11
elif salario > 5645.80:
    inss = 5645.80 * 0.11

print(f"A contribuição do inss é de R$ {inss}")