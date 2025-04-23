#Program que mostra todos os números pares que estão em um intervalo de 1 e 50

print('Esse programa mostra todos os números pares que estão em um intervalo de 1 e 50')
for c in range(0, 51):
    if c > 0 and c % 2 == 0:
        print(c)
print('fim')
