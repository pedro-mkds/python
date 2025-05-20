dados = dict()
conjunto = list()
dados['nome'] = str(input('Nome: ')).strip().title()
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 6:
    dados['situação'] = 'Aprovado'
elif dados['media'] >= 5:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
conjunto.append(dados.copy())

print('-=' * 30)
for k, v in dados.items():
    print(f' -{k} é igual a {v}')
