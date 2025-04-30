#Programa que le um número inteiro e mostra na tela os primeiros elementos de uma Sequência de Fibonacci

n = int(input('Digite um número inteiro: '))
v1 = 0
v2 = 1
cont = 3
print('{} -> {}'.format(v1, v2), end='')
while cont <= n:
    v3 = v1 + v2
    print(' -> {}'.format(v3), end='')
    cont += 1
    v1 = v2
    v2 = v3
print(' -> Fim')