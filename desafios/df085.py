
par = list()
impar = list()
conjunto = [par,impar]

for c in range(1,8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'\nOs valores pares digitados foram: {sorted(conjunto[0])}')
print(f'Os valores ímpares digitados foram: {sorted(conjunto[1])}')