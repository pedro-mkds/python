#Leitor de número

num = int(input('Digite um número: '))
n = str(num)

print('Analisando número {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))