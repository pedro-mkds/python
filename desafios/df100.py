from random import randint
from time import sleep

def sortear(lst):
    for c in range(0, 5):
        lst.append(randint(0,10))
    print(f'Foram gerados os seguintes números: ', end='')
    for c in lst:
        print(f'{c}', end=' ', flush=True)
        sleep(0.5)
    print(' Pronto!')
    
def pares(v):
    soma = 0
    for c in v:
        if c % 2 == 0:
            soma += c
    print(f'\nA soma dos números pares desta lista é: {soma}')


lista = list()
sortear(lista)
pares(lista)