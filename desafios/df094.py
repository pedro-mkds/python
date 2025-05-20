dados = dict()
conjunto = list()
somaidade = 0

while True:
    dados['nome'] = input('Nome: ').strip().title()

    while True:
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo in ('M', 'F'):
            dados['sexo'] = sexo
            break
        else:
            print('Digite apenas "M" para Masculino ou "F" para Feminino.')

    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    conjunto.append(dados.copy())

    while True:
        continuar = input('Deseja continuar [S/N]? ').strip().upper()
        if continuar in ('S', 'N'):
            break

    if continuar == 'N':
        break

# Média
med_idade = somaidade / len(conjunto)

print('\n' + '-=' * 30)
print(f'Foram cadastradas {len(conjunto)} pessoa(s)')
print('-=' * 30)
print(f'Média de idade do grupo: {med_idade:.1f}')

# Lista de mulheres
print('Lista de mulheres cadastradas:')
mulheres = [p for p in conjunto if p['sexo'] == 'F']
if mulheres:
    for m in mulheres:
        print(f" - {m['nome']}")
else:
    print(' => Nenhuma mulher foi cadastrada!')

print('-=' * 30)

# Lista acima da média
print('Lista de pessoas com idade acima da média:')
acima = [p for p in conjunto if p['idade'] > med_idade]
if acima:
    for p in acima:
        print(f" - {p['nome']} com {p['idade']} anos")
else:
    print(' => Não há pessoas com idade acima da média!')

print('-=' * 30)