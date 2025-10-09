def processa_primeiro_time(info: str) -> list:
    dados = info.strip().split(' ')
    if len(dados) == 2:
        return [dados[0], int(dados[1])]
    else:
        return [f"{dados[0]} {dados[1]}", int(dados[2])]

def processa_segundo_time(info: str) -> list:
    dados = info.strip().split(' ')
    if len(dados) == 2:
        return [dados[1], int(dados[0])]
    else:
        return [f"{dados[1]} {dados[2]}", int(dados[0])]
    

times = {}

with open('partidas.txt', mode='r', encoding='utf8') as arquivo:
    partidas = arquivo.readlines()
    for partida in partidas:
        print(partida)
        divisao = partida.strip().split('X')
        #print(divisao)
        time_casa = processa_primeiro_time(divisao[0])
        time_visi = processa_segundo_time(divisao[1])
        nome_cs = time_casa[0]
        gols_cs = time_casa[1]
        nome_vi = time_visi[0]
        gols_vi = time_visi[1]

        if nome_cs in times:
            time_cs = times[nome_cs]
        else:
            time_cs = {'vitorias': 0, 'empates': 0, 'derrotas': 0}
            times[nome_cs] = time_cs
        
        if nome_vi in times:
            time_vi = times[nome_vi]
        else:
            time_vi = {'vitorias': 0, 'empates': 0, 'derrotas': 0}
            times[nome_vi] = time_vi

        if gols_cs > gols_vi:
            time_cs['vitorias'] = time_cs['vitorias'] + 1
            time_vi['derrotas'] = time_vi['derrotas'] + 1

        elif gols_cs < gols_vi:
            time_vi['vitorias'] = time_vi['vitorias'] + 1
            time_cs['derrotas'] = time_cs['derrotas'] + 1
       
        else:
            time_cs['empates'] = time_cs['empates'] + 1
            time_vi['empates'] = time_vi['empates'] + 1


for chave in times.keys():
    time = times[chave]
    print(f'{chave}\tpontos: {3 * time['vitorias'] + time['empates']}')


