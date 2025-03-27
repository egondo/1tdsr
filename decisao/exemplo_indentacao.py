salario = float(input("Digite o seu salário: "))

if salario < 2000:
    print("A vida está muito difícil")
    print("mas estou batalhando para melhorar!")
elif salario <= 5000:
    print("Para você a vida melhorou um pouco")
    print("pois o governo vai te liberar de pagar")
    print("o imposto de renda!")
elif salario <= 10000:
    print("Se vc não tiver filhos, acho que você vive")
    print("confortavelmente!")
else:
    print("Vc está bem encaminhado, só não fazer")
    print("nenhuma bobagem!")