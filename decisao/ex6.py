num_a = int(input("Digite A: "))
num_b = int(input("Digite B: "))

resto = num_a % num_b
if resto == 0:
    print(f"{num_a} é divisível por {num_b}")
else:
    print(f"{num_a} não é divisível por {num_b}")

if num_a % num_b == 0:
    print(f"{num_a} é divisível por {num_b}")
else:
    print(f"{num_a} não é divisível por {num_b}")

match num_a % num_b:
    case 0:
        print(f"{num_a} é divisível por {num_b}")
    case _: #situação que não casa com nenhum case anterior
        print(f"{num_a} não é divisível por {num_b}")
