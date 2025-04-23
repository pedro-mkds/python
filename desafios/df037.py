#Programa que transforma um número em: Binário, Octagonal e Hexadecimal

numero = int(input('Digite um número qualquer: '))

binario = bin(numero)
octagonal = oct(numero)
hexadecimal = hex(numero)

print('Seu número convertido para Binário fica: {}'.format(binario[2:]))
print('Seu número convertido para Octagonal fica: {}'.format(octagonal[2:]))
print('Seu número convertido para Hexadecimal fica: {}'.format(hexadecimal[2:]))