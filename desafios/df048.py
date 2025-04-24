#Programa que mostra a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        cont += 1
        s += c

print('A soma dos {} valores deu um total de: {}'.format(cont, s))
