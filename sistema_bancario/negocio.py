import banco


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

    