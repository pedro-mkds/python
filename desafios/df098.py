from time import sleep
def contador(a, b, c):
    print(f'Contagem de {a} até {b}, pulando de {c} em {c}')
    if c == 0:
        c = 1
    if a < b:
        while a <= b:
            print(f'{a}', end=' ', flush=True)
            sleep(0.5)
            a += abs(c)
    else:
        while a >= b:
            print(f'{a}', end=' ', flush=True)
            sleep(0.5)
            a -= abs(c)
    
    print('\nFIM!')
    print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
contador(i, f, p)