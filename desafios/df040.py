#Programa para calcular média
from time import sleep
m1 = float(input('Digite sua primeira nota: '))
m2 = float(input('Digite sua segunda nota: '))
m3 = float(input('Digite sua terceira nota: '))
media = (m1 + m2 + m3) / 3
print('===' * 20)
print('Vamos calcular sua média!')
print('===' *20 )

print('Calculando sua média...')
sleep(3)
print('===' * 20)
if media >= 7:
    print('PARABÉNS! Você foi aprovado!')
elif  media >= 5:
    print('Você ficou de recuperação! Pois não atingiu a média pedida.')
else:
    print('REPROVADO! Você não atingiu a média minima para recuperação e foi reprovado.')
print('===' * 20)
print('Sua média foi de: {:.2f}'.format(media))
print('===' * 20)