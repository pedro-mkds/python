matriz = list()
for l in range(0, 3):
    for c in range(0,3):
        num = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        matriz.append(num)

print(matriz)
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')
