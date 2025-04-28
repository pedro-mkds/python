from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número de 0  10. Tente adivinhar...')
print('-=-' * 20)
sleep(3)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
t = 1
print('processando...')
sleep(1)
while jogador != computador:
    sleep(1)
    t += 1
    if jogador < computador:
        print('Mais... Tente ')
    elif jogador > computador:
        print('Menos... Tente mais uma vez')
    sleep(1)
    jogador = int(input('\nEm que número eu pensei? ')) #Jogador tenta adivinhar
print('PARABÉNS! Você conseguiu me vencer com um total de {} tentativa(as)!'.format(t))
