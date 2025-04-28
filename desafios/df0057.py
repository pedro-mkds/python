#Programa que le o sexo de uma pessoa mas so aceita os valores M e F. Caso esteja errado ira pedir a digitação novamente
s = str(input('Digite seu sexo [M/F]: ')).upper()[0]
while s not in 'MF':
    s = str(input('Dados inválidos! Digite seu sexo novamente [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(s))