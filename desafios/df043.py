#Programa que calcula o IMC de uma pessoa
from time import sleep
print('-=-' * 20)
print('Calculadora de IMC')
print('-=-' * 20)
print('O cálculo do IMC é feito da seguinte forma: \nDivida o seu peso em quilos pela sua altura em metros ao quadrado')
print('-=-' * 20)
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2) 
print('Processando dados...')
sleep(2)
print('Calculando imc...')
sleep(2)
print('Terminando análise e gerando resultado...')
sleep(3)
print('-=-' * 20)
if imc < 18.5:
    print('Você está abaixo do peso')
    print('Seu IMC está {:.2f}, o ideal seria de 18.50 a 25'.format(imc))
elif imc <= 25:
    print('Seu peso é ideal')
    print('Seu IMC está {:.2f}, que se encaixa dentro do ideal que é de 18.50 a 25'.format(imc))
elif imc <= 30:
    print('Você está com sobrepeso')
    print('Seu IMC está {:.2f}, o ideal seria de 18.50 a 25'.format(imc))
elif imc <= 40:
    print('Você esta com obesidade')
    print('Seu IMC está {:.2f}, o ideal seria de 18.50 a 25'.format(imc))
elif imc > 40:
    print('Tome cuidado! Você está com obesidade mórbida')
    print('Seu IMC está {:.2f}, o ideal seria de 18.50 a 25'.format(imc))
else:
    print('Você digitou uma medida inválida!')