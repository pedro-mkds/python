def met(p = 0, formato=False):
    return p / 2 if formato is False else moeda(p)


def dobro(p = 0, formato=False):
    return p * 2 if formato is False else moeda(p)


def aum(p = 0, x = 0, formato=False):
    return p + (p * (x / 100)) if formato is False else moeda(p)


def dim(p = 0, x = 0, formato=False):
    return p - (p * (x / 100)) if formato is False else moeda(p)


def moeda(p = 0, moeda = 'R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')
