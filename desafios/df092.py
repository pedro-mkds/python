import datetime

dados = dict()
conjunto = list()
anoatual = datetime.datetime.now().year
dados['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['anocon'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))

dados['aposentadoria'] = idade + ((dados['anocon'] + 35) - anoatual)
conjunto.append(dados.copy())
print('-=' * 30)
print('== INFORMAÇÕES ==')
print('-=' * 30)
print(f'Nome: {dados["nome"]}.')
print(f'Idade: {idade}.')
print(f'Carteira de Trabalho: {dados["ctps"]}.')
if dados['ctps'] != 0:
    print(f'Contratação: {dados["anocon"]}.')
    print(f'Salário: R${dados["salario"]:.2f}.')
    print(f'Ira se aposentar com: {dados["aposentadoria"]} anos.')
