#Programa para simular empréstimo
from time import sleep
print('-=-' * 20)
print('Simulador de empréstimo')
print('-=-' * 20)
valordacasa = int(input('Qual o valor da casa? R$'))
salario = float(input('Qual é sua renda mensal? R$'))
anos = int(input('Em quantos anos vai pagar? '))
print('-=-' *20)
print('Analisando dados...')
sleep(3)

valorprestacao = valordacasa / (anos * 12)
limite = salario * 0.3
parcelas = anos * 12

if valorprestacao <= limite:
    print('Empréstimo APROVADO. O valor da prestação, não excedeu o limite de 30% do seu salário. ')
    print('Confirmando os dados...')
    sleep(1.5)
    print('Valor da casa R${:.2f} \nSeu salário R${:.2f}. \nPrazo do pagamento {} anos.'.format(valordacasa, salario, anos))
    print('O pagamento sera de {} parcelas, de R${:.2f}'.format(parcelas, valorprestacao))
    
elif valorprestacao > limite:
    print('Empréstimo NEGADO.')
    print('Seu empréstimo foi negado pois as prestações ultrapassaram o limite de R${:.2f} (30% do seu salário).'.format(limite))
    
else:
    print('Algo deu errado. Tente novamente.')