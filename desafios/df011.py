salário= float(input('Calculadora de reajuste salarial. \nDigite seu salário atual: '))
aumento= float(input('Digite a porcentagem do seu aumento: '))
salárioatual= salário + (salário * aumento / 100)

reajuste= salárioatual-salário

print('Seu salário atual sera de R${:.2f}'.format(salárioatual))
print('Seu aumento foi de R${:.2f}'.format(reajuste))