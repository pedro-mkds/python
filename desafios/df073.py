times = ('Palmeiras', 'Red Bull Bragantino', 'Flamengo', 'Cruzeiro', 'Fluminense', 'Bahia', 'Ceará', 'Corinthians', 'Internacional', 'Atlético-MG', 'São Paulo', 'Botafogo', 'Grêmio', 'Vasco', 'Juventude', 'Mirassol', 'Fortaleza', 'Vitória', 'Santos', 'Sport')

print('Tabela dos 20 primeiros colocados do campeonato Brasileiro de Futebol são:')
for cont in range(0, len(times)):
    print(f'{cont + 1}° Lugar: {times[cont]}')

print(f'Os 5 primeiros times são: {times[:5]}')

print(f'Os 4 útlimos times são: {times[-4:]}') 

print(f'Os times em ordem alfábetica ficam: {sorted(times)}')

posição = times.index('Grêmio')
print(f'O Grêmio se econtra na {posição}° posição')
