import random

with open('partidas.txt', mode="a") as arq:
    times = ['Palmeiras', 'Santos', 'São Paulo', 'Corinthians', 'RB Bragantino', 'São Caetano']

    for i in range(len(times)):
        for j in range(i+ 1, len(times)):
            gc = random.randint(0, 7)
            gv = random.randint(0, 7)
            arq.write(f"{times[i]} {gc} X {gv} {times[j]}\n")
