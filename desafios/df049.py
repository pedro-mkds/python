#Programa que mostra a tabuada de um número v2.0

n = int(input('Digite um número que te mostrarei a tabuada dele completa: '))
for c in range(1, 11):
    print('{} X {} = {}'.format(n, c, n * c))
print('Fim')