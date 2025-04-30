#Programa que le um número inteiro e mostra na tela os primeiros elementos de uma Sequência de Fibonacci

n = int(input('Digite um número inteiro: '))
primeiro = 0
segundo = 1
cont = 3
print('{} -> {}'.format(primeiro, segundo), end='')
while cont <= n:
    terceiro = primeiro + segundo
    print(' -> {}'.format(terceiro), end='')
    cont += 1
    primeiro = segundo
    segundo = terceiro
print(' -> Fim')
    
    