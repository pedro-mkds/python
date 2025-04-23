#Programa que faz o computador jogar Jokenpô
from random import choice
from time import sleep
jokenpo = ['pedra', 'papel', 'tesoura']
computador = choice(jokenpo)
jogador = str(input('Escolha: pedra, papel ou tesoura: ')).strip().lower()

print('=' *30)
print('Vamos jogar Jokenpô!')
print('=' *30) 
print('=' *30)
print('O jogador e o computador já escolheram. Vamos começar!')
sleep(1)
print('Pedra...')
sleep(1)
print('Papel...')
sleep(2)
print('Tesoura!')
print('=' *30)
sleep(2)

if jogador.lower() not in jokenpo:
    print('Jogada inválida! Tente novamente.')
elif jogador == computador:
    print('O jogo deu empate!')
elif jogador == 'pedra' and computador == 'tesoura':
    print('O jogador venceu!')
elif jogador == 'papel' and computador == 'pedra':
    print('O jogador venceu!')
elif jogador == 'tesoura' and computador == 'papel':
    print('O jogador venceu!')
else:
    print('O computador venceu!')
    
print('O jogador escolheu {} e o computador escolheu {}'.format(jogador, computador))
