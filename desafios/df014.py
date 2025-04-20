import math
co= float(input('Digite o valor do Cateto Oposto: '))
ca= float(input('Digite o valor do Cateto Adjancente: '))
hi= math.hypot(co,ca)
print('O valor da Hipotenusa é: {:.2f}'.format(hi))
