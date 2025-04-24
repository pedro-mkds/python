#Programa que le o ano de nascimento de 7 pessoas. E depois mostra quantos são menor de idade e quantas ja atingiram a maior idade
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(0, 7):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoa(as) são maior de idade e {} são menores de idade'.format(totmaior, totmenor))
