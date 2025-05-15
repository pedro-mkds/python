matriz = list()
soma = soma3col = maior = menor = 0
for l in range(0, 3):
    for c in range(0,3):
        num = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        matriz.append(num)
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
        

print(matriz)
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')


print(f'A soma de todos os valores pares é de: {soma}')
print(f'A soma de todos os valores da 3º coluna é de: {soma3col}')
print(f'A soma de todos os valores da 2º linha é de: {maior}')
