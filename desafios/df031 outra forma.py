dist = float(input('Qual distância da sua viagem? '))
print('Você está preste a começar uma viagem de {}km'.format(dist))

if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))