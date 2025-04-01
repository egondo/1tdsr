num = int(input("Informe um número: "))

resto = num % 2
match resto:
    case 0:
        print(f"{num} é par")
    case 1:
        print(f"{num} é ímpar")
        