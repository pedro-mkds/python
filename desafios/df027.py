velocidade = int(input('A quantos km/h você estava? '))
if velocidade <= 80:
  print('Tudo bem, você está dentro do limite permitido')
else:
  print('Mais cuidado da próxima vez, você ultrapassou o limite de velocidade permitido de 80km/h, e agora tera que pagar uma multa de R${:.2f}'.format((velocidade - 80)*7))