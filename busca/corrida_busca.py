import time
import busca

def cria_lista(qtd: int) -> list:
    resp = []
    for i in range(qtd):
        resp.append(i)

    return resp

dados = cria_lista(5_000_000)

t_ini = time.time()
for i in range(100):
    ret = busca.busca(dados, 7_000_000)
tempo = time.time() - t_ini
print(f"Busca demorou {tempo}s")

t_ini = time.time()
for i in range(100_000):
    ret = busca.busca_binaria(dados, 7_000_000)
tempo = time.time() - t_ini
print(f"Busca Binaria demorou {tempo}s")
