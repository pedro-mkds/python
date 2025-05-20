from time import sleep
from random import randint
def maior(* num):
    c = maior = 0
    print('\nAnalisando os valores passados...')
    for v in num:
        sleep(0.3)
        print(f'{v}', end=' ', flush=True)
        if c == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        c += 1
    print(f'Foram informados {c} valores ao todo')
    print(f'O maior valor informado foi: {maior}.')
        


maior(9, 7, 2, 3, 5, 4, 0)
maior(2, 8, 1)
maior(7, 0, 4, 10, 6, 3)
maior(5)
maior()
