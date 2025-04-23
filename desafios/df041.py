#Programa que calcula categoria, através da idade
from datetime import date
from time import sleep
print('-==-' * 15)
anonascimento = int(input('Digite o ano em que você nasceu: '))
anoatual = date.today().year
anos = anoatual - anonascimento
print('-==-' * 15)
print('Confederação Nacional de Natação! Vamos definir sua categoria')
print('-==-' * 15)
print('Processando dados...')
sleep (2)
if anos > 0 and anos <= 9:
    print('Como você tem 9 anos ou menos sua categoria é: MIRIM')
elif anos <= 14:
    print('Como você tem entre 10 e 14 anos sua categoria é: INFANTIL')
elif anos <= 19:
    print('Como você tem entre 15 e 19 anos ou menos sua categoria é: JUNIOR')
elif anos <= 24:
    print('Como você tem entre 20 e 24 anos sua categoria é: SÊNIOR')
elif anos >= 25:
    print('Como você tem mais de 25 anos sua categoria é: MASTER')
else:
    print('Você digitou uma data inválida')

