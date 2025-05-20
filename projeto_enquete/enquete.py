def cadastra_pergunta(repositorio: list):
    numero = int(input("Número: "))
    enunciado = input("Enunciado: ")
    tipo = input("Tipo: ")
    if tipo == 'unica' or tipo == 'multipla':
        alternativas = []
        print("Alternativas ou enter para finalizar")
        num = 1
        item = input(f"alternativa {num}: ")
        while item != '':
            alternativas.append(item)
            num = num + 1
            item = input(f"alternativa {num}: ")
    else:
        alternativas = None
    #colocando pergunta no repositorio
    repositorio.append(numero)
    repositorio.append(enunciado)
    repositorio.append(tipo)
    repositorio.append(alternativas)

def monta_pergunta(quest: list) -> str:
    resp = f"{quest[0]}) {quest[1]} "
    if quest[2] != 'aberta':
        op = "abcdefghijklmnopqrst"
        i = 0
        for alt in quest[3]:
            resp = resp + f"\n  {op[i]}) {alt}"
            i = i + 1
    return resp

def exibe_perguntas(repositorio: list):
    i = 0
    print("**********************************")
    while i < len(repositorio):
        quest = repositorio[i: i+4]
        info = monta_pergunta(quest)
        print(info)
        print("")
        i = i + 4
    print("**********************************")

def menu() -> int:
    print("1) Cadastra Pergunta")
    print("2) Aplica enquete")
    print("3) Visualiza perguntas")
    print("4) Apaga pergunta")
    print("5) Sair")
    return int(input("opção: "))

def apaga_pergunta(repositorio):
    num = int(input("Digite o nº da pergunta que deseja apagar: "))
    i = 0
    while i < len(repositorio) and repositorio[i] != num:
        i = i + 4
    
    if repositorio[i] == num:
        repositorio.pop(i)
        repositorio.pop(i)
        repositorio.pop(i)
        repositorio.pop(i)
    else:
        print("Nenhuma pergunta encontrada!")



#main
perguntas = [1, "Qual time vc torce?", 'aberta', None,
             2, "Quem vai ganhar a Champions?", 'unica', ['PSG', 'Inter'],
             3, "Melhor jogador?", 'multipla', ['Raphinha', 'Mbappe', 
                                               'Vini Jr', 'Yamal']]
opcao = 0
while opcao != 5:
    opcao = menu()
    if opcao == 1:
        cadastra_pergunta(perguntas)

    elif opcao == 2:
        print("aplicando a enquete")

    elif opcao == 3:
        exibe_perguntas(perguntas)

    elif opcao == 4:
        apaga_pergunta(perguntas)

    elif opcao != 5:
        print("Opção inválida")
