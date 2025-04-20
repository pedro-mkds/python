from random import choice
nmr = int(input('Escolha em um número entre 0 e 5: '))
lista = [0,1,2,3,4,5]
escolhido = choice(lista)

if nmr == escolhido :
  print('Parabéns você acertou!')
else:
  print('Você errou!')
print('O número sorteado foi: {}'.format(escolhido))
