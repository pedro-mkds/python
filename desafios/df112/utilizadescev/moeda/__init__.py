def met(p=0, formato=False):
    """
    Calcula a metade de um valor.

    Parâmetros:
    - p (float): Valor a ser dividido.
    - formato (bool): Se True, retorna o valor formatado em moeda.

    Retorna:
    - float ou str: Metade do valor, formatado ou não.
    """
    res = p / 2
    return res if not formato else moeda(res)


def dobro(p=0, formato=False):
    """
    Calcula o dobro de um valor.

    Parâmetros:
    - p (float): Valor a ser duplicado.
    - formato (bool): Se True, retorna o valor formatado em moeda.

    Retorna:
    - float ou str: Dobro do valor, formatado ou não.
    """
    res = p * 2
    return res if not formato else moeda(res)


def aum(p=0, x=0, formato=False):
    """
    Calcula o aumento percentual sobre um valor.

    Parâmetros:
    - p (float): Valor base.
    - x (float): Percentual de aumento.
    - formato (bool): Se True, retorna o valor formatado em moeda.

    Retorna:
    - float ou str: Valor com aumento aplicado, formatado ou não.
    """
    res = p + (p * (x / 100))
    return res if not formato else moeda(res)


def dim(p=0, x=0, formato=False):
    """
    Calcula o desconto percentual sobre um valor.

    Parâmetros:
    - p (float): Valor base.
    - x (float): Percentual de desconto.
    - formato (bool): Se True, retorna o valor formatado em moeda.

    Retorna:
    - float ou str: Valor com desconto aplicado, formatado ou não.
    """
    res = p - (p * (x / 100))
    return res if not formato else moeda(res)


def moeda(p=0, moeda='R$'):
    """
    Formata um valor numérico como moeda brasileira.

    Parâmetros:
    - p (float): Valor numérico.
    - moeda (str): Símbolo da moeda (padrão 'R$').

    Retorna:
    - str: Valor formatado como moeda.
    """
    return f'{moeda}{p:>.2f}'.replace('.', ',')


def resumo(p=0, a=10, d=5, form=False):
    """
    Exibe um resumo formatado com várias operações financeiras sobre um valor.

    Parâmetros:
    - p (float): Valor base.
    - a (float): Percentual de aumento.
    - d (float): Percentual de desconto.
    - form (bool ou str): Se 'S' ou True, ativa a formatação dos valores.

    Retorna:
    - None. Apenas exibe o resumo no console.
    """
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
