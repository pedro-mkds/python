def met(p = 0):
    return p / 2


def dobro(p = 0):
    return p * 2


def aum(p = 0, x = 0):
    return p + (p * (x / 100))


def dim(p = 0, x = 0):
    return p - (p * (x / 100))


def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')
