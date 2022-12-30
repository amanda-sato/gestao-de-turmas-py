def trunca(texto, limite):
    if len(texto) <= limite:
        return texto

    return texto[:limite - 3] + '...'
