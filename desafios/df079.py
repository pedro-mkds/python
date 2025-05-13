val = list()
while True:
    num = int(input('Digite um valor: '))
    if num in val:
        print('Você ja digitou esse número. Tente novamente.')
    else:
        val.append(num)
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if continuar == 'N':
        break
    
print(f'Você digitou os seguintes número: {sorted(val)}')