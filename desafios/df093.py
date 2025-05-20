gols = []
dados = {}
conjunto = []

# Coleta de dados
dados['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))

for c in range(partidas):
    gol = int(input(f"Quantos gols {dados['nome']} fez no {c + 1}° jogo? "))
    gols.append(gol)

# Salvando dados
dados['gols'] = gols[:]
dados['totgols'] = sum(gols)
conjunto.append(dados.copy())

# Exibição
print('\n' + '-=' * 30)
print(conjunto)
print('-=' * 30)
print(f"\nO jogador {dados['nome']} participou de {partidas} partidas.")
for c, g in enumerate(dados['gols']):
    print(f"    => No {c + 1}° jogo marcou {g} gols")
print(f"    TOTAL DE GOLS: {dados['totgols']}")
print('-=' * 30)
