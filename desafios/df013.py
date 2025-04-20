dias= float(input('Quantos dias o carro foi alugado? '))
km= float(input('Quantos km foram rodados durantes esse dias? '))

pago= (dias*60)+(km*0.15)

print('Sabendo que você alugou o carro por {:.0f} dias e andou nesse período {:.0f}km. \n A sua conta final a pagar sera de: R${:.2f}'.format(dias, km, pago))