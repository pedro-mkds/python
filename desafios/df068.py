from random import randint, choice

c = 0

while True:
    jogador = int(input('Escolha um valor de 0 a 10: '))
    computador = randint(0, 10) 
    analise = (jogador + computador)
    escjogador = ' '
    
    while escjogador not in 'PI':
        escjogador = str(input('Escolha PAR ou ÍMPAR [P / I]: ')).strip().upper()[0]
        
    if escjogador == 'P':
        
        if analise % 2 == 0:
            print(f'Você VENCEU! O jogador escolheu {jogador} e o computador escolheu {computador} e a soma é {analise}, DEU PAR')
            c += 1
            print('Vamos jogar novamente...')
            
        else:
            print(f'Você PERDEU! O jogador escolheu {jogador} e o computador escolheu {computador} e a soma é {analise}, DEU ÍMPAR')
            break
        
    elif escjogador == 'I':
        
        if analise % 2 != 0:
            print(f'Você VENCEU! O jogador escolheu {jogador} e o computador escolheu {computador} e a soma é {analise}, DEU ÍMPAR')
            c += 1
            print('Vamos jogar novamente...')
            
        else:
            print(f'Você PERDEU! O jogador escolheu {jogador} e o computador escolheu {computador} e a soma é {analise}, DEU PAR')
            break
            
        
        
print(f'Fim de jogo! Você venceu {c} vezes')