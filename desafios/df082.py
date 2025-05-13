val = list()
listaimpar = list()
listapar = list()
while True:
    val.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in ('SN'):
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Lista Geral: {sorted(val)}')

print('Extraindo dados e formando novas lista de números pares e ímpares...')

for cont in range(0, len(val)):
    if val[cont] % 2 == 0:
        listapar.append(val[cont])
    else:
        listaimpar.append(val[cont])
print(f'Lista Par: {sorted(listapar)}')
print(f'Lista Ímpar: {sorted(listaimpar)}')