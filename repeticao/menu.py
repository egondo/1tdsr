print(" Sistem de vendas de produtos pela internet")
print("1) cadastra usuário: ")
print("2) consulta produtos: ")
print("3) adiciona produto no carrinho: ")
print("4) consulta últimas compras: ")
print("5) finaliza a compra")
print("6) sair")

opcao = int(input("Informe uma das opções acima: "))

while opcao != 6:
    if opcao == 1:
        nome = input("Nome: ")
        cpf = input("cpf: ")
    
    elif opcao == 2:
        nome = input("Informe o nome do produto: ")
        print("001\tGeladeira Frost Free")
        print("002\tNotebook Samsung")
    
    elif opcao == 3:
        prod = input("Informe o código do produto: ")
        qtd = int(input("Quantas peças deseja levar"))
    
    elif opcao == 4:
        print("Mostrando últimas 5 compras: ")
        print("Compra 1 ....")

    elif opcao == 5:
        print("Qual a forma de pagamento:")
        print(" a) Cartão\n b) Dinheiro\n c) PIX")
    elif opcao == 6:
        print("Finalizando o programa")
    else:
        print("Informe uma opção correta!")

    print(" Sistem de vendas de produtos pela internet")
    print("1) cadastra usuário: ")
    print("2) consulta produtos: ")
    print("3) adiciona produto no carrinho: ")
    print("4) consulta últimas compras: ")
    print("5) finaliza a compra")
    print("6) sair")

    opcao = int(input("Informe uma das opções acima: "))
