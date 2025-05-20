from datetime import date
def voto(n=0):
    if n < 18:
        return print(f'Com {n} anos: NÃO VOTA!')
    elif n < 65:
        return print(f'Com {n} anos: VOTO OBRIGATÓRIO!')
    else:
        return print(f'Com {n} anos: VOTO OPCIONAL!')


anoatual = date.today().year
anonasc = int(input('Digite o ano em que você nasceu: '))
idade = anoatual - anonasc
voto(idade)
