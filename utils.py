def trunca(texto, limite):
    if len(texto) <= limite:
        return texto

    return texto[:limite - 3] + '...'

def safe_input(text, type, sentinel):
    try:
        return type(input(text))
    except ValueError:
        return sentinel
