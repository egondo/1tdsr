import baralho as bar

def quer_carta(mao: list) -> bool:
    print(mao)
    resp = input("Quer carta? ")
    if resp == 'S':
        return True
    else:
        return False
    
def get_pontos(mao) -> int:
    pontos = 0
    for carta in mao:
        if carta[0] > 10:
            pontos = pontos + 10
        else:
            pontos = pontos + carta[0]
    return pontos


deck = bar.cria()
bar.embaralha(deck)

mao_cpu = bar.distribui(deck, 2)
mao_hum = bar.distribui(deck, 2)

while quer_carta(mao_hum):
    c = bar.compra(deck)
    mao_hum.append(c)

while quer_carta(mao_cpu):
    c = bar.compra(deck)
    mao_cpu.append(c)

pontos_hum = get_pontos(mao_hum)
pontos_cpu = get_pontos(mao_cpu)

if pontos_hum > pontos_cpu and pontos_hum <= 21:
    print("Ser humano venceu!")
elif pontos_hum < pontos_cpu and pontos_cpu <= 21:
    print("Computador venceu!")
elif pontos_cpu > 21 and pontos_hum <= 21:
    print("Ser humano Venceu!")
elif pontos_cpu <= 21 and pontos_hum > 21:
    print("CPU Venceu!")
else:
    print("CPU Venceu!")    



