#programa que calcula distancia de uma viagem e mostra o custo dessa viagem

dist = int(input('Quantos Km teve sua última viagem? '))

if dist <= 200:
  print('Sua viagem teve um custo de R$0.50 por KM, ficando um total de R${:.2f}'.format(dist*0.50))
else:
  print('Sua viagem teve um custo de R$0.45 por KM, ficando um total de R${:.2f}'.format(dist*0.45))