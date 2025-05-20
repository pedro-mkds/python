conjunto = list()

while True:
    dados = dict()
    gols = list()

    dados['nome'] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(partidas):
        gol = int(input(f'Quantos gols {dados["nome"]} fez no {c + 1}° jogo? '))
        gols.append(gol)

    dados['gols'] = gols
    dados['totgols'] = sum(gols)
    conjunto.append(dados.copy())

    while True:
        continuar = input('Deseja cadastrar mais um jogador [S/N]? ').strip().upper()
        if continuar in ('S', 'N'):
            break

    if continuar == 'N':
        break

# Exibição dos dados em forma de tabela
print()
print('-=' * 40)
print(f'{"COD":<5}{"NOME":<15}{"GOLS":<20}{"TOTAL DE GOLS":<15}')
print('-' * 60)

for i, jogador in enumerate(conjunto):
    print(f'{i:<5}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["totgols"]:<15}')

print('-=' * 40)
