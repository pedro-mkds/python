num = int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))


print(f'Foram digitados {num.count(9)}x o número 9')
if 3 in num:
    posição = num.index(3)
    print(f'O número 3 aparece na posição {posição}')
else:
    print('O número 3 não foi digitado')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')
