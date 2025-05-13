val = []
while True:
    val.append(int(input('Digite um valor: ')))
    
    continuar = ' '
    while continuar not in ('SN'):
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram digitados {len(val)} elementos.')
val.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente ficam: {val}')

if 5 in val:
    posição = val.index(5)
    print(f'O número 5 está na lista e ocupa a posição {posição}')
else:
    print('O número 5 não foi digitado!')