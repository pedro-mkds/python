salario = int(input('Digite o seu salário: '))

if salario > 1250:
  print('Parabéns você recebeu um aumento de 10%, seu novo salário sera de R${:.2f}'.format(salario+(salario*0.10)))
else:
  print('Parabéns você recebeu um aumento de 15%, seu novo salário sera de R${:.2f}'.format(salario+(salario*0.15)))