#Programa que le nomes

nome = str(input('Digite seu nome completo: ')).strip()
pn = nome.split()
un = pn[::-1]

print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(pn[0]))
print('Seu último nome é {}'.format(un[0]))


#outra forma

nome2 = str(input('Digite seu nome completo: ')).strip().split()

print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome2[0]))
print('Seu último nome é {}'.format(nome2[len(nome2)-1]))