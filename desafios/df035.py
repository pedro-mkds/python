#Programa se identifica sem 3 retas podem format um triangulo

print('Este programa irá identificar se 3 retas podem formar um triângulo')
r1 = float(input('Digite o valor da primeira reta:'))
r2 = float(input('Digite o valor da segunda reta:'))
r3 = float(input('Digite o valor da terceira reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estas retas podem formar um triângulo')
else:
    
    print('Estas retas não podem formar um triângulo')