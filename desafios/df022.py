#Programa que verifica se o nome possui a palavra 'Silva'

nome = str(input('Digite seu nome: ')).strip()
verificar = bool(nome.upper().count('SILVA'))

print('Seu nome possui a palavra Silva = {}'.format(verificar))

#outra forma

print('Seu nome possui a palavra Silva = {}'.format('silva' in nome.lower()))
