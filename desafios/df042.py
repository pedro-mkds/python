#Programa que mostra se um triângulo é Equilatero, Isóceles ou Escaleno

print('Este programa irá identificar se 3 retas podem formar um triângulo e dira se ele é Equilatero, Isóceles ou Escaleno')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

equilatero = r1 == r2 == r3
isoceles = r1 == r2 or r1 == r3 or r2 == r3
escaleno = r1 != r2 != r3


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estas retas podem formar um triângulo')
    if r1 == r2 == r3: 
        print('Seu triângulo é equilatero, pois possui 3 lados iguais!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Seu triângulo é isoceles, pois possui 2 lados iguais!')
    elif r1 != r2 != r3:
        print('Seu triângulo é escaleno, pois não possui lados iguais!')
else:
    print('Estas retas não podem formar um triângulo')