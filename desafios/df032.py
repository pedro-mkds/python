#Programa que mostra se um ano é bissexto ou não

from datetime import date

ano = int(input('Digite um ano para descobrir se ele é bissexto ou não. Coloque 0 para saber se o ano atual: '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} náo é um ano bissexto!'.format(ano))