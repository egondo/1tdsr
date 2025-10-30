import banco

def cadastra_transacao(lancamento):
    banco.insere_lancamento(lancamento)
    info = {
        "valor": lancamento['valor'],
        "id": lancamento['conta_id']
    }
    banco.atualiza_saldo(info)

def recupera_transacoes(conta_id: int) -> list:
    lancamentos = banco.recupera_lancamentos(conta_id)    
    resultados = []
    for reg in lancamentos:
        info = {
            "tipo": reg[0],
            "data": reg[1],
            "observacao": reg[2],
            "valor": reg[3]
        }
        resultados.append(info)

    return resultados



def recupera_contas() -> list:
    registros = banco.recupera_contas()
    retorno = []
    for info in registros:
        conta = {
            "id": info[0],
            "numero": info[1],
            "agencia": info[2],
            "cliente": info[3],
            "saldo": info[4]
        }
        retorno.append(conta)
    return retorno

    