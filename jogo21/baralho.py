import random

def cria() -> list:
    monte = []
    naipes = ("ouros", "espadas", "copas", "paus")
    for naipe in naipes:
        for valor in range(1, 14):
            monte.append( (valor, naipe) )
    return monte


def compra(monte: list) -> tuple:
    if len(monte) > 0:
        carta = monte.pop(0)
    else:
        carta = None 
    return carta

def distribui(monte: list, n: int) -> list:
    mao = []
    for i in range(0, n):
        mao.append(compra(monte))
    return mao

def embaralha(monte: list):
    for i in range(200):
        x = random.randint(0, len(monte) - 1)
        y = random.randint(0, len(monte) - 1)
        aux = monte[x]
        monte[x] = monte[y]
        monte[y] = aux


if __name__ == "__main__":
    deck = cria()
    for card in deck:
        print(card) 

