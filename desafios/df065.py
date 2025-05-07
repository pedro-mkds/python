#Programa que le varios números inteiros e mostra a média entre eles e depois mostra qual foi o maior e qual foi o menor
s = c = m = maior = menor = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    m = s / c
    
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
print('Você digitou {} número e a média deles é de: {:.2f}.'.format(c, m))
print('Desses {} números o maior foi {} e o menor foi {}.'.format(c, maior, menor))