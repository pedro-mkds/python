#Programa que le 3 número e diz qual é o maior e qual é o maior

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))

#Verificando o menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
#Verificando o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior númerp é: {} .\n O menor número é: {}.'.format(maior, menor))
