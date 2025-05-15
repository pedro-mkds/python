conjunto = list()
c = 0

while True:
    dados = []
    while True:
        nome = input('Nome: ').strip()
        if nome.replace(' ', '').isalpha():
            dados.append(nome.title())
            break
        else:
            print('❌ Digite o nome apenas usando letras. Evite símbolos e números.')
    while True:
        try:
            peso = int(input('Peso em kg: '))
            if peso > 0:
                dados.append(peso)
                break
            else:
                print('❌ Seu peso deve ser maior ou igual a 1kg')
        except ValueError:
            print('❌ Digite apenas números inteiros')
    while True:
        try:
            altura = int(input('Digite sua altura em cm: '))
            if altura > 0:
                dados.append(altura)
                break
            else:
                print('❌ Seu peso deve ser maior ou igual a 1cm')
        except ValueError:
            print('❌ Digite apenas números inteiros')
        
    continuar = ' '
    while continuar not in ('SN'):
        conjunto.append(dados)
        c += 1
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

magreza = list() # 0.0 a 18.4
peso_normal = list() # 18.5 a 24.9
sobrepeso = list() # 25.0 a 29.9
obesidade1 = list() # 30.0 a 34.9
obesidade2 = list() # 35.0 a 39.9
obesidade3 = list() # 40.0 a 100.0

for s in conjunto:
    imc = s[1] / ((s[2] / 100) ** 2)
    if imc <= 18.4:
        magreza.append(s[0])
    elif imc <= 24.9:
        peso_normal.append(s[0])
    elif imc <= 29.9:
        obesidade1.append(s[0])
    elif imc <= 34.9:
        obesidade2.append(s[0])
    elif imc <= 35:
        obesidade3.append(s[0])
        
print('\n===== CLASSIFICAÇÃO DE PESSOAS POR NÍVEL DE IMC =====\n')

print(f'Total de pessoas cadastradas: {len(conjunto)}')

print(f'\nMagreza (IMC de 0.0 a 18.4) - {len(magreza)} pessoa(s):')
for pessoa in magreza:
    print(f'  - {pessoa}')

print(f'\nPeso Normal (IMC de 18.5 a 24.9) - {len(peso_normal)} pessoa(s):')
for pessoa in peso_normal:
    print(f'  - {pessoa}')

print(f'\nSobrepeso (IMC de 25.0 a 29.9) - {len(sobrepeso)} pessoa(s):')
for pessoa in sobrepeso:
    print(f'  - {pessoa}')

print(f'\nObesidade Grau I (IMC de 30.0 a 34.9) - {len(obesidade1)} pessoa(s):')
for pessoa in obesidade1:
    print(f'  - {pessoa}')

print(f'\nObesidade Grau II (IMC de 35.0 a 39.9) - {len(obesidade2)} pessoa(s):')
for pessoa in obesidade2:
    print(f'  - {pessoa}')

print(f'\nObesidade Grau III (IMC de 40.0 a 100.0) - {len(obesidade3)} pessoa(s):')
for pessoa in obesidade3:
    print(f'  - {pessoa}')
    