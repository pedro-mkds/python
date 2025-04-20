#Aprendo a fazer cálculos

# Ordem de precedência

# 1 - () Parênteses
# 2 - ** Potência
# 3 - * , / , // , % Multiplicação, divisão, divisão inteira, resto da divisão
# 4 - + e - Adição e subtração

v= int(input('Digite um valor: '))
v2= int(input('Digite outro valor: '))

a=v+v2
s=v-v2
m=v*v2
d=v/v2
p=v**v2
di=v//v2
rd=v%v2



print('A adição entre {} e {} é de {}'.format(v, v2, a), end='. ')
print('A subtração entre {} e {} é de {}'.format(v, v2, s), end='. ')
print('A multiplicação entre {} e {} é de {}'.format(v, v2, m), end='. ')
print('A divisão entre {} e {} é de {:.3f}'.format(v, v2, d), end='. ')
print('A potênciação entre {} e {} é de {}'.format(v, v2, p), end='. ')
print('A divisão inteira entre {} e {} é de {}'.format(v, v2, di), end='. ')
print('A entre {} e {} é de {}'.format(v, v2, rd), end='.')