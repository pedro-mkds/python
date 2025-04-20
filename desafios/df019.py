nome = str(input('Digite seu nome completo: ')).strip()

print('Este é seu nome em maiúsculas {}'.format(nome.upper()))
print('Este é seu nome em minúsculas {}'.format(nome.lower()))
print('Seu nome tem {} letras '.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome {} possui {} letras'.format(separa[0], len(separa[0])))
