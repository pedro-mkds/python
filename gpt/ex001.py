#Programa que le a idade de uma pessoa e diz em que fase ela está:

idade = int(input('Digite sua idade: '))

if idade < 0:
    print('Você digitou uma idade inválida')
elif idade <= 12:
    print('Você é uma criança')
elif idade <= 17:
    print('Você é um adolescente')
elif idade <= 59:
    print('Você é adulto')
else:
    print('Você é idoso')