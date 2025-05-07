
while True:
    print('=' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 40)
    if n < 0:
        break
    for c in range(1, 11):
        t = n * c
        print(f'{n} X {c} = {t} ')

print('O Programa foi ENCERRADO. Volte sempre!') 