matriz = list()
soma = soma3col = maior = menor = 0

for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        linha.append(num)

        if num % 2 == 0:
            soma += num

        if c == 2:
            soma3col += num

        if l == 1:
            if c == 0:
                maior = menor = num
            else:
                if num > maior:
                    maior = num
                if num < menor:
                    menor = num

    matriz.append(linha)

print('\nMatriz formatada:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^3} ]', end=' ')
    print()

print(f'\nA soma de todos os valores pares é de: {soma}')
print(f'A soma dos valores da 3ª coluna é de: {soma3col}')
print(f'O maior valor da 2ª linha é: {maior}')
