def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('= ', end='')
    return f


num = int(input('Digite um número: '))
resp = input('Gostaria de ver o fatorial completo [S/N]? ').strip().upper()
show = resp == 'S'

resultado = fatorial(num, show)
print(resultado)

help(fatorial)
