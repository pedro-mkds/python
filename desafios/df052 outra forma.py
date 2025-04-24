num = int(input('Digite um número: '))
tot = 0
if num > 0:
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end='')
            tot += 1
        else:
            print('\033[31m', end='')
        print('{}'.format(c), end='')
    print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
    if tot <= 2 and tot > 0:
        print('{} é um número PRIMO!'.format(num))
    else:
        print('{} NÃO é um número primo.'.format(num))
else:
    print('Você digitou um valor inválido')
