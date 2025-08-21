import busca

def unique(lista: list) -> list:
    resp = []
    for elem in lista:
        if busca.busca(resp, elem) == -1:
            resp.append(elem)
    
    return resp


if __name__ == "__main__":
    a = [2, 4, 0, 3, 2, 6, 3, 7]
    r = unique(a)
    print(r)
