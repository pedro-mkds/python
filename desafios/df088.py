from random import randint
print('Gerador de palpites MEGA SENA')
conjunto = list()
quantjog = int(input('Digite quantos jogos serão: '))

for c in range(0, quantjog):
    palpites = []
    for q in range(0, 6):
        palpites.append(randint(1, 60))
    conjunto.append(palpites)   
        
for c, v in enumerate(conjunto):
    print(f'Palpite {c+1}° jogo: {v}')