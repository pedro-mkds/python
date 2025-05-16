matriz = list()
for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        linha.append(num)
    matriz.append(linha)

print('\nMatriz formatada:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
