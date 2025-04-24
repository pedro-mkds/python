#Programa que le um número inteiro e diz se ele é primo ou não

num = int(input('Digite um número inteiro: '))
divisoes = 0

for c in range(1, num + 1):
    if num % c == 0:
        divisoes += 1
        
if divisoes == 2:
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')