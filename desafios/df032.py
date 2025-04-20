#Programa que mostra se um ano é bissexto ou não

ano = int(input('Digite um ano para descobrir se ele é bissexto ou não: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
  print('{} é um ano bissexto!'.format(ano))
else:
  print('{} náo é um ano bissexto!'.format(ano))