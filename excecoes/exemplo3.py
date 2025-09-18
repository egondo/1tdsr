def recupera(chave: str):
    dic = {
        "SP": "São Paulo",
        "RS": "Porto Alegre",
        "MG": "Belo Horizonte",
        "BA": "Salvador"
    }
    if chave in dic:
        return dic[chave]
    else:
        raise KeyError(f"{chave} nao existe no dicionario")

if __name__ == "__main__":
    print(recupera("RS"))