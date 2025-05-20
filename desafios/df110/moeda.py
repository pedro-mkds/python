def met(p=0, formato=False):
    res = p / 2
    return res if not formato else moeda(res)

def dobro(p=0, formato=False):
    res = p * 2
    return res if not formato else moeda(res)

def aum(p=0, x=0, formato=False):
    res = p + (p * (x / 100))
    return res if not formato else moeda(res)

def dim(p=0, x=0, formato=False):
    res = p - (p * (x / 100))
    return res if not formato else moeda(res)

def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:>.2f}'.replace('.', ',')

def resumo(p=0, a=10, d=5, form=False):
    if form == 'S':
        form = True
    elif form == 'N':
        form = False

    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p) if form else p}')
    print(f'Dobro do preço: \t{dobro(p, form)}')
    print(f'Metade do preço: \t{met(p, form)}')
    print(f'Aumento de {a}%: \t{aum(p, a, form)}')
    print(f'Redução de {d}%: \t{dim(p, d, form)}')
    print('-' * 30)
