a = input('Digite um algo: ')

print('Só tem espaços? {}'.format(a.isspace()))
print('Contém números? {}'.format(a.isnumeric()))
print('Contém letras? {}'.format(a.isalpha()))
print('Contem letras e númers {}'.format(a.isalnum()))
print('Está em maiúsculos {}'.format(a.isupper()))
print('Está em minúsculas {}'.format(a.islower()))
print('Está em capitalizada {}'.format(a.istitle()))