
def max_min(conjunto) -> tuple:
    aux_max = conjunto[0]
    aux_min = conjunto[0]

    for numero in conjunto:
        if numero >= aux_max:
            aux_max = numero
        elif numero <= aux_min:
            aux_min = numero

return aux_min, aux_max
        

if __name__ == "_main__":
    c = [0, 10, 67, 43]
    retorno = max_min(c)
    print(retorno)
