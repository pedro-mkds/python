dados = dict()
conjunto = list()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))
conjunto.append(dados.copy())
print(conjunto)
print(f'Nome é igual a {conjunto[0]['nome']}')
print(f'Média é igual a {conjunto[0]['media']}')
if conjunto[0]['media'] >= 6:
    print('Situação é igual a APROVADO')
else:
    print('Situação é igual a REPROVADO')