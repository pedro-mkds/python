def info(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = 0
    else:
        gol = int(gol)
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')


nome = str(input('Nome do jogador: ')).strip()
gol = input('Quantos gols o jogador fez? ').strip()
info(nome, gol)
