#Programa que le o peso de 5 pessoas e mostra qual é o maior peso e qual é o menor peso.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.2f}Kg.'.format(maior))
print('O menor peso lido foi de {:.2f}Kg.'.format(menor))